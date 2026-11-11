"""Repair, decimate or remesh a triangle mesh.

  remesh    feature-preserving isotropic remeshing (MeshLab). Sharp edges above
            --feature-angle degrees are kept. --edge is the target edge length as a
            fraction of the bounding-box diagonal (e.g. 0.02).
  decimate  quadric edge-collapse simplification to --faces triangles.
  repair    close small holes, remove small components and fix non-manifold parts
            (MeshFix). Refuses surfaces with many open edges unless --force.

Usage:  python tools/remesh.py remesh   in.obj out.obj [--edge 0.02] [--feature-angle 30]
        python tools/remesh.py decimate in.obj out.obj [--faces 60000]
        python tools/remesh.py repair   in.obj out.obj [--force]
Needs:  pip install trimesh numpy pymeshlab fast-simplification pymeshfix
"""

import argparse

import numpy as np
import trimesh
from trimesh.grouping import group_rows


def clean(mesh: trimesh.Trimesh) -> trimesh.Trimesh:
    mesh = trimesh.Trimesh(mesh.vertices, mesh.faces, process=True)
    mesh.merge_vertices(merge_tex=True, merge_norm=True)
    mesh.update_faces(mesh.nondegenerate_faces())
    mesh.update_faces(mesh.unique_faces())
    mesh.remove_unreferenced_vertices()
    return mesh


def remesh(mesh, edge=0.02, feature_angle=30.0, iterations=20):
    import pymeshlab
    ms = pymeshlab.MeshSet()
    ms.add_mesh(pymeshlab.Mesh(mesh.vertices, mesh.faces))
    ms.meshing_isotropic_explicit_remeshing(
        iterations=iterations, targetlen=pymeshlab.PercentageValue(edge * 100), featuredeg=feature_angle,
        checksurfdist=True, maxsurfdist=pymeshlab.PercentageValue(0.2), reprojectflag=True, smoothflag=True)
    r = ms.current_mesh()
    return clean(trimesh.Trimesh(r.vertex_matrix(), r.face_matrix()))


def decimate(mesh, faces=60_000):
    import fast_simplification
    if len(mesh.faces) <= faces:
        return mesh
    v, f = fast_simplification.simplify(np.asarray(mesh.vertices, np.float32),
                                        np.asarray(mesh.faces, np.int32), 1 - faces / len(mesh.faces))
    return clean(trimesh.Trimesh(v, f))


def boundary_fraction(mesh) -> float:
    return len(group_rows(mesh.edges_sorted, require_count=1)) / max(len(mesh.edges_unique), 1)


def repair(mesh, force=False):
    import pymeshfix
    if not force and boundary_fraction(mesh) > 0.005:
        raise SystemExit(f"{boundary_fraction(mesh):.1%} of edges are open; this looks like an open surface. "
                         "Use --force to close it anyway.")
    mf = pymeshfix.MeshFix(np.asarray(mesh.vertices, float), np.asarray(mesh.faces, np.int32))
    mf.repair(joincomp=True, remove_smallest_components=True)
    return clean(trimesh.Trimesh(mf.points, mf.faces))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("mode", choices=["remesh", "decimate", "repair"])
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--edge", type=float, default=0.02)
    parser.add_argument("--feature-angle", type=float, default=30.0)
    parser.add_argument("--faces", type=int, default=60_000)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    mesh = clean(trimesh.load(args.input, force="mesh"))
    if args.mode == "remesh":
        mesh = remesh(mesh, args.edge, args.feature_angle)
    elif args.mode == "decimate":
        mesh = decimate(mesh, args.faces)
    else:
        mesh = repair(mesh, args.force)
    if not mesh.is_winding_consistent:
        trimesh.repair.fix_winding(mesh)
    if mesh.is_watertight and mesh.volume < 0:
        mesh.invert()
    genus = (2 - mesh.euler_number) // 2
    print(f"faces {len(mesh.faces)}  watertight {mesh.is_watertight}  bodies {mesh.body_count}  genus {genus}")
    mesh.export(args.output)


if __name__ == "__main__":
    main()
