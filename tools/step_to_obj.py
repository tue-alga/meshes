import argparse
import subprocess
from collections import defaultdict
from pathlib import Path

import trimesh

GMSH_CMD = r"C:\Users\snoep\Documents\gmsh-4.15.2-Windows64\gmsh.exe"
DEFAULT_REFINE_COUNT = 3
SCRIPT_DIR = Path(__file__).resolve().parent


def run_gmsh_command(args: list[str], error_context: str) -> None:
    result = subprocess.run(
        args,
        check=False,
        capture_output=True,
        text=True,
        creationflags=subprocess.CREATE_NO_WINDOW,
    )

    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip() or "Unknown Gmsh error"
        raise RuntimeError(f"{error_context}: {message}")


def run_gmsh(step_path: Path, stl_path: Path, refine_count: int) -> None:
    run_gmsh_command(
        [
            GMSH_CMD,
            str(step_path),
            "-2",
            "-format",
            "stl",
            "-o",
            str(stl_path),
        ],
        f"Gmsh surface meshing failed for '{step_path}'",
    )

    if not stl_path.is_file():
        raise RuntimeError(f"Gmsh did not produce the expected STL file: '{stl_path}'")

    for _ in range(refine_count):
        run_gmsh_command(
            [
                GMSH_CMD,
                str(stl_path),
                "-refine",
                "-format",
                "stl",
                "-o",
                str(stl_path),
                "-nopopup",
            ],
            f"Gmsh refinement failed for '{stl_path}'",
        )

        if not stl_path.is_file():
            raise RuntimeError(
                f"Gmsh did not produce the expected refined STL file: '{stl_path}'"
            )


def rewrite_obj_without_header(obj_path: Path) -> None:
    with open(obj_path, "r", encoding="utf-8") as fin:
        lines = fin.read().splitlines(True)

    filtered_lines = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("v ") or stripped.startswith("f "):
            filtered_lines.append(line)

    with open(obj_path, "w", encoding="utf-8") as fout:
        fout.writelines(filtered_lines)


def stl_to_obj(stl_path: Path, obj_path: Path) -> None:
    mesh = trimesh.load_mesh(stl_path)

    if isinstance(mesh, trimesh.Scene):
        geometries = [
            g for g in mesh.geometry.values() if isinstance(g, trimesh.Trimesh)
        ]
        if not geometries:
            raise RuntimeError(
                f"STL file '{stl_path}' does not contain any mesh geometry"
            )
        mesh = trimesh.util.concatenate(geometries)

    if not isinstance(mesh, trimesh.Trimesh):
        raise RuntimeError(
            f"STL file '{stl_path}' could not be loaded as a triangular mesh"
        )

    mesh.export(obj_path)
    rewrite_obj_without_header(obj_path)


def step_to_obj(step_path: Path, refine_count: int) -> Path:
    if step_path.suffix.lower() not in {".step", ".stp"}:
        raise ValueError(f"Unsupported file type: '{step_path}'")

    obj_path = step_path.with_suffix(".obj")
    stl_path = step_path.with_suffix(".stl")

    run_gmsh(step_path, stl_path, refine_count)
    stl_to_obj(stl_path, obj_path)

    return obj_path


def is_orientable(mesh) -> bool:
    return mesh.is_winding_consistent


def is_connected(mesh) -> bool:
    return len(mesh.split()) == 1


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


def is_closed(mesh) -> bool:
    return mesh.is_watertight


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


def verify_obj_directory(directory: Path) -> None:
    obj_files = sorted(
        [
            path
            for path in directory.iterdir()
            if path.is_file() and path.suffix.lower() == ".obj"
        ]
    )

    if not obj_files:
        print(f"No OBJ files found in '{directory}'.")
        return

    print()
    print(f"Verifying {len(obj_files)} OBJ file(s) in '{directory}'...")

    valid = 0
    invalid = []

    for obj_path in obj_files:
        try:
            mesh = trimesh.load_mesh(obj_path)
            if isinstance(mesh, trimesh.Scene):
                geometries = [
                    g for g in mesh.geometry.values() if isinstance(g, trimesh.Trimesh)
                ]
                if not geometries:
                    raise RuntimeError(
                        f"OBJ file '{obj_path}' does not contain any mesh geometry"
                    )
                mesh = trimesh.util.concatenate(geometries)

            if not isinstance(mesh, trimesh.Trimesh):
                raise RuntimeError(
                    f"OBJ file '{obj_path}' could not be loaded as a triangular mesh"
                )

            if is_valid(mesh):
                valid += 1
            else:
                invalid.append(obj_path)
        except Exception as exc:
            invalid.append(obj_path)
            print(f"[ERROR]  Failed to validate '{obj_path.name}': {exc}")

    print()
    print("Validation summary")
    print("------------------")
    print(f"Valid:   {valid}")
    print(f"Invalid: {len(invalid)}")

    if invalid:
        print("Invalid OBJ files:")
        for path in invalid:
            print(f"- {path.name}")


def convert_directory(directory: Path, refine_count: int) -> None:
    step_files = sorted(
        [
            path
            for path in directory.iterdir()
            if path.is_file() and path.suffix.lower() in {".step", ".stp"}
        ]
    )

    if not step_files:
        print(f"No STEP files found in '{directory}'.")
        return

    print(f"Found {len(step_files)} STEP file(s) in '{directory}'.")

    converted = 0
    failed = 0

    for index, step_path in enumerate(step_files, start=1):
        print(f"[{index}/{len(step_files)}] Converting '{step_path.name}'...")
        try:
            obj_path = step_to_obj(step_path, refine_count)
            converted += 1
            print(f"  Wrote '{obj_path.name}'.")
        except Exception as exc:
            failed += 1
            print(f"  Failed: {exc}")

    print()
    print("Conversion summary")
    print("------------------")
    print(f"Converted: {converted}")
    print(f"Failed:    {failed}")


def run_parser_validation(directory: Path) -> None:
    verify_obj_directory(directory)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert STEP files to OBJ by meshing them with Gmsh as a 2D surface mesh "
            "and refining the mesh a configurable number of times."
        )
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="temp",
        help="STEP file or directory to process (default: temp)",
    )
    parser.add_argument(
        "--refine",
        type=int,
        default=DEFAULT_REFINE_COUNT,
        help=f"Number of Gmsh refinement passes (default: {DEFAULT_REFINE_COUNT})",
    )
    return parser.parse_args()


def main() -> None:
    if not Path(GMSH_CMD).is_file():
        raise SystemExit(f"Gmsh executable was not found: '{GMSH_CMD}'")

    args = parse_args()
    path = Path(args.path).resolve()

    if args.refine < 0:
        raise SystemExit("--refine must be non-negative")

    if path.is_file():
        obj_path = step_to_obj(path, args.refine)
        print(f"Wrote '{obj_path}'.")
        run_parser_validation(path.parent)
    elif path.is_dir():
        convert_directory(path, args.refine)
        run_parser_validation(path)
    else:
        raise SystemExit(f"Path does not exist: '{path}'")


if __name__ == "__main__":
    main()
