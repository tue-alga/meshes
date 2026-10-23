import csv
import os
import tempfile
from collections import defaultdict
from pathlib import Path

try:
    import trimesh
except ImportError:
    raise SystemExit(
        "Missing dependency: trimesh. Install it with: pip install trimesh"
    )


SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

DEFAULT_DATASET_PATH = PROJECT_ROOT / "dataset"
DEFAULT_SOURCES_PATH = SCRIPT_DIR / "sources.csv"
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


def to_obj(path: str) -> str:
    assert os.path.isfile(path), f"{path} is not a file"

    path_excluding_extension, _ = os.path.splitext(path)

    mesh = load_trimesh(path)
    new_path = path_excluding_extension + ".obj"
    export_obj_safely(mesh, new_path)

    return new_path


# To verify that a mesh is orientable, there must exist a consistent winding order on the faces
def is_orientable(mesh) -> bool:
    return mesh.is_winding_consistent


# To verify that a mesh is connected, it must consist of exactly 1 connected component
def is_connected(mesh) -> bool:
    return len(mesh.split()) == 1


# To verify that a mesh is vertex-manifold, the link of each vertex must be a single path or cycle
def is_vertex_manifold(mesh) -> bool:
    for v, fs in enumerate(mesh.vertex_faces):
        adj = defaultdict(set)
        [
            adj[x].add(y) or adj[y].add(x)
            for f in fs[fs != -1]
            for x, y in [[i for i in mesh.faces[f] if i != v]]
        ]
        d = [*map(len, adj.values())]
        if any(i > 2 for i in d) or not (d.count(1) == 2 or all(i == 2 for i in d)):
            return False
    return True


# To verify that a mesh is closed, each edge must be adjacent to at least 2 faces
def is_closed(mesh) -> bool:
    return mesh.is_watertight


def check_mesh(mesh, path: str) -> None:
    if len(mesh.split()) != 1:
        print(
            f"[WARNING] Mesh '{path}' does not consist of exactly one connected component."
        )
    if not mesh.is_watertight:
        print(f"[WARNING] Mesh '{path}' is not watertight or orientable.")


# We consider a mesh to be valid if it is orientable, connected, vertex-manifold, edge-manifold, and closed
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

    return orientable and connected and vertex_manifold and closed


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


def load_sources(csv_path=DEFAULT_SOURCES_PATH) -> dict[str, tuple[str, str]]:
    path = Path(csv_path)

    if not path.is_file():
        raise FileNotFoundError(f"{csv_path} is not a valid file")

    sources = {}

    with open(path, "r", encoding="utf-8", newline="") as fin:
        reader = csv.DictReader(fin)

        required_columns = {"name", "source", "url"}
        if reader.fieldnames is None or not required_columns.issubset(
            reader.fieldnames
        ):
            raise ValueError(f"{csv_path} must contain the columns: name, source, url")

        for row in reader:
            name = row["name"].strip()
            source = row["source"].strip()
            url = row["url"].strip()

            if not name:
                continue

            sources[name] = (source, url)

    return sources


def fmt(n):
    return f"{n:,}".replace(",", ".")


DEFAULT_NEW_PATH = SCRIPT_DIR / "new_meshes.txt"
NEW_BADGE = '<img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/>'
DEFAULT_PROCESSOR = "Maxim Snoep"
# per-object URLs that belong to one collection (reference) in the README
COLLECTION_URLS = {
    "https://github.com/odedstein/meshes/": "https://github.com/odedstein/meshes",
    "https://ten-thousand-models.appspot.com/": "https://ten-thousand-models.appspot.com",
    "https://github.com/nasa/NASA-3D-Resources/": "https://github.com/nasa/NASA-3D-Resources",
}


def collection_url(url: str) -> str:
    for prefix, collection in COLLECTION_URLS.items():
        if url.startswith(prefix):
            return collection
    return url


# archives that copies of older models were obtained from
ARCHIVE_URLS = {
    "Alec Jacobson": "https://github.com/alecjacobson/common-3d-test-models",
    "Oded Stein": "https://github.com/odedstein/meshes",
    "Keenan Crane": "https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/",
    "Princeton": "https://gfx.cs.princeton.edu/proj/sugcon/models/",
}


def split_source(source: str) -> tuple[str, str]:
    """'Origin + Archive + Person (tag, tag)' -> (origin, note such as '(via Archive; simplified)' or '(meshed by X)').

    A later part without tags is an archive the mesh was obtained from."""
    base, *rest = source.split(" + ")
    notes = []
    for part in rest:
        person, _, tags = part.partition(" (")
        tags = tags.rstrip(")")
        if not tags:
            url = ARCHIVE_URLS.get(person)
            notes.append(f"via [{person}]({url})" if url else f"via {person}")
        elif person != DEFAULT_PROCESSOR:
            notes.append(f"{tags} by {person}")
        else:
            notes.append(tags)
    return base, f"({'; '.join(notes)})" if notes else ""


def load_new(path=DEFAULT_NEW_PATH) -> set[str]:
    path = Path(path)
    if not path.is_file():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def print_dataset(
    base_path=DEFAULT_DATASET_PATH,
    sources_path=DEFAULT_SOURCES_PATH,
) -> None:
    base = Path(base_path)
    sources = load_sources(sources_path)
    new_names = load_new()

    folders = {
        "a.smooth_zero": ("a", "smooth"),
        "b.smooth_plus": ("b", "smooth"),
        "c.sharp_zero": ("c", "sharp"),
        "d.sharp_plus": ("d", "sharp"),
        "e.nightmares": ("e", "nightmares"),
    }

    dataset_names = set()
    missing_sources = set()

    # first pass: geometry and the reference (collection) of every mesh
    tables = []
    ref_info: dict[str, tuple[str, str]] = {}
    ref_count: dict[str, int] = {}
    ref_order: dict[str, int] = {}
    for folder in sorted(base.iterdir()):
        if not folder.is_dir() or folder.name not in folders:
            continue
        files = sorted(
            (p for p in folder.iterdir() if p.is_file() and p.suffix == ".obj"),
            key=lambda p: p.stem.lower(),
        )
        rows = []
        for file_path in files:
            mesh = load_trimesh(file_path)
            V, E, F = len(mesh.vertices), len(mesh.edges_unique), len(mesh.faces)
            g = (2 - (V - E + F)) // 2
            dataset_names.add(file_path.stem)
            key, note = None, ""
            source_info = sources.get(file_path.stem)
            if source_info is None:
                missing_sources.add(file_path.stem)
            else:
                source_name, source_url = source_info
                base_name, note = split_source(source_name)
                key = collection_url(source_url) or base_name
                ref_info.setdefault(key, (base_name, key if source_url else ""))
                ref_count[key] = ref_count.get(key, 0) + 1
                ref_order.setdefault(key, len(ref_order))
            rows.append((file_path, g, V, E, F, key, note))
        if rows:
            tables.append((folder, rows))

    ranked = sorted(ref_order, key=ref_order.get)
    number = {k: i + 1 for i, k in enumerate(ranked)}

    for folder, rows in tables:
        letter, name = folders[folder.name]
        genera = [r[1] for r in rows]
        g_label = "=0" if all(g == 0 for g in genera) else "≥1" if all(g >= 1 for g in genera) else "≥0"
        print()
        print(f"### ({letter}) {name} (g{g_label}, n={len(rows)})")
        # GitHub shrinks images in wide tables; an unbreakable header keeps the thumbnail column wide enough
        spacer = "&nbsp;" * 17
        print(f"| {spacer} | model | genus | vertices | edges | triangles | source |")
        print("|-|-------|-------|----------|-------|-----------|--------|")
        for file_path, g, V, E, F, key, note in rows:
            preview_stem = (DEFAULT_PREVIEW_PATH / folder.name / file_path.stem).relative_to(PROJECT_ROOT).as_posix()
            thumb_cell = f'<img src="{preview_stem}.png" width="60"/>'
            source_cell = f"[^{number[key]}] {note}".strip() if key else ""
            badge = f" {NEW_BADGE}" if file_path.stem in new_names else ""
            print(
                f"| {thumb_cell} | [{file_path.stem}]({preview_stem}.stl){badge} | {g} | {fmt(V)} | {fmt(E)} | {fmt(F)} "
                f"| {source_cell} |"
            )

    from citations import CITATIONS

    print()
    # GitHub renders these as footnotes, numbered by first appearance, with links back to each model
    for key in ranked:
        base_name, url = ref_info[key]
        citation = CITATIONS.get(url) or CITATIONS.get(base_name) or (f"{base_name}. <{url}>" if url else base_name)
        print(f"[^{number[key]}]: {citation}")

    unused_sources = sorted(set(sources) - dataset_names)

    if missing_sources:
        print("\n[WARNING] Source metadata is missing for the following dataset files:")
        for name in sorted(missing_sources):
            print(f"[WARNING]   {name}")

    if unused_sources:
        print(
            "\n[WARNING] The following source metadata entries were not found in the dataset:"
        )
        for name in unused_sources:
            print(f"[WARNING]   {name}")


if __name__ == "__main__":
    normalize_dataset()
    verify_dataset()
    print_dataset()
