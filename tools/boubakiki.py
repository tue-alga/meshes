"""Measure how bouba (smooth/organic) or kiki (CAD/mechanical) each mesh is.

Per mesh it computes three scale- and (mostly) tessellation-independent features:

  planar       fraction of the surface area covered by planar patches (groups of coplanar
               adjacent faces, each at least 0.1% of the total area)
  developable  fraction of the surface area around vertices with ~zero Gaussian curvature
               (angle defect normalised by vertex area and total area)
  sharp        total length of edges with a dihedral angle above 30 degrees,
               divided by sqrt(total area)

and combines them into a kikiness score in [0, 1] with a logistic regression fitted on the
current bouba/kiki folder labels (nightmares are scored but not used for fitting). It reports
the cross-validated accuracy and lists the meshes whose geometry disagrees with their folder.

Usage:  python tools/boubakiki.py [--csv out.csv]
Needs:  pip install trimesh numpy scipy
"""

import argparse
import csv
from pathlib import Path

import numpy as np
import trimesh

ROOT = Path(__file__).resolve().parent.parent
LABEL = {"a.bouba_zero": 0, "b.bouba_plus": 0, "c.kiki_zero": 1, "d.kiki_plus": 1}


def features(mesh: trimesh.Trimesh) -> dict:
    area = mesh.area
    # planar patches
    facets_area = mesh.facets_area if len(mesh.facets) else np.zeros(0)
    planar = facets_area[facets_area > 1e-3 * area].sum() / area
    # developable: vertices with near-zero normalised Gaussian curvature
    defect = 2 * np.pi - np.bincount(mesh.faces.ravel(), weights=mesh.face_angles.ravel(), minlength=len(mesh.vertices))
    vertex_area = np.bincount(mesh.faces.ravel(), weights=np.repeat(mesh.area_faces / 3, 3), minlength=len(mesh.vertices))
    k = np.abs(defect) / np.maximum(vertex_area, 1e-30) * area  # sphere: 4*pi everywhere
    developable = vertex_area[k < 0.5].sum() / area
    # sharp edges
    angles = mesh.face_adjacency_angles
    lengths = np.linalg.norm(np.diff(mesh.vertices[mesh.face_adjacency_edges], axis=1)[:, 0], axis=1)
    sharp = lengths[angles > np.radians(30)].sum() / np.sqrt(area)
    return dict(planar=float(planar), developable=float(developable), sharp=float(sharp))


def fit_logistic(X, y, l2=1e-2, iters=2000, lr=0.5):
    w = np.zeros(X.shape[1])
    b = 0.0
    for _ in range(iters):
        p = 1 / (1 + np.exp(-(X @ w + b)))
        w -= lr * (X.T @ (p - y) / len(y) + l2 * w)
        b -= lr * (p - y).mean()
    return w, b


def design(rows):
    return np.array([[r["planar"], r["developable"], np.log1p(r["sharp"])] for r in rows])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--csv", help="write per-mesh features and scores to this CSV file")
    args = parser.parse_args()

    rows = []
    for obj in sorted((ROOT / "dataset").glob("*/*.obj")):
        mesh = trimesh.load(obj, force="mesh")
        rows.append(dict(name=obj.stem, folder=obj.parent.name, **features(mesh)))

    train = [r for r in rows if r["folder"] in LABEL]
    X, y = design(train), np.array([LABEL[r["folder"]] for r in train], float)
    mu, sd = X.mean(0), X.std(0) + 1e-12
    Xn = (X - mu) / sd

    # 10-fold cross-validated predictions
    rng = np.random.default_rng(0)
    folds = rng.permutation(len(train)) % 10
    cv = np.zeros(len(train))
    for f in range(10):
        w, b = fit_logistic(Xn[folds != f], y[folds != f])
        cv[folds == f] = 1 / (1 + np.exp(-(Xn[folds == f] @ w + b)))
    acc = ((cv > 0.5) == y).mean()

    w, b = fit_logistic(Xn, y)
    for r in rows:
        x = (design([r])[0] - mu) / sd
        r["kikiness"] = float(1 / (1 + np.exp(-(x @ w + b))))
    for r, p in zip(train, cv):
        r["kikiness_cv"] = float(p)

    print(f"meshes: {len(rows)}  (bouba {int((y == 0).sum())}, kiki {int((y == 1).sum())})")
    print(f"10-fold cross-validated accuracy: {acc:.1%}")
    print("weights (standardised): planar {:.2f}, developable {:.2f}, log sharp {:.2f}".format(*w))
    print("\nIn bouba but looks kiki (cross-validated kikiness > 0.5):")
    for r in sorted((r for r in train if LABEL[r["folder"]] == 0 and r["kikiness_cv"] > 0.5), key=lambda r: -r["kikiness_cv"]):
        print(f"  {r['kikiness_cv']:.2f}  {r['name']:28} planar {r['planar']:.2f}  developable {r['developable']:.2f}  sharp {r['sharp']:.1f}")
    print("\nIn kiki but looks bouba (cross-validated kikiness < 0.5):")
    for r in sorted((r for r in train if LABEL[r["folder"]] == 1 and r["kikiness_cv"] < 0.5), key=lambda r: r["kikiness_cv"]):
        print(f"  {r['kikiness_cv']:.2f}  {r['name']:28} planar {r['planar']:.2f}  developable {r['developable']:.2f}  sharp {r['sharp']:.1f}")
    print("\nNightmares:")
    for r in sorted((r for r in rows if r["folder"] == "e.nightmares"), key=lambda r: r["kikiness"]):
        print(f"  {r['kikiness']:.2f}  {r['name']}")

    if args.csv:
        with open(args.csv, "w", newline="", encoding="utf-8") as f:
            w_ = csv.DictWriter(f, fieldnames=["name", "folder", "planar", "developable", "sharp", "kikiness", "kikiness_cv"])
            w_.writeheader()
            for r in rows:
                w_.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})


if __name__ == "__main__":
    main()
