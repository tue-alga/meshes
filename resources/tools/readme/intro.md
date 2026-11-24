<img src="resources/preview/header.png" alt="All meshes in the dataset" width="100%"/>

This repository contains a curated collection of {mesh_count} triangle meshes spanning a wide variety of shapes. All meshes are verified to be connected (a single component), closed (every edge is shared by exactly two triangles), orientable (the triangles can be oriented consistently), vertex-manifold (the triangles around each vertex form a single disk), embedded (free of self-intersections), and to bound a handlebody (a solid ball with handles attached). The dataset changes over time, so please cite the specific [tagged version](https://github.com/tue-alga/meshes/tags) you used. <b>The current version is v4.0.0</b>.

> 💡 **Tip:** GitHub has a built-in 3D model viewer. Click a category below to open it, then click any model name to preview it interactively in 3D.

The meshes are stored as `.obj` files in `dataset/`. The `resources/preview/` folder contains a thumbnail and `.stl` copy such that the models can be viewed using GitHub's built-in 3D viewer, and `resources/tools/` contains the scripts used to build and check the dataset. The collection is organized into five categories based on geometric character and topological complexity: (a) **smooth genus 0**, (b) **smooth genus ≥ 1**, (c) **sharp genus 0**, (d) **sharp genus ≥ 1**, and (e) **nightmares**. Here, *smooth* refers to organic or freeform shapes, *sharp* to CAD-like shapes with flat faces and sharp edges, and *nightmares* to very challenging shapes with unusual geometric or topological quirks.

