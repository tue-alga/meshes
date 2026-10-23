"""Mesh a CAD file (STEP/BREP/IGES/GEO) into a closed triangle mesh with the gmsh Python API.

Unlike step_to_obj.py (which uses an absolute element size), the element size here is relative
to the model's bounding-box diagonal, so it works for models in any unit. Faces are sewn, multiple
volumes are fused, and half-models (CFD geometry cut at a symmetry plane) can be mirrored.

Usage:  python tools/cad_to_obj.py <cad file> <out.obj> [--divisions 100] [--mirror]
Needs:  pip install gmsh trimesh numpy
"""

import argparse

import gmsh
import numpy as np
import trimesh
from trimesh.grouping import group_rows


def mesh_cad(path: str, divisions: float) -> trimesh.Trimesh:
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", 0)
    gmsh.option.setNumber("Geometry.OCCSewFaces", 1)
    gmsh.open(path)
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


def mirror_half_model(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    """Close a half-model whose open boundary lies on an axis-aligned symmetry plane."""
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
    parser.add_argument("cad")
    parser.add_argument("out")
    parser.add_argument("--divisions", type=float, default=100,
                        help="max element size = bounding-box diagonal / divisions (default: 100)")
    parser.add_argument("--mirror", action="store_true", help="mirror an open half-model across its symmetry plane")
    args = parser.parse_args()

    mesh = mesh_cad(args.cad, args.divisions)
    if args.mirror and not mesh.is_watertight:
        mesh = mirror_half_model(mesh)
    print(f"faces {len(mesh.faces)}  watertight {mesh.is_watertight}  bodies {mesh.body_count}")
    mesh.export(args.out)


if __name__ == "__main__":
    main()
