import os

try:
    import trimesh
except ImportError:
    raise SystemExit(
        "Missing dependency: trimesh. Install it with: pip install trimesh"
    )


def rewrite_obj_without_header(obj_path):
    with open(obj_path, "r", encoding="utf-8") as fin:
        lines = fin.read().splitlines(True)

    if lines and lines[0].startswith("#"):
        with open(obj_path, "w", encoding="utf-8") as fout:
            fout.writelines(lines[1:])


def check_mesh(mesh, path):
    if len(mesh.split()) != 1:
        print(f"[WARN] {path} is not 1 connected component")
    if not mesh.is_watertight:
        print(f"[WARN] {path} is not watertight or orientable")


base_path = os.path.join(".", "dataset")

folders_scanned = 0
mesh_groups_found = 0
processed_from_obj = 0
processed_from_stl = 0
failed = 0

for upper in os.listdir(base_path):
    folder = os.path.join(base_path, upper)
    if not os.path.isdir(folder):
        continue

    folders_scanned += 1
    print(f"\n[INFO] Scanning folder {folders_scanned}: {folder}")

    stems = {}
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue

        stem, ext = os.path.splitext(name)
        ext = ext.lower()
        if ext not in {".obj", ".stl"}:
            continue

        if stem not in stems:
            stems[stem] = set()
        stems[stem].add(ext)

    mesh_groups_found += len(stems)
    total_in_folder = len(stems)

    for index, (stem, exts) in enumerate(stems.items(), start=1):
        print(f"[INFO]   [{index}/{total_in_folder}] Processing {stem}")

        obj_path = os.path.join(folder, stem + ".obj")
        stl_path = os.path.join(folder, stem + ".stl")

        try:
            if ".obj" in exts:
                mesh = trimesh.load(obj_path)
                check_mesh(mesh, obj_path)

                mesh.export(obj_path)
                rewrite_obj_without_header(obj_path)

                mesh.export(stl_path)

                processed_from_obj += 1
                print(f"[DONE]   Rewrote OBJ and regenerated STL for {stem}")

            elif ".stl" in exts:
                mesh = trimesh.load(stl_path)
                check_mesh(mesh, stl_path)

                mesh.export(obj_path)
                rewrite_obj_without_header(obj_path)

                mesh_from_obj = trimesh.load(obj_path)
                mesh_from_obj.export(stl_path)

                processed_from_stl += 1
                print(f"[DONE]   Generated OBJ and regenerated STL for {stem}")

        except Exception as exc:
            failed += 1
            print(f"[ERROR]  Failed processing {stem}: {exc}")

print("\n========== SUMMARY ==========")
print(f"Folders scanned:      {folders_scanned}")
print(f"Mesh groups found:    {mesh_groups_found}")
print(f"Processed from OBJ:   {processed_from_obj}")
print(f"Processed from STL:   {processed_from_stl}")
print(f"Failed:               {failed}")
print("Done.")
