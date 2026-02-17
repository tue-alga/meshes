import trimesh
import os

base_path = os.path.join(".", "dataset")

for upper in os.listdir(base_path):
    folder = os.path.join(base_path, upper)
    for f in os.listdir(folder):
        path = os.path.join(folder, f)

        path_excluding_extension, extension = os.path.splitext(path)

        if extension == ".stl":
            mesh = trimesh.load(path)
            new_path = path_excluding_extension + ".obj"
            mesh.export(new_path)

            # remove trimesh marketing from .obj
            with open(new_path, 'r') as fin:
                data = fin.read().splitlines(True)
            with open(new_path, 'w') as fout:
                fout.writelines(data[1:])