"""Render a small PNG thumbnail for every mesh in dataset/ into preview/.

Bouba meshes get smooth shading, kiki and nightmare meshes flat
shading. The camera is a Y-up dimetric orthographic view, and every mesh is
drawn in ALGO blue (#00a2de) with a dark outline.

The PNG has a transparent background.

Usage:  python tools/thumbnails.py [--size 160] [--force] [names ...]
Needs:  pip install pyvista pillow
"""

import argparse
from pathlib import Path

import numpy as np

try:
    import pyvista as pv
    from PIL import Image
except ImportError:
    raise SystemExit("Missing dependency: pip install pyvista pillow")

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATASET = PROJECT_ROOT / "dataset"
PREVIEW = PROJECT_ROOT / "preview"

ALGO = "#00a2de"
OUTLINE = "#004f6e"
SMOOTH_FOLDERS = {"a.bouba_zero", "b.bouba_plus"}
AZIMUTH, ELEVATION = 30.0, 20.0  # degrees; azimuth around +Y measured from +Z
SUPERSAMPLE = 3

pv.OFF_SCREEN = True


def render_thumbnail(obj_path: Path, png_path: Path, smooth: bool, size: int) -> None:
    mesh = pv.read(obj_path)

    plotter = pv.Plotter(off_screen=True, window_size=(size * SUPERSAMPLE, size * SUPERSAMPLE))
    plotter.set_background("white")
    plotter.add_mesh(mesh, color=ALGO, smooth_shading=smooth, specular=0.25,
                     specular_power=20, ambient=0.25, diffuse=0.8)
    plotter.add_silhouette(mesh, color=OUTLINE, line_width=SUPERSAMPLE + 1)
    plotter.enable_ssao(radius=mesh.length * 0.03, kernel_size=128)
    plotter.enable_anti_aliasing("ssaa")

    a, e = np.radians(AZIMUTH), np.radians(ELEVATION)
    direction = np.array([np.cos(e) * np.sin(a), np.sin(e), np.cos(e) * np.cos(a)])
    center = np.array(mesh.center)
    plotter.camera.focal_point = tuple(center)
    plotter.camera.position = tuple(center + direction * mesh.length * 2)
    plotter.camera.up = (0.0, 1.0, 0.0)
    plotter.enable_parallel_projection()
    plotter.reset_camera()
    plotter.camera.zoom(1.0)

    image = plotter.screenshot(transparent_background=True, return_img=True)
    plotter.close()

    png_path.parent.mkdir(parents=True, exist_ok=True)
    Image.fromarray(image).resize((size, size), Image.LANCZOS).save(png_path, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("names", nargs="*", help="only render these mesh names")
    parser.add_argument("--size", type=int, default=160, help="thumbnail size in pixels (default: 160)")
    parser.add_argument("--force", action="store_true", help="re-render existing thumbnails")
    args = parser.parse_args()

    obj_files = sorted(DATASET.glob("*/*.obj"))
    if args.names:
        obj_files = [p for p in obj_files if p.stem in set(args.names)]

    rendered = skipped = failed = 0
    for index, obj_path in enumerate(obj_files, start=1):
        folder = obj_path.parent.name
        png_path = PREVIEW / folder / f"{obj_path.stem}.png"
        if png_path.exists() and not args.force:
            skipped += 1
            continue
        try:
            render_thumbnail(obj_path, png_path, folder in SMOOTH_FOLDERS, args.size)
            rendered += 1
            print(f"[{index}/{len(obj_files)}] {folder}/{obj_path.stem}")
        except Exception as exc:
            failed += 1
            print(f"[ERROR] {obj_path}: {exc}")

    print(f"\nRendered: {rendered}  Skipped (exists): {skipped}  Failed: {failed}")


if __name__ == "__main__":
    main()
