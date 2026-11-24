"""Check that every mesh in dataset/ is valid.

A valid mesh is orientable, connected, vertex-manifold and closed, does not intersect itself (so it is
embedded in 3D space), and bounds a handlebody.

A handlebody (https://en.wikipedia.org/wiki/Handlebody) is a ball with solid handles attached: a thickened
graph. A closed surface of genus 0 always bounds a ball (Alexander), so it passes right away. A closed surface
of higher genus can bound something else, for example a block with a knotted tunnel through it.

The check fills the solid with tetrahedra and collapses it: a tetrahedron is removed through a triangle that
no other tetrahedron uses, then a triangle through an edge that no other triangle uses. If only edges remain,
the solid collapses onto a graph and is a handlebody. A greedy collapse can get stuck on a real handlebody,
so a few random orders are tried before a mesh fails.

Every mesh, of any genus, must also be fillable by TetGen, which keeps the surface exactly. TetGen refuses
surfaces that touch or intersect themselves, including triangles folded flat onto a neighbour, so this
also confirms that the mesh is embedded. TetGen sometimes crashes on such input, so it runs in a separate
process.

Usage:  python resources/tools/preprocessing/validate.py
Needs:  pip install -r resources/tools/requirements.txt
"""

import multiprocessing
import queue
from collections import defaultdict, deque
from pathlib import Path

import numpy as np
import trimesh

from convert import DEFAULT_DATASET_PATH, load_trimesh


TRIES = 3
TET_FACES = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
TRI_EDGES = [[0, 1], [1, 2], [0, 2]]


def _collapse(cells: np.ndarray, faces_of: list, rng) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Remove cells through free faces (faces on exactly one remaining cell), until none are left.

    Returns (which cells remain, all faces, which faces remain)."""
    k = len(faces_of)
    faces, inverse = np.unique(np.sort(cells[:, faces_of].reshape(-1, len(faces_of[0])), axis=1),
                               axis=0, return_inverse=True)
    cell_faces = inverse.reshape(-1, k)
    order = np.argsort(inverse, kind="stable")  # incidences grouped per face
    starts = np.searchsorted(inverse[order], np.arange(len(faces) + 1))
    count = np.diff(starts)
    cell_alive = np.ones(len(cells), bool)
    face_alive = np.ones(len(faces), bool)
    free = np.flatnonzero(count == 1)
    rng.shuffle(free)
    queue = deque(free.tolist())
    while queue:
        f = queue.popleft()
        if not face_alive[f] or count[f] != 1:
            continue
        c = next(i // k for i in order[starts[f]:starts[f + 1]] if cell_alive[i // k])
        cell_alive[c] = False
        face_alive[f] = False
        for g in cell_faces[c]:
            if face_alive[g]:
                count[g] -= 1
                if count[g] == 1:
                    queue.append(g)
    return cell_alive, faces, face_alive


def _collapses_to_graph(tets: np.ndarray, rng) -> bool:
    tets_left, triangles, triangle_alive = _collapse(tets, TET_FACES, rng)
    if tets_left.any():
        return False
    triangles = triangles[triangle_alive]
    return len(triangles) == 0 or not _collapse(triangles, TRI_EDGES, rng)[0].any()


def _genus(mesh) -> int:
    return (2 - mesh.euler_number) // 2


def _tetgen(vertices, faces, switches, out):
    import tetgen

    try:
        tg = tetgen.TetGen(vertices, faces)
        tg.tetrahedralize(switches=switches)
        out.put(np.asarray(tg.elem))
    except RuntimeError as error:
        out.put(str(error))


def _tetgen_safely(vertices, faces, switches):
    """TetGen in a child process, so a crash inside TetGen cannot take the caller down."""
    ctx = multiprocessing.get_context("spawn")
    out = ctx.Queue()
    process = ctx.Process(target=_tetgen, args=(vertices, faces, switches, out))
    process.start()
    result = None
    while result is None:
        try:
            result = out.get(timeout=1)
        except queue.Empty:
            if not process.is_alive() and out.empty():
                break  # TetGen crashed
    process.join(5)
    if process.is_alive():
        process.kill()
    return result if isinstance(result, np.ndarray) else None


def _tetrahedralize(mesh) -> np.ndarray:
    """Tetrahedra filling the solid bounded by the mesh, with the same boundary topology."""
    vertices, faces = np.asarray(mesh.vertices, float), np.asarray(mesh.faces, np.int32)
    for switches in ("pQ", "pYQ"):  # "Y" (no extra points on the surface) avoids some TetGen failures
        tets = _tetgen_safely(vertices, faces, switches)
        if tets is not None:
            return tets
    raise RuntimeError("TetGen could not fill the mesh, so it is not embedded")


def is_handlebody(mesh, tets: np.ndarray | None = None) -> bool:
    """True if the solid bounded by a closed, connected, manifold mesh is a handlebody."""
    if _genus(mesh) == 0:
        return True
    if tets is None:
        tets = _tetrahedralize(mesh)
    rng = np.random.default_rng(0)
    return any(_collapses_to_graph(tets, rng) for _ in range(TRIES))


# To verify that a mesh is orientable, there must exist a consistent winding order on the faces
def is_orientable(mesh) -> bool:
    return mesh.is_winding_consistent


# To verify that a mesh is connected, it must consist of exactly 1 connected component
def is_connected(mesh) -> bool:
    return len(mesh.split()) == 1


# To verify that a mesh is vertex-manifold (has no singular vertices), the link of each vertex must be
# a single cycle, or a single path on a boundary. The link of v has an edge {a, b} for every face (v, a, b),
# counted with multiplicity: one connected graph with every degree at most 2 is a path or a cycle, and it
# is a simple one exactly when it has one edge fewer than its nodes (path) or as many (cycle).
def is_vertex_manifold(mesh) -> bool:
    for v, fs in enumerate(mesh.vertex_faces):
        adj = defaultdict(list)
        for f in fs[fs != -1]:
            a, b = (i for i in mesh.faces[f] if i != v)
            adj[a].append(b)
            adj[b].append(a)
        if not adj or any(len(n) > 2 for n in adj.values()):
            return False
        edges = sum(map(len, adj.values())) // 2
        if edges not in (len(adj) - 1, len(adj)):
            return False
        seen, todo = {next(iter(adj))}, [next(iter(adj))]
        while todo:
            for n in adj[todo.pop()]:
                if n not in seen:
                    seen.add(n)
                    todo.append(n)
        if len(seen) != len(adj):
            return False
    return True


# To verify that a mesh is closed, each edge must be adjacent to exactly 2 faces
def is_closed(mesh) -> bool:
    return mesh.is_watertight


# To verify that a mesh is embedded, no two triangles that do not share a vertex or edge may intersect
def is_self_intersection_free(mesh) -> bool:
    """No two triangles that share no vertex intersect (MeshLab). Triangles folded flat onto a
    neighbour are caught later, when TetGen refuses to fill the mesh."""
    import pymeshlab

    ms = pymeshlab.MeshSet()
    ms.add_mesh(pymeshlab.Mesh(vertex_matrix=mesh.vertices, face_matrix=mesh.faces))
    ms.compute_selection_by_self_intersections_per_face()
    return ms.current_mesh().selected_face_number() == 0


# We consider a mesh to be valid if it is orientable, connected, vertex-manifold, edge-manifold, and closed,
# does not intersect itself, and the solid it bounds is confirmed to be a handlebody (see is_handlebody)
def is_valid(mesh) -> bool:
    orientable = is_orientable(mesh)
    connected = is_connected(mesh)
    vertex_manifold = is_vertex_manifold(mesh)
    closed = is_closed(mesh)

    if not orientable:
        print("The mesh is not orientable.")
    if not connected:
        print("The mesh is not connected.")
    if not vertex_manifold:
        print("The mesh is not vertex-manifold.")
    if not closed:
        print("The mesh is not closed.")
    if not (orientable and connected and vertex_manifold and closed):
        return False
    if not is_self_intersection_free(mesh):
        print("The mesh intersects itself.")
        return False

    # Only meaningful for a closed, connected, manifold surface, so checked last.
    try:
        tets = _tetrahedralize(mesh)
    except RuntimeError as error:
        print(f"The mesh intersects itself: {error}.")
        return False
    handlebody = is_handlebody(mesh, tets)
    if not handlebody:
        print("The mesh does not bound a handlebody.")
    return handlebody


def verify_dataset(base_path=DEFAULT_DATASET_PATH) -> None:
    base = Path(base_path)
    if not base.is_dir():
        raise FileNotFoundError(f"{base_path} is not a valid directory")

    valid = 0
    invalid = []

    for folder in base.iterdir():
        if not folder.is_dir():
            continue

        print(f"\n[INFO] Verifying directory: {folder}")

        for file_path in folder.iterdir():
            if not file_path.is_file() or file_path.suffix != ".obj":
                continue
            mesh = load_trimesh(file_path)
            if is_valid(mesh):
                valid += 1
            else:
                invalid.append(file_path)

    print(f"\nValid meshes:   {valid}")
    print(f"Invalid meshes: {len(invalid)}")
    if invalid:
        print("\nMeshes that failed validation:")
        for path in invalid:
            print(f"- {path}")


if __name__ == "__main__":
    verify_dataset()
