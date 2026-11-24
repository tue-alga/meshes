"""Regenerate README.md: the text in resources/tools/readme/intro.md, followed by the mesh tables and references
built from dataset/ and resources/tools/metadata/sources.csv.

Usage:  python resources/tools/readme/update_readme.py
"""

import contextlib
import io
import re
from pathlib import Path

from tables import PROJECT_ROOT, print_dataset

INTRO = Path(__file__).resolve().parent / "intro.md"


def main() -> None:
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        print_dataset()
    output = buffer.getvalue()
    tables, _, warnings = output.partition("\n[WARNING]")
    tables = tables.strip() + "\n"

    readme = PROJECT_ROOT / "README.md"
    total = len(re.findall(r"^\| <img", tables, flags=re.M))
    head = INTRO.read_text(encoding="utf-8").replace("{mesh_count}", str(total))
    readme.write_text(head + tables, encoding="utf-8", newline="\r\n")
    print(f"README.md updated: {total} meshes")
    if warnings:
        print("[WARNING]" + warnings.rstrip())


if __name__ == "__main__":
    main()
