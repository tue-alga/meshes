"""Load meshes and convert between OBJ, STL and CAD files.

Without arguments, this script normalizes the dataset: every mesh in dataset/ is rewritten as a
clean OBJ (an STL there becomes an OBJ), and its STL copy for GitHub's 3D viewer is written to
resources/preview/.

With a CAD file (STEP/BREP/IGES/GEO), it meshes it into a closed triangle mesh with gmsh. The
element size is relative to the model's bounding-box diagonal, so it works for models in any
unit. Faces are sewn, multiple volumes are fused, and half-models (CFD geometry cut at a
symmetry plane) can be mirrored.

Usage:  python resources/tools/preprocessing/convert.py
        python resources/tools/preprocessing/convert.py <cad file> <out.obj> [--divisions 100] [--mirror]
Needs:  pip install trimesh  (and gmsh numpy for CAD files)
"""

import argparse
import tempfile
from pathlib import Path

try:
    import trimesh
except ImportError:
    raise SystemExit(
        "Missing dependency: trimesh. Install it with: pip install trimesh"
    )


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DEFAULT_DATASET_PATH = PROJECT_ROOT / "dataset"
# STL copies (for GitHub's 3D viewer) and thumbnails live here, mirroring dataset/
DEFAULT_PREVIEW_PATH = PROJECT_ROOT / "resources" / "preview"


def rewrite_obj_without_header(obj_path: str) -> None:
    with open(obj_path, "r", encoding="utf-8") as fin:
        lines = fin.read().splitlines(True)

    filtered_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("v ") or stripped.startswith("f "):
            filtered_lines.append(line)

    with open(obj_path, "w", encoding="utf-8") as fout:
        fout.writelines(filtered_lines)


def load_trimesh(path: str | Path):
    path = Path(path)

    try:
        mesh = trimesh.load(path, force="mesh")
    except Exception:
        mesh = trimesh.load(path)

    if isinstance(mesh, trimesh.Scene):
        geometries = [
            g for g in mesh.geometry.values() if isinstance(g, trimesh.Trimesh)
        ]
        if geometries:
            mesh = trimesh.util.concatenate(geometries)
        else:
            vertices = []
            faces = []
            vertex_offset = 0

            for geometry in mesh.geometry.values():
                if hasattr(geometry, "vertices"):
                    current_vertices = geometry.vertices
                    if len(current_vertices) == 0:
                        continue

                    vertices.extend(current_vertices)

                    if hasattr(geometry, "faces") and len(geometry.faces) > 0:
                        faces.extend(geometry.faces + vertex_offset)

                    vertex_offset += len(current_vertices)

            if not vertices:
                raise ValueError(
                    f"Mesh file '{path}' does not contain any mesh geometry"
                )

            mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)

    if not isinstance(mesh, trimesh.Trimesh):
        raise TypeError(f"File '{path}' could not be loaded as a triangular mesh")

    return mesh


def export_obj_safely(mesh, obj_path: str | Path) -> None:
    obj_path = Path(obj_path)
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".obj", delete=False, dir=obj_path.parent, encoding="utf-8"
    ) as tmp:
        temp_path = Path(tmp.name)

    try:
        mesh.export(temp_path)
        rewrite_obj_without_header(str(temp_path))
        temp_path.replace(obj_path)
    finally:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)


def export_stl_safely(mesh, stl_path: str | Path) -> None:
    stl_path = Path(stl_path)
    with tempfile.NamedTemporaryFile(
        suffix=".stl", delete=False, dir=stl_path.parent
    ) as tmp:
        temp_path = Path(tmp.name)

    try:
        mesh.export(temp_path)
        temp_path.replace(stl_path)
    finally:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)


def check_mesh(mesh, path: str) -> None:
    if len(mesh.split()) != 1:
        print(
            f"[WARNING] Mesh '{path}' does not consist of exactly one connected component."
        )
    if not mesh.is_watertight:
        print(f"[WARNING] Mesh '{path}' is not watertight or orientable.")


def normalize_dataset(
    base_path=DEFAULT_DATASET_PATH, preview_path=DEFAULT_PREVIEW_PATH
) -> None:
    base = Path(base_path)
    preview = Path(preview_path)

    if not base.is_dir():
        raise FileNotFoundError(f"{base_path} is not a valid directory")

    folders_scanned = 0
    mesh_groups_found = 0
    processed_from_obj = 0
    processed_from_stl = 0
    failed = 0

    for folder in base.iterdir():
        if not folder.is_dir():
            continue

        folders_scanned += 1
        print(f"\n[INFO] Scanning directory {folders_scanned}: {folder}")

        stems = {}
        for file_path in folder.iterdir():
            if not file_path.is_file():
                continue

            stem = file_path.stem
            ext = file_path.suffix.lower()
            if ext not in {".obj", ".stl"}:
                continue

            if stem not in stems:
                stems[stem] = set()
            stems[stem].add(ext)

        mesh_groups_found += len(stems)
        total_in_folder = len(stems)

        for index, (stem, exts) in enumerate(stems.items(), start=1):
            print(f"[INFO]   [{index}/{total_in_folder}] Processing mesh '{stem}'.")

            obj_path = folder / f"{stem}.obj"
            legacy_stl_path = folder / f"{stem}.stl"
            stl_path = preview / folder.name / f"{stem}.stl"
            stl_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                if ".obj" in exts:
                    mesh = load_trimesh(obj_path)
                    check_mesh(mesh, str(obj_path))

                    export_obj_safely(mesh, obj_path)
                    export_stl_safely(mesh, stl_path)
                    legacy_stl_path.unlink(missing_ok=True)

                    processed_from_obj += 1
                    print(
                        f"[INFO]   Updated the OBJ file and regenerated the STL file for mesh '{stem}'."
                    )

                elif ".stl" in exts:
                    mesh = load_trimesh(legacy_stl_path)
                    check_mesh(mesh, str(legacy_stl_path))

                    export_obj_safely(mesh, obj_path)
                    export_stl_safely(mesh, stl_path)
                    legacy_stl_path.unlink(missing_ok=True)

                    processed_from_stl += 1
                    print(
                        f"[INFO]   Created the OBJ file and regenerated the STL file for mesh '{stem}'."
                    )

            except Exception as exc:
                failed += 1
                print(f"[ERROR]  Failed to process mesh '{stem}': {exc}")

    print("\n========== SUMMARY ==========")
    print(f"Directories scanned:  {folders_scanned}")
    print(f"Mesh groups found:    {mesh_groups_found}")
    print(f"Processed from OBJ:   {processed_from_obj}")
    print(f"Processed from STL:   {processed_from_stl}")
    print(f"Failed:               {failed}")
    print("Normalization completed.")


def mesh_cad(path: str | Path, divisions: float = 100):
    """Mesh a CAD file with gmsh; the max element size is the bounding-box diagonal / divisions."""
    import gmsh
    import numpy as np

    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    gmsh.option.setNumber("Geometry.OCCSewFaces", 1)
    gmsh.open(str(path))
    volumes = gmsh.model.getEntities(3)
    if len(volumes) > 1:
        gmsh.model.occ.fuse([volumes[0]], volumes[1:])
        gmsh.model.occ.synchronize()
    x0, y0, z0, x1, y1, z1 = gmsh.model.getBoundingBox(-1, -1)
    diag = float(np.linalg.norm([x1 - x0, y1 - y0, z1 - z0]))
    gmsh.option.setNumber("Mesh.MeshSizeMax", diag / divisions)
    gmsh.option.setNumber("Mesh.MeshSizeMin", diag / divisions / 20)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 16)
    gmsh.model.mesh.generate(2)

    tags, coords, _ = gmsh.model.mesh.getNodes()
    index = {t: i for i, t in enumerate(tags)}
    faces = []
    for dim, tag in gmsh.model.getEntities(2):
        types, _, nodes = gmsh.model.mesh.getElements(dim, tag)
        for t, n in zip(types, nodes):
            if t == 2:  # 3-node triangle
                faces.append(np.vectorize(index.get)(n.reshape(-1, 3)))
    gmsh.finalize()

    mesh = trimesh.Trimesh(coords.reshape(-1, 3), np.vstack(faces), process=True)
    mesh.merge_vertices(digits_vertex=int(-np.log10(diag * 1e-7)))
    return mesh


def mirror_half_model(mesh):
    """Close a half-model whose open boundary lies on an axis-aligned symmetry plane."""
    import numpy as np
    from trimesh.grouping import group_rows

    diag = mesh.scale
    boundary = np.unique(mesh.edges_sorted[group_rows(mesh.edges_sorted, require_count=1)])
    if not len(boundary):
        return mesh
    spread = np.ptp(mesh.vertices[boundary], axis=0)
    axis = int(np.argmin(spread))
    if spread[axis] > diag * 1e-4:
        raise ValueError("open boundary is not on an axis-aligned plane; cannot mirror")
    c = float(np.median(mesh.vertices[boundary, axis]))
    half = mesh.vertices.copy()
    half[boundary, axis] = c
    mirrored = half.copy()
    mirrored[:, axis] = 2 * c - mirrored[:, axis]
    full = trimesh.util.concatenate([trimesh.Trimesh(half, mesh.faces, process=False),
                                     trimesh.Trimesh(mirrored, mesh.faces[:, ::-1], process=False)])
    full.merge_vertices(digits_vertex=int(-np.log10(diag * 1e-6)))
    return full


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("cad", nargs="?", help="CAD file to mesh (omit to normalize the dataset)")
    parser.add_argument("out", nargs="?", help="output OBJ for the CAD mesh")
    parser.add_argument("--divisions", type=float, default=100,
                        help="max element size = bounding-box diagonal / divisions (default: 100)")
    parser.add_argument("--mirror", action="store_true", help="mirror an open half-model across its symmetry plane")
    args = parser.parse_args()

    if args.cad is None:
        normalize_dataset()
        return
    if args.out is None:
        parser.error("give an output OBJ path after the CAD file")
    mesh = mesh_cad(args.cad, args.divisions)
    if args.mirror and not mesh.is_watertight:
        mesh = mirror_half_model(mesh)
    print(f"faces {len(mesh.faces)}  watertight {mesh.is_watertight}  bodies {mesh.body_count}")
    export_obj_safely(mesh, args.out)


if __name__ == "__main__":
    main()
