"""Load meshes and convert between OBJ and STL.

Running this script normalizes the dataset: every mesh in dataset/ is rewritten as a clean OBJ
(an STL there becomes an OBJ), and its STL copy for GitHub's 3D viewer is written to preview/.

Usage:  python tools/preprocessing/convert.py
Needs:  pip install trimesh
"""

import tempfile
from pathlib import Path

try:
    import trimesh
except ImportError:
    raise SystemExit(
        "Missing dependency: trimesh. Install it with: pip install trimesh"
    )


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_DATASET_PATH = PROJECT_ROOT / "dataset"
# STL copies (for GitHub's 3D viewer) and thumbnails live here, mirroring dataset/
DEFAULT_PREVIEW_PATH = PROJECT_ROOT / "preview"


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


if __name__ == "__main__":
    normalize_dataset()
