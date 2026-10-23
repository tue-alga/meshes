"""Regenerate the mesh tables in README.md (everything from the first '### (a)' heading to the end)
from dataset/ and tools/sources.csv, and update the mesh count in the first paragraph.

With --preview, also write temp/README_preview.html (GitHub-like rendering, needs `pip install markdown`);
serve the repository root (python -m http.server) and open /temp/README_preview.html to see thumbnails.

Usage:  python tools/update_readme.py [--preview]
"""

import argparse
import contextlib
import io
import re
from pathlib import Path

from parser import PROJECT_ROOT, print_dataset

CSS = """body{font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;max-width:1012px;margin:32px auto;padding:0 16px;
color:#1f2328;background:#fff;line-height:1.5;font-size:14px}table{border-collapse:collapse;margin:16px 0}
th,td{border:1px solid #d1d9e0;padding:4px 10px}tr:nth-child(2n){background:#f6f8fa}td img{display:block}
h3{border-bottom:1px solid #d1d9e0;padding-bottom:.3em;margin-top:32px}a{color:#0969da;text-decoration:none}
code{background:#eff1f3;padding:.1em .3em;border-radius:4px}blockquote{border-left:.25em solid #d1d9e0;color:#59636e;margin:0;padding:0 1em}"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--preview", action="store_true")
    args = parser.parse_args()

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        print_dataset()
    output = buffer.getvalue()
    tables, _, warnings = output.partition("\n[WARNING]")
    tables = tables.strip() + "\n"

    readme = PROJECT_ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    head = text[: text.index("### (a)")]
    total = len(re.findall(r"^\| <img", tables, flags=re.M))
    head = re.sub(r"collection of \d+ triangle meshes", f"collection of {total} triangle meshes", head)
    readme.write_text(head + tables, encoding="utf-8", newline="\r\n")
    print(f"README.md updated: {total} meshes")
    if warnings:
        print("[WARNING]" + warnings.rstrip())

    if args.preview:
        import markdown
        out = PROJECT_ROOT / "temp" / "README_preview.html"
        out.parent.mkdir(exist_ok=True)
        body = markdown.markdown(readme.read_text(encoding="utf-8"), extensions=["tables"])
        out.write_text(f'<!doctype html><meta charset=utf-8><base href="/"><title>README preview</title>'
                       f"<style>{CSS}</style>{body}", encoding="utf-8")
        print(f"Preview written to {out.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
