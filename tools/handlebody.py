"""Check that the solid bounded by a mesh is a handlebody.

A handlebody (https://en.wikipedia.org/wiki/Handlebody) is a ball with solid handles attached: a thickened
graph. A closed surface of genus 0 always bounds a ball (Alexander), so it passes right away. A closed surface
of higher genus can bound something else, for example a block with a knotted tunnel through it.

The check fills the solid with tetrahedra and collapses it: a tetrahedron is removed through a triangle that
no other tetrahedron uses, then a triangle through an edge that no other triangle uses. If only edges remain,
the solid collapses onto a graph and is a handlebody. A greedy collapse can get stuck on a real handlebody,
so a few random orders are tried before a mesh fails.

Filling the solid: TetGen keeps the surface exactly, but fails on self-intersecting meshes (and sometimes
crashes), so it runs in a separate process. If it fails, fTetWild fills the solid approximately; that result
is only used when its boundary is still one surface of the same genus.

Needs:  pip install tetgen pytetwild
"""

import multiprocessing
import queue
from collections import deque

import numpy as np
import trimesh

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


def _boundary(vertices, tets) -> trimesh.Trimesh:
    faces, counts = np.unique(np.sort(tets[:, TET_FACES].reshape(-1, 3), axis=1), axis=0, return_counts=True)
    boundary = trimesh.Trimesh(vertices, faces[counts == 1], process=False)
    boundary.remove_unreferenced_vertices()
    return boundary


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
    import pytetwild

    for epsilon in (2e-4, 5e-5):
        v, tets = pytetwild.tetrahedralize(vertices, faces, edge_length_fac=0.02, epsilon=epsilon, num_opt_iter=10)
        boundary = _boundary(v, tets)
        if boundary.body_count == 1 and _genus(boundary) == _genus(mesh):
            return np.asarray(tets)
    raise RuntimeError("could not fill the mesh with tetrahedra without changing its topology")


def is_handlebody(mesh) -> bool:
    """True if the solid bounded by a closed, connected, manifold mesh is a handlebody."""
    if _genus(mesh) == 0:
        return True
    tets = _tetrahedralize(mesh)
    rng = np.random.default_rng(0)
    return any(_collapses_to_graph(tets, rng) for _ in range(TRIES))
