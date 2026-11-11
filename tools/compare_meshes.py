"""Describe how mesh B differs from mesh A: identical, rotated / scaled / moved, retriangulated,
or different geometry. Used to check dataset meshes against freshly downloaded originals.

The reported rotation, scale and translation map B onto A (A ~= s * R @ B + t).

Usage:  python tools/compare_meshes.py a.obj b.obj
Needs:  pip install trimesh numpy scipy
"""

import argparse
import itertools

import numpy as np
import trimesh
from scipy.spatial import cKDTree
from scipy.spatial.transform import Rotation

AXIS_ROTATIONS = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i, (p, s) in enumerate(zip(perm, signs)):
            R[i, p] = s
        AXIS_ROTATIONS.append(R)
PROPER = [R for R in AXIS_ROTATIONS if np.linalg.det(R) > 0]


def load(path) -> trimesh.Trimesh:
    m = trimesh.load(path, force="mesh", process=False)
    m = trimesh.Trimesh(m.vertices, m.faces, process=True)
    m.merge_vertices()
    return m


def umeyama(P, Q, fixed_scale=None):
    """Return s, R, t minimising |s R Q + t - P| (rows are points)."""
    mp, mq = P.mean(0), Q.mean(0)
    U, S, Vt = np.linalg.svd((P - mp).T @ (Q - mq) / len(P))
    D = np.eye(3)
    D[2, 2] = np.sign(np.linalg.det(U @ Vt))
    R = U @ D @ Vt
    s = fixed_scale if fixed_scale is not None else np.trace(np.diag(S) @ D) / ((Q - mq) ** 2).sum(1).mean()
    return s, R, mp - s * R @ mq


def describe(a: trimesh.Trimesh, b: trimesh.Trimesh) -> tuple[str, str]:
    va, vb = a.vertices, b.vertices
    diag = np.linalg.norm(np.ptp(va, 0))
    same_counts = len(va) == len(vb) and len(a.faces) == len(b.faces)
    if same_counts and np.abs(va[np.lexsort(va.T)] - vb[np.lexsort(vb.T)]).max() < 1e-6 * diag:
        return "unchanged", ""

    # rigid ICP on surface samples, started from every axis rotation; scale from the area ratio
    pa = trimesh.sample.sample_surface_even(a, 3000, seed=1)[0]
    pb = trimesh.sample.sample_surface_even(b, 3000, seed=2)[0]
    ta = cKDTree(pa)
    s = np.sqrt(a.area / b.area)
    best = None
    for R0 in PROPER:
        q = s * pb @ R0.T
        q += (va.min(0) + va.max(0)) / 2 - (np.ptp(q, 0) / 2 + q.min(0))
        for _ in range(30):
            _, idx = ta.query(q)
            _, R2, t2 = umeyama(pa[idx], q, fixed_scale=1.0)
            q = q @ R2.T + t2
        d = ta.query(q)[0].mean() / diag
        if best is None or d < best[0]:
            best = (d, umeyama(q, pb, fixed_scale=s))
    d, (s, R, t) = best
    d = (d + cKDTree(s * pb @ R.T + t).query(pa)[0].mean() / diag) / 2

    snapped = min(AXIS_ROTATIONS, key=lambda r: np.abs(r - R).max())
    if np.abs(snapped - R).max() < 0.03:
        R = snapped
    for nice in [1.0, 0.001, 1000.0, 0.01, 100.0, 0.1, 10.0, 0.0254, 1 / 0.0254]:
        if abs(s / nice - 1) < 0.01:
            s = nice
    exact = False
    if same_counts:
        tv = cKDTree(va)
        for _ in range(25):
            _, idx = tv.query(s * vb @ R.T + t)
            _, R, t = umeyama(va[idx], vb, fixed_scale=s)
        exact = tv.query(s * vb @ R.T + t)[0].max() / diag < 1e-5
        if exact:
            d = 0.0

    parts = []
    if not np.allclose(R, np.eye(3), atol=2e-3):
        ax = next((r for r in AXIS_ROTATIONS if np.allclose(R, r, atol=2e-3)), None)
        if ax is not None:
            parts.append("rotated (axis permutation " + str(ax.astype(int).tolist()).replace(" ", "") + ")")
        else:
            e = Rotation.from_matrix(R).as_euler("xyz", degrees=True).round(1)
            parts.append(f"rotated (xyz Euler {e[0]:g}°, {e[1]:g}°, {e[2]:g}°)")
    if abs(s - 1) > 2e-3:
        parts.append(f"scaled ×{s:.4g}")
    if np.linalg.norm(t) > 2e-3 * diag:
        parts.append("translated")
    if d > 1.2e-2:
        kind = "different geometry" if d > 3e-2 else "remeshed / repaired"
        parts.append(f"{kind} (mean surface distance {d:.2%} of diagonal)")
    elif not same_counts:
        parts.append(f"retriangulated ({len(va)} → {len(vb)} vertices)")
    elif not exact:
        parts.append("vertices moved slightly")
    return ("changed", "; ".join(parts)) if parts else ("unchanged", "vertex order only")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("a")
    parser.add_argument("b")
    args = parser.parse_args()
    status, detail = describe(load(args.a), load(args.b))
    print(status + (f": {detail}" if detail else ""))


if __name__ == "__main__":
    main()
