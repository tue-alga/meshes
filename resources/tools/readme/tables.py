"""Build the README's mesh tables and reference list from dataset/ and resources/tools/metadata/."""

import csv
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "preprocessing")]

from convert import DEFAULT_DATASET_PATH, DEFAULT_PREVIEW_PATH, PROJECT_ROOT, load_trimesh

DEFAULT_SOURCES_PATH = TOOLS / "metadata" / "sources.csv"


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


def print_dataset(
    base_path=DEFAULT_DATASET_PATH,
    sources_path=DEFAULT_SOURCES_PATH,
) -> None:
    base = Path(base_path)
    sources = load_sources(sources_path)

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

    # References are numbered by how many meshes use them
    ranked = sorted(ref_count, key=lambda k: (-ref_count[k], ref_order[k]))
    number = {k: i + 1 for i, k in enumerate(ranked)}
    print("<!-- sources -->")

    for folder, rows in tables:
        letter, name = folders[folder.name]
        genera = [r[1] for r in rows]
        g_label = "=0" if all(g == 0 for g in genera) else "≥1" if all(g >= 1 for g in genera) else "≥0"
        genus_label = {"=0": " genus 0", "≥1": " genus ≥ 1"}.get(g_label, "")
        print()
        print("<details>")
        # Bold instead of a heading: GitHub adds an anchor link to headings
        print(f"<summary><b>({letter}) {name.capitalize()}{genus_label} ({len(rows)} meshes)</b></summary>")
        print("<br>")  # space between the title and the table
        print()
        # GitHub shrinks images in wide tables; an unbreakable header keeps the thumbnail column wide enough
        spacer = "&nbsp;" * 17
        print(f"| {spacer} | model | genus | vertices | edges | triangles | source |")
        print("|-|-------|-------|----------|-------|-----------|--------|")
        for file_path, g, V, E, F, key, note in rows:
            preview_stem = (DEFAULT_PREVIEW_PATH / folder.name / file_path.stem).relative_to(PROJECT_ROOT).as_posix()
            thumb_cell = f'<img src="{preview_stem}.png" width="60"/>'
            # GitHub prefixes ids with user-content-; linking to that id opens the closed references
            source_cell = f'<a href="#user-content-ref-{number[key]}">[{number[key]}]</a> {note}'.strip() if key else ""
            print(
                f"| {thumb_cell} | [{file_path.stem}]({preview_stem}.stl) | {g} | {fmt(V)} | {fmt(E)} | {fmt(F)} "
                f"| {source_cell} |"
            )
        print()
        print("</details>")

    from metadata.citations import CITATIONS

    # Plain numbered entries: GitHub always moves footnotes out of collapsed sections
    print()
    print("---")
    print()
    print("<details>")
    print("<summary>References</summary>")
    print()
    entries = []  # sub + sup: 9px text, since sub alone (12px) is the size of GitHub footnotes
    for key in ranked:
        base_name, url = ref_info[key]
        citation = CITATIONS.get(url) or CITATIONS.get(base_name) or (f"{base_name}. <{url}>" if url else base_name)
        entries.append(f'<a id="ref-{number[key]}"></a><sub><sup>**[{number[key]}]** {citation}</sup></sub>')
    print("<br>\n".join(entries))
    print()
    print("</details>")

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
