This repository contains a curated collection of 723 triangle meshes spanning a wide variety of shapes. All meshes are verified to be connected, watertight, orientable, and manifold. You can refer to a specific version of the dataset (e.g., in a publication) through the [releases](https://github.com/tue-alga/meshes/releases) page.

> 💡 **Tip:** GitHub has a built-in STL viewer. Click on any model name in the tables below to preview it interactively in 3D.

The meshes are stored as `.obj` files in `dataset/`. The `preview/` folder contains a thumbnail and `.stl` copy such that the models can be viewed using GitHub's built-in 3D viewer. The collection is organized into five categories based on geometric character and topological complexity: (a) **smooth genus 0**, (b) **smooth genus ≥ 1**, (c) **sharp genus 0**, (d) **sharp genus ≥ 1**, and (e) **nightmares**. Here, *smooth* refers to organic or freeform shapes, *sharp* to CAD-like shapes with flat faces and sharp edges, and *nightmares* to very challenging shapes with unusual geometric or topological quirks.

### (a) smooth (g=0, n=209)
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | model | genus | vertices | edges | triangles | source |
|-|-------|-------|----------|-------|-----------|--------|
| <img src="preview/a.smooth_zero/18_quadwild.png" width="120"/> | [18_quadwild](preview/a.smooth_zero/18_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 25.002 | 75.000 | 50.000 | [^1] (repaired) |
| <img src="preview/a.smooth_zero/40746_snoep.png" width="120"/> | [40746_snoep](preview/a.smooth_zero/40746_snoep.stl) | 0 | 1.698 | 5.088 | 3.392 | [^2] (re-oriented) |
| <img src="preview/a.smooth_zero/40746_thingi.png" width="120"/> | [40746_thingi](preview/a.smooth_zero/40746_thingi.stl) | 0 | 1.698 | 5.088 | 3.392 | [^2] |
| <img src="preview/a.smooth_zero/711_dente_skel.png" width="120"/> | [711_dente_skel](preview/a.smooth_zero/711_dente_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.337 | 28.005 | 18.670 | [^3] |
| <img src="preview/a.smooth_zero/aircraft_quadwild.png" width="120"/> | [aircraft_quadwild](preview/a.smooth_zero/aircraft_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 13.687 | 41.055 | 27.370 | [^1] (repaired) |
| <img src="preview/a.smooth_zero/airplane1_gao.png" width="120"/> | [airplane1_gao](preview/a.smooth_zero/airplane1_gao.stl) | 0 | 9.417 | 28.245 | 18.830 | [^4] |
| <img src="preview/a.smooth_zero/airplane2_gao.png" width="120"/> | [airplane2_gao](preview/a.smooth_zero/airplane2_gao.stl) | 0 | 26.806 | 80.412 | 53.608 | [^4] |
| <img src="preview/a.smooth_zero/among-us-crewmate_sketchfab.png" width="120"/> | [among-us-crewmate_sketchfab](preview/a.smooth_zero/among-us-crewmate_sketchfab.stl) | 0 | 964 | 2.886 | 1.924 | [^5] |
| <img src="preview/a.smooth_zero/among-us-crewmate_snoep.png" width="120"/> | [among-us-crewmate_snoep](preview/a.smooth_zero/among-us-crewmate_snoep.stl) | 0 | 3.061 | 9.177 | 6.118 | [^5] (remeshed) |
| <img src="preview/a.smooth_zero/Android_Figure_Panda_gso.png" width="120"/> | [Android_Figure_Panda_gso](preview/a.smooth_zero/Android_Figure_Panda_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 5.311 | 15.927 | 10.618 | [^6] |
| <img src="preview/a.smooth_zero/angel_quadwild.png" width="120"/> | [angel_quadwild](preview/a.smooth_zero/angel_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.468 | 13.398 | 8.932 | [^1] |
| <img src="preview/a.smooth_zero/armadillo_gao.png" width="120"/> | [armadillo_gao](preview/a.smooth_zero/armadillo_gao.stl) | 0 | 15.508 | 46.518 | 31.012 | [^4] |
| <img src="preview/a.smooth_zero/armadillo_jacobson.png" width="120"/> | [armadillo_jacobson](preview/a.smooth_zero/armadillo_jacobson.stl) | 0 | 49.990 | 149.964 | 99.976 | [^7] |
| <img src="preview/a.smooth_zero/armadillo_stein.png" width="120"/> | [armadillo_stein](preview/a.smooth_zero/armadillo_stein.stl) | 0 | 14.587 | 43.755 | 29.170 | [^8] |
| <img src="preview/a.smooth_zero/armchair_gao.png" width="120"/> | [armchair_gao](preview/a.smooth_zero/armchair_gao.stl) | 0 | 12.972 | 38.910 | 25.940 | [^4] |
| <img src="preview/a.smooth_zero/asiandragon_skel.png" width="120"/> | [asiandragon_skel](preview/a.smooth_zero/asiandragon_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 29.999 | 89.991 | 59.994 | [^3] (repaired, simplified) |
| <img src="preview/a.smooth_zero/ballJoint_skel.png" width="120"/> | [ballJoint_skel](preview/a.smooth_zero/ballJoint_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 137.062 | 411.180 | 274.120 | [^3] |
| <img src="preview/a.smooth_zero/bear0_quadwild.png" width="120"/> | [bear0_quadwild](preview/a.smooth_zero/bear0_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 5.018 | 15.048 | 10.032 | [^1] |
| <img src="preview/a.smooth_zero/bear1_quadwild.png" width="120"/> | [bear1_quadwild](preview/a.smooth_zero/bear1_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.290 | 12.864 | 8.576 | [^1] |
| <img src="preview/a.smooth_zero/bigguy_quadwild.png" width="120"/> | [bigguy_quadwild](preview/a.smooth_zero/bigguy_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 6.786 | 20.352 | 13.568 | [^1] |
| <img src="preview/a.smooth_zero/bimba_gao.png" width="120"/> | [bimba_gao](preview/a.smooth_zero/bimba_gao.stl) | 0 | 10.797 | 32.385 | 21.590 | [^4] |
| <img src="preview/a.smooth_zero/bimba_jacobson.png" width="120"/> | [bimba_jacobson](preview/a.smooth_zero/bimba_jacobson.stl) | 0 | 29.995 | 89.979 | 59.986 | [^7] (simplified) |
| <img src="preview/a.smooth_zero/bimba_loopy.png" width="120"/> | [bimba_loopy](preview/a.smooth_zero/bimba_loopy.stl) | 0 | 11.772 | 35.310 | 23.540 | [^9] |
| <img src="preview/a.smooth_zero/bird_gao.png" width="120"/> | [bird_gao](preview/a.smooth_zero/bird_gao.stl) | 0 | 17.318 | 51.948 | 34.632 | [^4] |
| <img src="preview/a.smooth_zero/blade_gao.png" width="120"/> | [blade_gao](preview/a.smooth_zero/blade_gao.stl) | 0 | 14.106 | 42.312 | 28.208 | [^4] |
| <img src="preview/a.smooth_zero/blade_loopy.png" width="120"/> | [blade_loopy](preview/a.smooth_zero/blade_loopy.stl) | 0 | 14.532 | 43.590 | 29.060 | [^9] |
| <img src="preview/a.smooth_zero/blub_crane.png" width="120"/> | [blub_crane](preview/a.smooth_zero/blub_crane.stl) | 0 | 7.106 | 21.312 | 14.208 | [^10] |
| <img src="preview/a.smooth_zero/bone1_loopy.png" width="120"/> | [bone1_loopy](preview/a.smooth_zero/bone1_loopy.stl) | 0 | 1.566 | 4.692 | 3.128 | [^9] |
| <img src="preview/a.smooth_zero/bone_femur_loopy.png" width="120"/> | [bone_femur_loopy](preview/a.smooth_zero/bone_femur_loopy.stl) | 0 | 4.666 | 13.992 | 9.328 | [^9] |
| <img src="preview/a.smooth_zero/bone_gao.png" width="120"/> | [bone_gao](preview/a.smooth_zero/bone_gao.stl) | 0 | 6.046 | 18.132 | 12.088 | [^4] |
| <img src="preview/a.smooth_zero/brain2_skel.png" width="120"/> | [brain2_skel](preview/a.smooth_zero/brain2_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 29.906 | 89.712 | 59.808 | [^3] (repaired, simplified) |
| <img src="preview/a.smooth_zero/brucewick_stein.png" width="120"/> | [brucewick_stein](preview/a.smooth_zero/brucewick_stein.stl) | 0 | 1.431 | 4.287 | 2.858 | [^8] |
| <img src="preview/a.smooth_zero/BU_polycut.png" width="120"/> | [BU_polycut](preview/a.smooth_zero/BU_polycut.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 30.002 | 90.000 | 60.000 | [^11] (simplified) |
| <img src="preview/a.smooth_zero/bumpy_sphere_gao.png" width="120"/> | [bumpy_sphere_gao](preview/a.smooth_zero/bumpy_sphere_gao.stl) | 0 | 22.890 | 68.664 | 45.776 | [^4] |
| <img src="preview/a.smooth_zero/bun_zipper_skel.png" width="120"/> | [bun_zipper_skel](preview/a.smooth_zero/bun_zipper_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 35.188 | 105.558 | 70.372 | [^3] (repaired) |
| <img src="preview/a.smooth_zero/bunny_alessia_quadwild.png" width="120"/> | [bunny_alessia_quadwild](preview/a.smooth_zero/bunny_alessia_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 1.077 | 3.225 | 2.150 | [^1] |
| <img src="preview/a.smooth_zero/bunny_gao.png" width="120"/> | [bunny_gao](preview/a.smooth_zero/bunny_gao.stl) | 0 | 11.247 | 33.735 | 22.490 | [^4] |
| <img src="preview/a.smooth_zero/bunny_loopy.png" width="120"/> | [bunny_loopy](preview/a.smooth_zero/bunny_loopy.stl) | 0 | 11.120 | 33.354 | 22.236 | [^9] |
| <img src="preview/a.smooth_zero/bunny_snoep.png" width="120"/> | [bunny_snoep](preview/a.smooth_zero/bunny_snoep.stl) | 0 | 11.120 | 33.354 | 22.236 | [^9] (re-oriented) |
| <img src="preview/a.smooth_zero/bunny_stein.png" width="120"/> | [bunny_stein](preview/a.smooth_zero/bunny_stein.stl) | 0 | 3.301 | 9.897 | 6.598 | [^8] |
| <img src="preview/a.smooth_zero/buste_gao.png" width="120"/> | [buste_gao](preview/a.smooth_zero/buste_gao.stl) | 0 | 17.341 | 52.017 | 34.678 | [^4] |
| <img src="preview/a.smooth_zero/buste_loopy.png" width="120"/> | [buste_loopy](preview/a.smooth_zero/buste_loopy.stl) | 0 | 6.070 | 18.204 | 12.136 | [^9] |
| <img src="preview/a.smooth_zero/buste_snoep.png" width="120"/> | [buste_snoep](preview/a.smooth_zero/buste_snoep.stl) | 0 | 6.070 | 18.204 | 12.136 | [^9] (re-oriented) |
| <img src="preview/a.smooth_zero/C0089_quadwild.png" width="120"/> | [C0089_quadwild](preview/a.smooth_zero/C0089_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 30.386 | 91.152 | 60.768 | [^1] |
| <img src="preview/a.smooth_zero/cactus_loopy.png" width="120"/> | [cactus_loopy](preview/a.smooth_zero/cactus_loopy.stl) | 0 | 700 | 2.094 | 1.396 | [^9] |
| <img src="preview/a.smooth_zero/camille_hand_gao.png" width="120"/> | [camille_hand_gao](preview/a.smooth_zero/camille_hand_gao.stl) | 0 | 16.565 | 49.689 | 33.126 | [^4] |
| <img src="preview/a.smooth_zero/camille_hand_loopy.png" width="120"/> | [camille_hand_loopy](preview/a.smooth_zero/camille_hand_loopy.stl) | 0 | 3.705 | 11.109 | 7.406 | [^9] |
| <img src="preview/a.smooth_zero/cat_loopy.png" width="120"/> | [cat_loopy](preview/a.smooth_zero/cat_loopy.stl) | 0 | 2.332 | 6.990 | 4.660 | [^9] |
| <img src="preview/a.smooth_zero/cat_stein.png" width="120"/> | [cat_stein](preview/a.smooth_zero/cat_stein.stl) | 0 | 7.949 | 23.841 | 15.894 | [^8] |
| <img src="preview/a.smooth_zero/cheese_stein.png" width="120"/> | [cheese_stein](preview/a.smooth_zero/cheese_stein.stl) | 0 | 30.002 | 90.000 | 60.000 | [^8] (simplified) |
| <img src="preview/a.smooth_zero/chicken_high_skel.png" width="120"/> | [chicken_high_skel](preview/a.smooth_zero/chicken_high_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 30.001 | 89.997 | 59.998 | [^3] (simplified) |
| <img src="preview/a.smooth_zero/chinese_lion_gao.png" width="120"/> | [chinese_lion_gao](preview/a.smooth_zero/chinese_lion_gao.stl) | 0 | 25.194 | 75.576 | 50.384 | [^4] |
| <img src="preview/a.smooth_zero/chinese_lion_loopy.png" width="120"/> | [chinese_lion_loopy](preview/a.smooth_zero/chinese_lion_loopy.stl) | 0 | 4.248 | 12.738 | 8.492 | [^9] |
| <img src="preview/a.smooth_zero/chinese_lion_snoep.png" width="120"/> | [chinese_lion_snoep](preview/a.smooth_zero/chinese_lion_snoep.stl) | 0 | 4.248 | 12.738 | 8.492 | [^9] (re-oriented) |
| <img src="preview/a.smooth_zero/CompletePart_16_gao.png" width="120"/> | [CompletePart_16_gao](preview/a.smooth_zero/CompletePart_16_gao.stl) | 0 | 3.840 | 11.514 | 7.676 | [^4] |
| <img src="preview/a.smooth_zero/CompletePart_63_gao.png" width="120"/> | [CompletePart_63_gao](preview/a.smooth_zero/CompletePart_63_gao.stl) | 0 | 3.840 | 11.514 | 7.676 | [^4] |
| <img src="preview/a.smooth_zero/constant-width_crane.png" width="120"/> | [constant-width_crane](preview/a.smooth_zero/constant-width_crane.stl) | 0 | 19.802 | 59.400 | 39.600 | [^10] |
| <img src="preview/a.smooth_zero/cow2_quadwild.png" width="120"/> | [cow2_quadwild](preview/a.smooth_zero/cow2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.315 | 12.939 | 8.626 | [^1] |
| <img src="preview/a.smooth_zero/david_gao.png" width="120"/> | [david_gao](preview/a.smooth_zero/david_gao.stl) | 0 | 25.434 | 76.296 | 50.864 | [^4] |
| <img src="preview/a.smooth_zero/deformed_armadillo_gao.png" width="120"/> | [deformed_armadillo_gao](preview/a.smooth_zero/deformed_armadillo_gao.stl) | 0 | 87.286 | 261.852 | 174.568 | [^4] |
| <img src="preview/a.smooth_zero/dente_gao.png" width="120"/> | [dente_gao](preview/a.smooth_zero/dente_gao.stl) | 0 | 12.195 | 36.579 | 24.386 | [^4] |
| <img src="preview/a.smooth_zero/dilo_gao.png" width="120"/> | [dilo_gao](preview/a.smooth_zero/dilo_gao.stl) | 0 | 22.154 | 66.456 | 44.304 | [^4] |
| <img src="preview/a.smooth_zero/dino0_quadwild.png" width="120"/> | [dino0_quadwild](preview/a.smooth_zero/dino0_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.514 | 13.536 | 9.024 | [^1] |
| <img src="preview/a.smooth_zero/dino1_quadwild.png" width="120"/> | [dino1_quadwild](preview/a.smooth_zero/dino1_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.058 | 27.168 | 18.112 | [^1] |
| <img src="preview/a.smooth_zero/dino2_gao.png" width="120"/> | [dino2_gao](preview/a.smooth_zero/dino2_gao.stl) | 0 | 10.178 | 30.528 | 20.352 | [^4] |
| <img src="preview/a.smooth_zero/dino_gao.png" width="120"/> | [dino_gao](preview/a.smooth_zero/dino_gao.stl) | 0 | 16.634 | 49.896 | 33.264 | [^4] |
| <img src="preview/a.smooth_zero/dog_loopy.png" width="120"/> | [dog_loopy](preview/a.smooth_zero/dog_loopy.stl) | 0 | 3.084 | 9.246 | 6.164 | [^9] |
| <img src="preview/a.smooth_zero/duck2_gao.png" width="120"/> | [duck2_gao](preview/a.smooth_zero/duck2_gao.stl) | 0 | 9.640 | 28.914 | 19.276 | [^4] |
| <img src="preview/a.smooth_zero/duck_gao.png" width="120"/> | [duck_gao](preview/a.smooth_zero/duck_gao.stl) | 0 | 3.598 | 10.788 | 7.192 | [^4] |
| <img src="preview/a.smooth_zero/ellipse_loopy.png" width="120"/> | [ellipse_loopy](preview/a.smooth_zero/ellipse_loopy.stl) | 0 | 554 | 1.656 | 1.104 | [^9] |
| <img src="preview/a.smooth_zero/eros_gao.png" width="120"/> | [eros_gao](preview/a.smooth_zero/eros_gao.stl) | 0 | 25.001 | 74.997 | 49.998 | [^4] |
| <img src="preview/a.smooth_zero/falconstatue_stein.png" width="120"/> | [falconstatue_stein](preview/a.smooth_zero/falconstatue_stein.stl) | 0 | 25.839 | 77.511 | 51.674 | [^8] |
| <img src="preview/a.smooth_zero/fish0_quadwild.png" width="120"/> | [fish0_quadwild](preview/a.smooth_zero/fish0_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 3.048 | 9.138 | 6.092 | [^1] |
| <img src="preview/a.smooth_zero/fish1_gao.png" width="120"/> | [fish1_gao](preview/a.smooth_zero/fish1_gao.stl) | 0 | 11.895 | 35.679 | 23.786 | [^4] |
| <img src="preview/a.smooth_zero/fish2_gao.png" width="120"/> | [fish2_gao](preview/a.smooth_zero/fish2_gao.stl) | 0 | 10.604 | 31.806 | 21.204 | [^4] |
| <img src="preview/a.smooth_zero/fish_stein.png" width="120"/> | [fish_stein](preview/a.smooth_zero/fish_stein.stl) | 0 | 10.786 | 32.352 | 21.568 | [^8] |
| <img src="preview/a.smooth_zero/foot_gao.png" width="120"/> | [foot_gao](preview/a.smooth_zero/foot_gao.stl) | 0 | 10.342 | 31.020 | 20.680 | [^4] |
| <img src="preview/a.smooth_zero/frog_skel.png" width="120"/> | [frog_skel](preview/a.smooth_zero/frog_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 37.225 | 111.669 | 74.446 | [^3] |
| <img src="preview/a.smooth_zero/gargoyle2_100K_quadwild.png" width="120"/> | [gargoyle2_100K_quadwild](preview/a.smooth_zero/gargoyle2_100K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 50.002 | 150.000 | 100.000 | [^1] |
| <img src="preview/a.smooth_zero/gargoyle_gao.png" width="120"/> | [gargoyle_gao](preview/a.smooth_zero/gargoyle_gao.stl) | 0 | 13.024 | 39.066 | 26.044 | [^4] |
| <img src="preview/a.smooth_zero/glass1_gao.png" width="120"/> | [glass1_gao](preview/a.smooth_zero/glass1_gao.stl) | 0 | 29.674 | 89.016 | 59.344 | [^4] |
| <img src="preview/a.smooth_zero/glass2_gao.png" width="120"/> | [glass2_gao](preview/a.smooth_zero/glass2_gao.stl) | 0 | 11.710 | 35.124 | 23.416 | [^4] |
| <img src="preview/a.smooth_zero/goathead_snoep.png" width="120"/> | [goathead_snoep](preview/a.smooth_zero/goathead_snoep.stl) | 0 | 2.763 | 8.283 | 5.522 | [^8] (re-oriented) |
| <img src="preview/a.smooth_zero/goathead_stein.png" width="120"/> | [goathead_stein](preview/a.smooth_zero/goathead_stein.stl) | 0 | 2.763 | 8.283 | 5.522 | [^8] |
| <img src="preview/a.smooth_zero/guy_quadwild.png" width="120"/> | [guy_quadwild](preview/a.smooth_zero/guy_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.474 | 28.416 | 18.944 | [^1] |
| <img src="preview/a.smooth_zero/hand_gao.png" width="120"/> | [hand_gao](preview/a.smooth_zero/hand_gao.stl) | 0 | 13.982 | 41.940 | 27.960 | [^4] |
| <img src="preview/a.smooth_zero/hand_loopy.png" width="120"/> | [hand_loopy](preview/a.smooth_zero/hand_loopy.stl) | 0 | 2.474 | 7.416 | 4.944 | [^9] |
| <img src="preview/a.smooth_zero/hand_stein.png" width="120"/> | [hand_stein](preview/a.smooth_zero/hand_stein.stl) | 0 | 7.993 | 23.973 | 15.982 | [^8] |
| <img src="preview/a.smooth_zero/head1_gao.png" width="120"/> | [head1_gao](preview/a.smooth_zero/head1_gao.stl) | 0 | 14.399 | 43.191 | 28.794 | [^4] |
| <img src="preview/a.smooth_zero/head2_gao.png" width="120"/> | [head2_gao](preview/a.smooth_zero/head2_gao.stl) | 0 | 14.754 | 44.256 | 29.504 | [^4] |
| <img src="preview/a.smooth_zero/hh_skel.png" width="120"/> | [hh_skel](preview/a.smooth_zero/hh_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 52.098 | 156.288 | 104.192 | [^3] (repaired) |
| <img src="preview/a.smooth_zero/hht_skel.png" width="120"/> | [hht_skel](preview/a.smooth_zero/hht_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 55.693 | 167.073 | 111.382 | [^3] (repaired) |
| <img src="preview/a.smooth_zero/hippo_skel.png" width="120"/> | [hippo_skel](preview/a.smooth_zero/hippo_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 39.548 | 118.638 | 79.092 | [^3] (repaired) |
| <img src="preview/a.smooth_zero/homer_gao.png" width="120"/> | [homer_gao](preview/a.smooth_zero/homer_gao.stl) | 0 | 13.639 | 40.911 | 27.274 | [^4] |
| <img src="preview/a.smooth_zero/horse_gao.png" width="120"/> | [horse_gao](preview/a.smooth_zero/horse_gao.stl) | 0 | 19.851 | 59.547 | 39.698 | [^4] |
| <img src="preview/a.smooth_zero/horse_jacobson.png" width="120"/> | [horse_jacobson](preview/a.smooth_zero/horse_jacobson.stl) | 0 | 48.485 | 145.449 | 96.966 | [^7] |
| <img src="preview/a.smooth_zero/human1_gao.png" width="120"/> | [human1_gao](preview/a.smooth_zero/human1_gao.stl) | 0 | 10.231 | 30.687 | 20.458 | [^4] |
| <img src="preview/a.smooth_zero/human2_gao.png" width="120"/> | [human2_gao](preview/a.smooth_zero/human2_gao.stl) | 0 | 12.794 | 38.376 | 25.584 | [^4] |
| <img src="preview/a.smooth_zero/human3_gao.png" width="120"/> | [human3_gao](preview/a.smooth_zero/human3_gao.stl) | 0 | 12.329 | 36.981 | 24.654 | [^4] |
| <img src="preview/a.smooth_zero/human_hand_skel.png" width="120"/> | [human_hand_skel](preview/a.smooth_zero/human_hand_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 52.345 | 157.029 | 104.686 | [^3] (repaired) |
| <img src="preview/a.smooth_zero/human_man_stein.png" width="120"/> | [human_man_stein](preview/a.smooth_zero/human_man_stein.stl) | 0 | 6.890 | 20.664 | 13.776 | [^8] |
| <img src="preview/a.smooth_zero/human_neutral_stein.png" width="120"/> | [human_neutral_stein](preview/a.smooth_zero/human_neutral_stein.stl) | 0 | 9.437 | 28.305 | 18.870 | [^8] (repaired) |
| <img src="preview/a.smooth_zero/human_woman_stein.png" width="120"/> | [human_woman_stein](preview/a.smooth_zero/human_woman_stein.stl) | 0 | 6.890 | 20.664 | 13.776 | [^8] |
| <img src="preview/a.smooth_zero/humerus_skel.png" width="120"/> | [humerus_skel](preview/a.smooth_zero/humerus_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 35.002 | 105.000 | 70.000 | [^3] |
| <img src="preview/a.smooth_zero/igea_gao.png" width="120"/> | [igea_gao](preview/a.smooth_zero/igea_gao.stl) | 0 | 25.282 | 75.840 | 50.560 | [^4] |
| <img src="preview/a.smooth_zero/igea_jacobson.png" width="120"/> | [igea_jacobson](preview/a.smooth_zero/igea_jacobson.stl) | 0 | 30.001 | 89.997 | 59.998 | [^7] (simplified) |
| <img src="preview/a.smooth_zero/inigo_crane.png" width="120"/> | [inigo_crane](preview/a.smooth_zero/inigo_crane.stl) | 0 | 29.995 | 89.979 | 59.986 | [^10] (repaired, simplified) |
| <img src="preview/a.smooth_zero/insect_gao.png" width="120"/> | [insect_gao](preview/a.smooth_zero/insect_gao.stl) | 0 | 39.370 | 118.104 | 78.736 | [^4] |
| <img src="preview/a.smooth_zero/isidore_horse_gao.png" width="120"/> | [isidore_horse_gao](preview/a.smooth_zero/isidore_horse_gao.stl) | 0 | 19.465 | 58.389 | 38.926 | [^4] |
| <img src="preview/a.smooth_zero/kid00_topkids.png" width="120"/> | [kid00_topkids](preview/a.smooth_zero/kid00_topkids.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 11.510 | 34.524 | 23.016 | [^12] (repaired) |
| <img src="preview/a.smooth_zero/koala_stein.png" width="120"/> | [koala_stein](preview/a.smooth_zero/koala_stein.stl) | 0 | 3.560 | 10.674 | 7.116 | [^8] |
| <img src="preview/a.smooth_zero/kong_loopy.png" width="120"/> | [kong_loopy](preview/a.smooth_zero/kong_loopy.stl) | 0 | 15.778 | 47.328 | 31.552 | [^9] |
| <img src="preview/a.smooth_zero/lenka_new_quadwild.png" width="120"/> | [lenka_new_quadwild](preview/a.smooth_zero/lenka_new_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 6.001 | 17.997 | 11.998 | [^1] |
| <img src="preview/a.smooth_zero/lion_recon_gao.png" width="120"/> | [lion_recon_gao](preview/a.smooth_zero/lion_recon_gao.stl) | 0 | 27.899 | 83.691 | 55.794 | [^4] |
| <img src="preview/a.smooth_zero/lucy_quadwild.png" width="120"/> | [lucy_quadwild](preview/a.smooth_zero/lucy_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 46.090 | 138.264 | 92.176 | [^1] |
| <img src="preview/a.smooth_zero/lucy_skel.png" width="120"/> | [lucy_skel](preview/a.smooth_zero/lucy_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 29.989 | 89.961 | 59.974 | [^3] (simplified) |
| <img src="preview/a.smooth_zero/magalie_hand100K_quadwild.png" width="120"/> | [magalie_hand100K_quadwild](preview/a.smooth_zero/magalie_hand100K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 50.002 | 150.000 | 100.000 | [^1] |
| <img src="preview/a.smooth_zero/mannequin-devil_quadwild.png" width="120"/> | [mannequin-devil_quadwild](preview/a.smooth_zero/mannequin-devil_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 15.445 | 46.329 | 30.886 | [^1] (repaired) |
| <img src="preview/a.smooth_zero/mannequin_mc_quadwild.png" width="120"/> | [mannequin_mc_quadwild](preview/a.smooth_zero/mannequin_mc_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 30.002 | 90.000 | 60.000 | [^1] (repaired, simplified) |
| <img src="preview/a.smooth_zero/max-planck_jacobson.png" width="120"/> | [max-planck_jacobson](preview/a.smooth_zero/max-planck_jacobson.stl) | 0 | 51.212 | 153.630 | 102.420 | [^7] (repaired) |
| <img src="preview/a.smooth_zero/max-planck_quadwild.png" width="120"/> | [max-planck_quadwild](preview/a.smooth_zero/max-planck_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 54.032 | 162.090 | 108.060 | [^1] (repaired) |
| <img src="preview/a.smooth_zero/max_gao.png" width="120"/> | [max_gao](preview/a.smooth_zero/max_gao.stl) | 0 | 9.936 | 29.802 | 19.868 | [^4] |
| <img src="preview/a.smooth_zero/memento_skel.png" width="120"/> | [memento_skel](preview/a.smooth_zero/memento_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 26.277 | 78.825 | 52.550 | [^3] |
| <img src="preview/a.smooth_zero/Mens_Gold_Cup_ASV_Capetown_Penny_Loafer_in_Black_EjPnk3E8fCs_gso.png" width="120"/> | [Mens_Gold_Cup_ASV_Capetown_Penny_Loafer_in_Black_EjPnk3E8fCs_gso](preview/a.smooth_zero/Mens_Gold_Cup_ASV_Capetown_Penny_Loafer_in_Black_EjPnk3E8fCs_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 14.098 | 42.288 | 28.192 | [^6] |
| <img src="preview/a.smooth_zero/moai_gao.png" width="120"/> | [moai_gao](preview/a.smooth_zero/moai_gao.stl) | 0 | 10.002 | 30.000 | 20.000 | [^4] |
| <img src="preview/a.smooth_zero/mouse_gao.png" width="120"/> | [mouse_gao](preview/a.smooth_zero/mouse_gao.stl) | 0 | 13.961 | 41.877 | 27.918 | [^4] |
| <img src="preview/a.smooth_zero/mushroom_stein.png" width="120"/> | [mushroom_stein](preview/a.smooth_zero/mushroom_stein.stl) | 0 | 11.585 | 34.749 | 23.166 | [^8] |
| <img src="preview/a.smooth_zero/Nefertiti_crane.png" width="120"/> | [Nefertiti_crane](preview/a.smooth_zero/Nefertiti_crane.stl) | 0 | 29.999 | 89.991 | 59.994 | [^10] (simplified) |
| <img src="preview/a.smooth_zero/nefertiti_stein.png" width="120"/> | [nefertiti_stein](preview/a.smooth_zero/nefertiti_stein.stl) | 0 | 29.999 | 89.991 | 59.994 | [^8] (simplified) |
| <img src="preview/a.smooth_zero/noisydino_skel.png" width="120"/> | [noisydino_skel](preview/a.smooth_zero/noisydino_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 23.208 | 69.618 | 46.412 | [^3] (repaired) |
| <img src="preview/a.smooth_zero/Nordic_Ware_Original_Bundt_Pan_gso.png" width="120"/> | [Nordic_Ware_Original_Bundt_Pan_gso](preview/a.smooth_zero/Nordic_Ware_Original_Bundt_Pan_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 8.028 | 24.078 | 16.052 | [^6] |
| <img src="preview/a.smooth_zero/octopus_quadwild.png" width="120"/> | [octopus_quadwild](preview/a.smooth_zero/octopus_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 3.258 | 9.768 | 6.512 | [^1] |
| <img src="preview/a.smooth_zero/ogre_crane.png" width="120"/> | [ogre_crane](preview/a.smooth_zero/ogre_crane.stl) | 0 | 19.446 | 58.332 | 38.888 | [^10] (repaired) |
| <img src="preview/a.smooth_zero/ogre_jacobson.png" width="120"/> | [ogre_jacobson](preview/a.smooth_zero/ogre_jacobson.stl) | 0 | 25.669 | 77.001 | 51.334 | [^7] (repaired, simplified) |
| <img src="preview/a.smooth_zero/oni_gao.png" width="120"/> | [oni_gao](preview/a.smooth_zero/oni_gao.stl) | 0 | 12.887 | 38.655 | 25.770 | [^4] |
| <img src="preview/a.smooth_zero/pear_gao.png" width="120"/> | [pear_gao](preview/a.smooth_zero/pear_gao.stl) | 0 | 10.754 | 32.256 | 21.504 | [^4] |
| <img src="preview/a.smooth_zero/penguin_stein.png" width="120"/> | [penguin_stein](preview/a.smooth_zero/penguin_stein.stl) | 0 | 3.362 | 10.080 | 6.720 | [^8] |
| <img src="preview/a.smooth_zero/pensatore_gao.png" width="120"/> | [pensatore_gao](preview/a.smooth_zero/pensatore_gao.stl) | 0 | 19.624 | 58.866 | 39.244 | [^4] |
| <img src="preview/a.smooth_zero/pierrot_gao.png" width="120"/> | [pierrot_gao](preview/a.smooth_zero/pierrot_gao.stl) | 0 | 16.551 | 49.647 | 33.098 | [^4] |
| <img src="preview/a.smooth_zero/pig_crane.png" width="120"/> | [pig_crane](preview/a.smooth_zero/pig_crane.stl) | 0 | 4.434 | 13.296 | 8.864 | [^10] (repaired) |
| <img src="preview/a.smooth_zero/pig_gao.png" width="120"/> | [pig_gao](preview/a.smooth_zero/pig_gao.stl) | 0 | 15.594 | 46.776 | 31.184 | [^4] |
| <img src="preview/a.smooth_zero/pig_loopy.png" width="120"/> | [pig_loopy](preview/a.smooth_zero/pig_loopy.stl) | 0 | 3.166 | 9.492 | 6.328 | [^9] |
| <img src="preview/a.smooth_zero/polygirl_quadwild.png" width="120"/> | [polygirl_quadwild](preview/a.smooth_zero/polygirl_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 8.506 | 25.512 | 17.008 | [^1] (repaired) |
| <img src="preview/a.smooth_zero/rabbit_loopy.png" width="120"/> | [rabbit_loopy](preview/a.smooth_zero/rabbit_loopy.stl) | 0 | 8.002 | 24.000 | 16.000 | [^9] |
| <img src="preview/a.smooth_zero/ramses_gao.png" width="120"/> | [ramses_gao](preview/a.smooth_zero/ramses_gao.stl) | 0 | 13.505 | 40.509 | 27.006 | [^4] |
| <img src="preview/a.smooth_zero/red_circular_box100K_quadwild.png" width="120"/> | [red_circular_box100K_quadwild](preview/a.smooth_zero/red_circular_box100K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 50.002 | 150.000 | 100.000 | [^1] |
| <img src="preview/a.smooth_zero/red_circular_box_gao.png" width="120"/> | [red_circular_box_gao](preview/a.smooth_zero/red_circular_box_gao.stl) | 0 | 50.002 | 150.000 | 100.000 | [^4] |
| <img src="preview/a.smooth_zero/retinal_gao.png" width="120"/> | [retinal_gao](preview/a.smooth_zero/retinal_gao.stl) | 0 | 14.566 | 43.692 | 29.128 | [^4] |
| <img src="preview/a.smooth_zero/rgb_dragon_quadwild.png" width="120"/> | [rgb_dragon_quadwild](preview/a.smooth_zero/rgb_dragon_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 52.513 | 157.533 | 105.022 | [^1] |
| <img src="preview/a.smooth_zero/santa_gao.png" width="120"/> | [santa_gao](preview/a.smooth_zero/santa_gao.stl) | 0 | 10.406 | 31.212 | 20.808 | [^4] |
| <img src="preview/a.smooth_zero/scapula_skel.png" width="120"/> | [scapula_skel](preview/a.smooth_zero/scapula_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 30.001 | 89.997 | 59.998 | [^3] (simplified) |
| <img src="preview/a.smooth_zero/scorpion_stein.png" width="120"/> | [scorpion_stein](preview/a.smooth_zero/scorpion_stein.stl) | 0 | 6.315 | 18.939 | 12.626 | [^8] |
| <img src="preview/a.smooth_zero/screwdriver_gao.png" width="120"/> | [screwdriver_gao](preview/a.smooth_zero/screwdriver_gao.stl) | 0 | 24.568 | 73.698 | 49.132 | [^4] |
| <img src="preview/a.smooth_zero/sediapatch_gao.png" width="120"/> | [sediapatch_gao](preview/a.smooth_zero/sediapatch_gao.stl) | 0 | 15.584 | 46.746 | 31.164 | [^4] |
| <img src="preview/a.smooth_zero/shark_quadwild.png" width="120"/> | [shark_quadwild](preview/a.smooth_zero/shark_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 10.054 | 30.156 | 20.104 | [^1] |
| <img src="preview/a.smooth_zero/sphere_stein.png" width="120"/> | [sphere_stein](preview/a.smooth_zero/sphere_stein.stl) | 0 | 642 | 1.920 | 1.280 | [^8] |
| <img src="preview/a.smooth_zero/sphinx_gao.png" width="120"/> | [sphinx_gao](preview/a.smooth_zero/sphinx_gao.stl) | 0 | 10.608 | 31.818 | 21.212 | [^4] |
| <img src="preview/a.smooth_zero/sphinx_loopy.png" width="120"/> | [sphinx_loopy](preview/a.smooth_zero/sphinx_loopy.stl) | 0 | 10.184 | 30.546 | 20.364 | [^9] |
| <img src="preview/a.smooth_zero/spider_skel.png" width="120"/> | [spider_skel](preview/a.smooth_zero/spider_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 882 | 2.640 | 1.760 | [^3] (repaired) |
| <img src="preview/a.smooth_zero/spot_crane.png" width="120"/> | [spot_crane](preview/a.smooth_zero/spot_crane.stl) | 0 | 2.930 | 8.784 | 5.856 | [^10] |
| <img src="preview/a.smooth_zero/spot_snoep.png" width="120"/> | [spot_snoep](preview/a.smooth_zero/spot_snoep.stl) | 0 | 11.533 | 34.593 | 23.062 | [^8] (re-oriented) |
| <img src="preview/a.smooth_zero/spot_stein.png" width="120"/> | [spot_stein](preview/a.smooth_zero/spot_stein.stl) | 0 | 11.533 | 34.593 | 23.062 | [^8] |
| <img src="preview/a.smooth_zero/springer_stein.png" width="120"/> | [springer_stein](preview/a.smooth_zero/springer_stein.stl) | 0 | 9.686 | 29.052 | 19.368 | [^8] |
| <img src="preview/a.smooth_zero/squirrel_polycut.png" width="120"/> | [squirrel_polycut](preview/a.smooth_zero/squirrel_polycut.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 29.210 | 87.624 | 58.416 | [^11] |
| <img src="preview/a.smooth_zero/stanford-bunny_jacobson.png" width="120"/> | [stanford-bunny_jacobson](preview/a.smooth_zero/stanford-bunny_jacobson.stl) | 0 | 35.188 | 105.558 | 70.372 | [^7] (repaired) |
| <img src="preview/a.smooth_zero/strawberry_stein.png" width="120"/> | [strawberry_stein](preview/a.smooth_zero/strawberry_stein.stl) | 0 | 29.992 | 89.970 | 59.980 | [^8] (simplified) |
| <img src="preview/a.smooth_zero/stuffedtoy_stein.png" width="120"/> | [stuffedtoy_stein](preview/a.smooth_zero/stuffedtoy_stein.stl) | 0 | 6.669 | 20.001 | 13.334 | [^8] |
| <img src="preview/a.smooth_zero/sword_stein.png" width="120"/> | [sword_stein](preview/a.smooth_zero/sword_stein.stl) | 0 | 22.293 | 66.873 | 44.582 | [^8] |
| <img src="preview/a.smooth_zero/T165_shrec11.png" width="120"/> | [T165_shrec11](preview/a.smooth_zero/T165_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.493 | 28.473 | 18.982 | [^13] |
| <img src="preview/a.smooth_zero/T200_shrec11.png" width="120"/> | [T200_shrec11](preview/a.smooth_zero/T200_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.497 | 28.485 | 18.990 | [^13] |
| <img src="preview/a.smooth_zero/T211_shrec11.png" width="120"/> | [T211_shrec11](preview/a.smooth_zero/T211_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.454 | 28.356 | 18.904 | [^13] |
| <img src="preview/a.smooth_zero/T216_shrec11.png" width="120"/> | [T216_shrec11](preview/a.smooth_zero/T216_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.450 | 28.344 | 18.896 | [^13] |
| <img src="preview/a.smooth_zero/T222_shrec11.png" width="120"/> | [T222_shrec11](preview/a.smooth_zero/T222_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.501 | 28.497 | 18.998 | [^13] |
| <img src="preview/a.smooth_zero/T235_shrec11.png" width="120"/> | [T235_shrec11](preview/a.smooth_zero/T235_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.497 | 28.485 | 18.990 | [^13] |
| <img src="preview/a.smooth_zero/T248_shrec11.png" width="120"/> | [T248_shrec11](preview/a.smooth_zero/T248_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.148 | 27.438 | 18.292 | [^13] |
| <img src="preview/a.smooth_zero/T266_shrec11.png" width="120"/> | [T266_shrec11](preview/a.smooth_zero/T266_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.493 | 28.473 | 18.982 | [^13] |
| <img src="preview/a.smooth_zero/T280_shrec11.png" width="120"/> | [T280_shrec11](preview/a.smooth_zero/T280_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.497 | 28.485 | 18.990 | [^13] |
| <img src="preview/a.smooth_zero/T2_shrec11.png" width="120"/> | [T2_shrec11](preview/a.smooth_zero/T2_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.501 | 28.497 | 18.998 | [^13] |
| <img src="preview/a.smooth_zero/T340_shrec11.png" width="120"/> | [T340_shrec11](preview/a.smooth_zero/T340_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.318 | 27.948 | 18.632 | [^13] |
| <img src="preview/a.smooth_zero/T345_shrec11.png" width="120"/> | [T345_shrec11](preview/a.smooth_zero/T345_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.229 | 27.681 | 18.454 | [^13] |
| <img src="preview/a.smooth_zero/T351_shrec11.png" width="120"/> | [T351_shrec11](preview/a.smooth_zero/T351_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 7.734 | 23.196 | 15.464 | [^13] |
| <img src="preview/a.smooth_zero/T360_shrec11.png" width="120"/> | [T360_shrec11](preview/a.smooth_zero/T360_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.369 | 28.101 | 18.734 | [^13] |
| <img src="preview/a.smooth_zero/T366_shrec11.png" width="120"/> | [T366_shrec11](preview/a.smooth_zero/T366_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.499 | 28.491 | 18.994 | [^13] |
| <img src="preview/a.smooth_zero/T380_shrec11.png" width="120"/> | [T380_shrec11](preview/a.smooth_zero/T380_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.495 | 28.479 | 18.986 | [^13] |
| <img src="preview/a.smooth_zero/T402_shrec11.png" width="120"/> | [T402_shrec11](preview/a.smooth_zero/T402_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.497 | 28.485 | 18.990 | [^13] |
| <img src="preview/a.smooth_zero/T431_shrec11.png" width="120"/> | [T431_shrec11](preview/a.smooth_zero/T431_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.184 | 27.546 | 18.364 | [^13] |
| <img src="preview/a.smooth_zero/T441_shrec11.png" width="120"/> | [T441_shrec11](preview/a.smooth_zero/T441_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.500 | 28.494 | 18.996 | [^13] |
| <img src="preview/a.smooth_zero/T44_shrec11.png" width="120"/> | [T44_shrec11](preview/a.smooth_zero/T44_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.497 | 28.485 | 18.990 | [^13] |
| <img src="preview/a.smooth_zero/T473_shrec11.png" width="120"/> | [T473_shrec11](preview/a.smooth_zero/T473_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.485 | 28.449 | 18.966 | [^13] |
| <img src="preview/a.smooth_zero/T535_shrec11.png" width="120"/> | [T535_shrec11](preview/a.smooth_zero/T535_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.501 | 28.497 | 18.998 | [^13] |
| <img src="preview/a.smooth_zero/T594_shrec11.png" width="120"/> | [T594_shrec11](preview/a.smooth_zero/T594_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.484 | 28.446 | 18.964 | [^13] |
| <img src="preview/a.smooth_zero/T595_shrec11.png" width="120"/> | [T595_shrec11](preview/a.smooth_zero/T595_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.503 | 28.503 | 19.002 | [^13] |
| <img src="preview/a.smooth_zero/T60_shrec11.png" width="120"/> | [T60_shrec11](preview/a.smooth_zero/T60_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.500 | 28.494 | 18.996 | [^13] |
| <img src="preview/a.smooth_zero/T80_shrec11.png" width="120"/> | [T80_shrec11](preview/a.smooth_zero/T80_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.441 | 28.317 | 18.878 | [^13] |
| <img src="preview/a.smooth_zero/T85_shrec11.png" width="120"/> | [T85_shrec11](preview/a.smooth_zero/T85_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.500 | 28.494 | 18.996 | [^13] |
| <img src="preview/a.smooth_zero/T8_shrec11.png" width="120"/> | [T8_shrec11](preview/a.smooth_zero/T8_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.403 | 28.203 | 18.802 | [^13] |
| <img src="preview/a.smooth_zero/T95_shrec11.png" width="120"/> | [T95_shrec11](preview/a.smooth_zero/T95_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 9.404 | 28.206 | 18.804 | [^13] |
| <img src="preview/a.smooth_zero/torque1_loopy.png" width="120"/> | [torque1_loopy](preview/a.smooth_zero/torque1_loopy.stl) | 0 | 2.850 | 8.544 | 5.696 | [^9] |
| <img src="preview/a.smooth_zero/torque_loopy.png" width="120"/> | [torque_loopy](preview/a.smooth_zero/torque_loopy.stl) | 0 | 1.652 | 4.950 | 3.300 | [^9] |
| <img src="preview/a.smooth_zero/torso_quadwild.png" width="120"/> | [torso_quadwild](preview/a.smooth_zero/torso_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 50.002 | 150.000 | 100.000 | [^1] |
| <img src="preview/a.smooth_zero/toy1_gao.png" width="120"/> | [toy1_gao](preview/a.smooth_zero/toy1_gao.stl) | 0 | 13.452 | 40.350 | 26.900 | [^4] |
| <img src="preview/a.smooth_zero/toy2_gao.png" width="120"/> | [toy2_gao](preview/a.smooth_zero/toy2_gao.stl) | 0 | 10.755 | 32.259 | 21.506 | [^4] |
| <img src="preview/a.smooth_zero/trebol_loopy.png" width="120"/> | [trebol_loopy](preview/a.smooth_zero/trebol_loopy.stl) | 0 | 18.176 | 54.522 | 36.348 | [^9] |
| <img src="preview/a.smooth_zero/tree_stein.png" width="120"/> | [tree_stein](preview/a.smooth_zero/tree_stein.stl) | 0 | 30.000 | 89.994 | 59.996 | [^8] (simplified) |
| <img src="preview/a.smooth_zero/uu-memento_gao.png" width="120"/> | [uu-memento_gao](preview/a.smooth_zero/uu-memento_gao.stl) | 0 | 46.510 | 139.524 | 93.016 | [^4] |
| <img src="preview/a.smooth_zero/vase-lion100K_quadwild.png" width="120"/> | [vase-lion100K_quadwild](preview/a.smooth_zero/vase-lion100K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 26.681 | 80.037 | 53.358 | [^1] |
| <img src="preview/a.smooth_zero/venus_gao.png" width="120"/> | [venus_gao](preview/a.smooth_zero/venus_gao.stl) | 0 | 10.874 | 32.616 | 21.744 | [^4] |
| <img src="preview/a.smooth_zero/vessel_loopy.png" width="120"/> | [vessel_loopy](preview/a.smooth_zero/vessel_loopy.stl) | 0 | 2.658 | 7.968 | 5.312 | [^9] |
| <img src="preview/a.smooth_zero/woodenfish_gao.png" width="120"/> | [woodenfish_gao](preview/a.smooth_zero/woodenfish_gao.stl) | 0 | 15.940 | 47.814 | 31.876 | [^4] |

### (b) smooth (g≥1, n=95)
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | model | genus | vertices | edges | triangles | source |
|-|-------|-------|----------|-------|-----------|--------|
| <img src="preview/b.smooth_plus/10.102_knotplot.png" width="120"/> | [10.102_knotplot](preview/b.smooth_plus/10.102_knotplot.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 4.312 | 12.936 | 8.624 | [^14] |
| <img src="preview/b.smooth_plus/17674_skel.png" width="120"/> | [17674_skel](preview/b.smooth_plus/17674_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 29.211 | 87.639 | 58.426 | [^3] (repaired, simplified) |
| <img src="preview/b.smooth_plus/3_holes_quadwild.png" width="120"/> | [3_holes_quadwild](preview/b.smooth_plus/3_holes_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 9.847 | 29.553 | 19.702 | [^1] |
| <img src="preview/b.smooth_plus/ACE_Coffee_Mug_Kristen_16_oz_cup_gso.png" width="120"/> | [ACE_Coffee_Mug_Kristen_16_oz_cup_gso](preview/b.smooth_plus/ACE_Coffee_Mug_Kristen_16_oz_cup_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 5.612 | 16.836 | 11.224 | [^6] |
| <img src="preview/b.smooth_plus/Aroma_Stainless_Steel_Milk_Frother_2_Cup_gso.png" width="120"/> | [Aroma_Stainless_Steel_Milk_Frother_2_Cup_gso](preview/b.smooth_plus/Aroma_Stainless_Steel_Milk_Frother_2_Cup_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 10 | 10.771 | 32.367 | 21.578 | [^6] (repaired) |
| <img src="preview/b.smooth_plus/bob_crane.png" width="120"/> | [bob_crane](preview/b.smooth_plus/bob_crane.stl) | 1 | 5.344 | 16.032 | 10.688 | [^10] |
| <img src="preview/b.smooth_plus/boot_stein.png" width="120"/> | [boot_stein](preview/b.smooth_plus/boot_stein.stl) | 12 | 19.931 | 59.859 | 39.906 | [^8] |
| <img src="preview/b.smooth_plus/botijo_gao.png" width="120"/> | [botijo_gao](preview/b.smooth_plus/botijo_gao.stl) | 5 | 12.127 | 36.405 | 24.270 | [^4] |
| <img src="preview/b.smooth_plus/bottle1_gao.png" width="120"/> | [bottle1_gao](preview/b.smooth_plus/bottle1_gao.stl) | 1 | 14.832 | 44.496 | 29.664 | [^4] |
| <img src="preview/b.smooth_plus/bottle2_gao.png" width="120"/> | [bottle2_gao](preview/b.smooth_plus/bottle2_gao.stl) | 1 | 14.595 | 43.785 | 29.190 | [^4] |
| <img src="preview/b.smooth_plus/bozbezbozzel50K_quadwild.png" width="120"/> | [bozbezbozzel50K_quadwild](preview/b.smooth_plus/bozbezbozzel50K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 24.992 | 75.000 | 50.000 | [^1] |
| <img src="preview/b.smooth_plus/brain_quadwild.png" width="120"/> | [brain_quadwild](preview/b.smooth_plus/brain_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 57 | 49.888 | 150.000 | 100.000 | [^1] |
| <img src="preview/b.smooth_plus/bumpy_torus_gao.png" width="120"/> | [bumpy_torus_gao](preview/b.smooth_plus/bumpy_torus_gao.stl) | 1 | 15.279 | 45.837 | 30.558 | [^4] |
| <img src="preview/b.smooth_plus/camel_gao.png" width="120"/> | [camel_gao](preview/b.smooth_plus/camel_gao.stl) | 1 | 34.546 | 103.638 | 69.092 | [^4] |
| <img src="preview/b.smooth_plus/Centaur_tds.png" width="120"/> | [Centaur_tds](preview/b.smooth_plus/Centaur_tds.stl) | 9 | 29.973 | 89.967 | 59.978 | [^15] (repaired, simplified, rescaled) |
| <img src="preview/b.smooth_plus/chair1_gao.png" width="120"/> | [chair1_gao](preview/b.smooth_plus/chair1_gao.stl) | 4 | 11.421 | 34.281 | 22.854 | [^4] |
| <img src="preview/b.smooth_plus/chair_gao.png" width="120"/> | [chair_gao](preview/b.smooth_plus/chair_gao.stl) | 7 | 23.081 | 69.279 | 46.186 | [^4] |
| <img src="preview/b.smooth_plus/Cole_Hardware_Mug_Classic_Blue_gso.png" width="120"/> | [Cole_Hardware_Mug_Classic_Blue_gso](preview/b.smooth_plus/Cole_Hardware_Mug_Classic_Blue_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 4.358 | 13.074 | 8.716 | [^6] |
| <img src="preview/b.smooth_plus/cow_stein.png" width="120"/> | [cow_stein](preview/b.smooth_plus/cow_stein.stl) | 1 | 29.991 | 89.973 | 59.982 | [^8] (simplified) |
| <img src="preview/b.smooth_plus/Cup1_gao.png" width="120"/> | [Cup1_gao](preview/b.smooth_plus/Cup1_gao.stl) | 1 | 15.564 | 46.692 | 31.128 | [^4] |
| <img src="preview/b.smooth_plus/cup_gao.png" width="120"/> | [cup_gao](preview/b.smooth_plus/cup_gao.stl) | 2 | 10.495 | 31.491 | 20.994 | [^4] |
| <img src="preview/b.smooth_plus/dancer2_gao.png" width="120"/> | [dancer2_gao](preview/b.smooth_plus/dancer2_gao.stl) | 1 | 30.248 | 90.744 | 60.496 | [^4] |
| <img src="preview/b.smooth_plus/dancer_gao.png" width="120"/> | [dancer_gao](preview/b.smooth_plus/dancer_gao.stl) | 1 | 12.048 | 36.144 | 24.096 | [^4] |
| <img src="preview/b.smooth_plus/dancer_loopy.png" width="120"/> | [dancer_loopy](preview/b.smooth_plus/dancer_loopy.stl) | 1 | 24.998 | 74.994 | 49.996 | [^9] |
| <img src="preview/b.smooth_plus/dancing_children_gao.png" width="120"/> | [dancing_children_gao](preview/b.smooth_plus/dancing_children_gao.stl) | 8 | 12.163 | 36.531 | 24.354 | [^4] |
| <img src="preview/b.smooth_plus/demosthenes_stein.png" width="120"/> | [demosthenes_stein](preview/b.smooth_plus/demosthenes_stein.stl) | 1 | 29.965 | 89.895 | 59.930 | [^8] (repaired, simplified) |
| <img src="preview/b.smooth_plus/desertrose_crane.png" width="120"/> | [desertrose_crane](preview/b.smooth_plus/desertrose_crane.stl) | 1 | 31.680 | 95.040 | 63.360 | [^10] (repaired) |
| <img src="preview/b.smooth_plus/Diamond_Visions_Scissors_Red_gso.png" width="120"/> | [Diamond_Visions_Scissors_Red_gso](preview/b.smooth_plus/Diamond_Visions_Scissors_Red_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 7 | 3.396 | 10.224 | 6.816 | [^6] |
| <img src="preview/b.smooth_plus/double_torus_quadwild.png" width="120"/> | [double_torus_quadwild](preview/b.smooth_plus/double_torus_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 2.353 | 7.065 | 4.710 | [^1] |
| <img src="preview/b.smooth_plus/dragon0_quadwild.png" width="120"/> | [dragon0_quadwild](preview/b.smooth_plus/dragon0_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 26.176 | 78.528 | 52.352 | [^1] |
| <img src="preview/b.smooth_plus/dragon_stand_gao.png" width="120"/> | [dragon_stand_gao](preview/b.smooth_plus/dragon_stand_gao.stl) | 1 | 21.042 | 63.126 | 42.084 | [^4] |
| <img src="preview/b.smooth_plus/dragon_vrip_stanford.png" width="120"/> | [dragon_vrip_stanford](preview/b.smooth_plus/dragon_vrip_stanford.stl) | 3 | 29.750 | 89.262 | 59.508 | [^16] (repaired, simplified) |
| <img src="preview/b.smooth_plus/dragonstand2_gao.png" width="120"/> | [dragonstand2_gao](preview/b.smooth_plus/dragonstand2_gao.stl) | 1 | 30.561 | 91.683 | 61.122 | [^4] |
| <img src="preview/b.smooth_plus/dtorus_gao.png" width="120"/> | [dtorus_gao](preview/b.smooth_plus/dtorus_gao.stl) | 2 | 10.090 | 30.276 | 20.184 | [^4] |
| <img src="preview/b.smooth_plus/eight_gao.png" width="120"/> | [eight_gao](preview/b.smooth_plus/eight_gao.stl) | 2 | 5.544 | 16.638 | 11.092 | [^4] |
| <img src="preview/b.smooth_plus/ele12a_skel.png" width="120"/> | [ele12a_skel](preview/b.smooth_plus/ele12a_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 50.484 | 151.464 | 100.976 | [^3] |
| <img src="preview/b.smooth_plus/elephant_gao.png" width="120"/> | [elephant_gao](preview/b.smooth_plus/elephant_gao.stl) | 3 | 38.084 | 114.264 | 76.176 | [^4] |
| <img src="preview/b.smooth_plus/elk_gao.png" width="120"/> | [elk_gao](preview/b.smooth_plus/elk_gao.stl) | 1 | 23.114 | 69.342 | 46.228 | [^4] |
| <img src="preview/b.smooth_plus/feline_quadwild.png" width="120"/> | [feline_quadwild](preview/b.smooth_plus/feline_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 20.659 | 61.983 | 41.322 | [^1] |
| <img src="preview/b.smooth_plus/femur_quadwild.png" width="120"/> | [femur_quadwild](preview/b.smooth_plus/femur_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 3.897 | 11.697 | 7.798 | [^1] |
| <img src="preview/b.smooth_plus/fertility_gao.png" width="120"/> | [fertility_gao](preview/b.smooth_plus/fertility_gao.stl) | 4 | 26.222 | 78.684 | 52.456 | [^4] |
| <img src="preview/b.smooth_plus/filigree100k_quadwild.png" width="120"/> | [filigree100k_quadwild](preview/b.smooth_plus/filigree100k_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 65 | 49.872 | 150.000 | 100.000 | [^1] |
| <img src="preview/b.smooth_plus/genus3_gao.png" width="120"/> | [genus3_gao](preview/b.smooth_plus/genus3_gao.stl) | 3 | 33.952 | 101.868 | 67.912 | [^4] |
| <img src="preview/b.smooth_plus/Granimals_20_Wooden_ABC_Blocks_Wagon_g2TinmUGGHI_gso.png" width="120"/> | [Granimals_20_Wooden_ABC_Blocks_Wagon_g2TinmUGGHI_gso](preview/b.smooth_plus/Granimals_20_Wooden_ABC_Blocks_Wagon_g2TinmUGGHI_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 6.162 | 18.504 | 12.336 | [^6] |
| <img src="preview/b.smooth_plus/grayloc_gao.png" width="120"/> | [grayloc_gao](preview/b.smooth_plus/grayloc_gao.stl) | 9 | 11.339 | 34.065 | 22.710 | [^4] |
| <img src="preview/b.smooth_plus/greek_sculpture_gao.png" width="120"/> | [greek_sculpture_gao](preview/b.smooth_plus/greek_sculpture_gao.stl) | 4 | 12.501 | 37.521 | 25.014 | [^4] |
| <img src="preview/b.smooth_plus/greek_sculpture_quadwild.png" width="120"/> | [greek_sculpture_quadwild](preview/b.smooth_plus/greek_sculpture_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 24.994 | 75.000 | 50.000 | [^1] |
| <img src="preview/b.smooth_plus/happy_vrip_stanford.png" width="120"/> | [happy_vrip_stanford](preview/b.smooth_plus/happy_vrip_stanford.stl) | 10 | 29.419 | 88.311 | 58.874 | [^16] (repaired, simplified) |
| <img src="preview/b.smooth_plus/heptoroid_skel.png" width="120"/> | [heptoroid_skel](preview/b.smooth_plus/heptoroid_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 22 | 29.957 | 89.997 | 59.998 | [^3] (simplified) |
| <img src="preview/b.smooth_plus/holes2_loopy.png" width="120"/> | [holes2_loopy](preview/b.smooth_plus/holes2_loopy.stl) | 2 | 2.922 | 8.772 | 5.848 | [^9] |
| <img src="preview/b.smooth_plus/holes3_gao.png" width="120"/> | [holes3_gao](preview/b.smooth_plus/holes3_gao.stl) | 3 | 14.396 | 43.200 | 28.800 | [^4] |
| <img src="preview/b.smooth_plus/hound_skel.png" width="120"/> | [hound_skel](preview/b.smooth_plus/hound_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 6 | 7.538 | 22.644 | 15.096 | [^3] (repaired) |
| <img src="preview/b.smooth_plus/house_stein.png" width="120"/> | [house_stein](preview/b.smooth_plus/house_stein.stl) | 36 | 28.940 | 87.030 | 58.020 | [^8] (repaired, simplified) |
| <img src="preview/b.smooth_plus/indorelax_loopy.png" width="120"/> | [indorelax_loopy](preview/b.smooth_plus/indorelax_loopy.stl) | 2 | 12.128 | 36.390 | 24.260 | [^9] |
| <img src="preview/b.smooth_plus/jbs_003_quadwild.png" width="120"/> | [jbs_003_quadwild](preview/b.smooth_plus/jbs_003_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 24.994 | 75.000 | 50.000 | [^1] |
| <img src="preview/b.smooth_plus/Kiss_gao.png" width="120"/> | [Kiss_gao](preview/b.smooth_plus/Kiss_gao.stl) | 3 | 10.192 | 30.588 | 20.392 | [^4] |
| <img src="preview/b.smooth_plus/kiss_loopy.png" width="120"/> | [kiss_loopy](preview/b.smooth_plus/kiss_loopy.stl) | 3 | 12.738 | 38.226 | 25.484 | [^9] |
| <img src="preview/b.smooth_plus/kitten_gao.png" width="120"/> | [kitten_gao](preview/b.smooth_plus/kitten_gao.stl) | 1 | 10.183 | 30.549 | 20.366 | [^4] |
| <img src="preview/b.smooth_plus/kitten_loopy.png" width="120"/> | [kitten_loopy](preview/b.smooth_plus/kitten_loopy.stl) | 1 | 3.178 | 9.534 | 6.356 | [^9] |
| <img src="preview/b.smooth_plus/knot1_cgal.png" width="120"/> | [knot1_cgal](preview/b.smooth_plus/knot1_cgal.stl) | 1 | 3.200 | 9.600 | 6.400 | [^17] |
| <img src="preview/b.smooth_plus/knot_cgal.png" width="120"/> | [knot_cgal](preview/b.smooth_plus/knot_cgal.stl) | 1 | 2.080 | 6.240 | 4.160 | [^17] |
| <img src="preview/b.smooth_plus/laurent_hand_quadwild.png" width="120"/> | [laurent_hand_quadwild](preview/b.smooth_plus/laurent_hand_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 55.957 | 167.871 | 111.914 | [^1] (repaired) |
| <img src="preview/b.smooth_plus/lionstatue_stein.png" width="120"/> | [lionstatue_stein](preview/b.smooth_plus/lionstatue_stein.stl) | 3 | 37.159 | 111.489 | 74.326 | [^8] (repaired) |
| <img src="preview/b.smooth_plus/lissajous_knotplot.png" width="120"/> | [lissajous_knotplot](preview/b.smooth_plus/lissajous_knotplot.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 1.995 | 5.985 | 3.990 | [^14] |
| <img src="preview/b.smooth_plus/master_cylinder_gao.png" width="120"/> | [master_cylinder_gao](preview/b.smooth_plus/master_cylinder_gao.stl) | 3 | 13.689 | 41.079 | 27.386 | [^4] |
| <img src="preview/b.smooth_plus/neptune_quadwild.png" width="120"/> | [neptune_quadwild](preview/b.smooth_plus/neptune_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 23.687 | 71.073 | 47.382 | [^1] |
| <img src="preview/b.smooth_plus/neptune_skel.png" width="120"/> | [neptune_skel](preview/b.smooth_plus/neptune_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 28.052 | 84.168 | 56.112 | [^3] |
| <img src="preview/b.smooth_plus/Ocedar_Snap_On_Dust_Pan_And_Brush_1_ct_gso.png" width="120"/> | [Ocedar_Snap_On_Dust_Pan_And_Brush_1_ct_gso](preview/b.smooth_plus/Ocedar_Snap_On_Dust_Pan_And_Brush_1_ct_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 7.322 | 21.984 | 14.656 | [^6] |
| <img src="preview/b.smooth_plus/oil_pump_gao.png" width="120"/> | [oil_pump_gao](preview/b.smooth_plus/oil_pump_gao.stl) | 4 | 68.742 | 206.244 | 137.496 | [^4] |
| <img src="preview/b.smooth_plus/parsnip_stein.png" width="120"/> | [parsnip_stein](preview/b.smooth_plus/parsnip_stein.stl) | 12 | 29.715 | 89.211 | 59.474 | [^8] (simplified) |
| <img src="preview/b.smooth_plus/pegaso_quadwild.png" width="120"/> | [pegaso_quadwild](preview/b.smooth_plus/pegaso_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 6 | 15.319 | 45.987 | 30.658 | [^1] |
| <img src="preview/b.smooth_plus/PittsburghBridge_crane.png" width="120"/> | [PittsburghBridge_crane](preview/b.smooth_plus/PittsburghBridge_crane.stl) | 3 | 29.995 | 89.997 | 59.998 | [^10] |
| <img src="preview/b.smooth_plus/pizza_stein.png" width="120"/> | [pizza_stein](preview/b.smooth_plus/pizza_stein.stl) | 65 | 28.664 | 86.376 | 57.584 | [^8] (repaired) |
| <img src="preview/b.smooth_plus/raptor50K_quadwild.png" width="120"/> | [raptor50K_quadwild](preview/b.smooth_plus/raptor50K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 10 | 23.269 | 69.861 | 46.574 | [^1] |
| <img src="preview/b.smooth_plus/rhino_skel.png" width="120"/> | [rhino_skel](preview/b.smooth_plus/rhino_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 2.963 | 8.889 | 5.926 | [^3] (repaired) |
| <img src="preview/b.smooth_plus/robocat_deci_quadwild.png" width="120"/> | [robocat_deci_quadwild](preview/b.smooth_plus/robocat_deci_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 3.756 | 11.268 | 7.512 | [^1] |
| <img src="preview/b.smooth_plus/rockerArm_skel.png" width="120"/> | [rockerArm_skel](preview/b.smooth_plus/rockerArm_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 40.177 | 120.531 | 80.354 | [^3] |
| <img src="preview/b.smooth_plus/sacrum_skel.png" width="120"/> | [sacrum_skel](preview/b.smooth_plus/sacrum_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 17 | 29.968 | 90.000 | 60.000 | [^3] (simplified) |
| <img src="preview/b.smooth_plus/seabowl_skel.png" width="120"/> | [seabowl_skel](preview/b.smooth_plus/seabowl_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 45.095 | 135.303 | 90.202 | [^3] |
| <img src="preview/b.smooth_plus/seahorse2_100K_quadwild.png" width="120"/> | [seahorse2_100K_quadwild](preview/b.smooth_plus/seahorse2_100K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 8 | 49.986 | 150.000 | 100.000 | [^1] |
| <img src="preview/b.smooth_plus/skotknot_knotplot.png" width="120"/> | [skotknot_knotplot](preview/b.smooth_plus/skotknot_knotplot.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 308 | 924 | 616 | [^14] |
| <img src="preview/b.smooth_plus/skull_stein.png" width="120"/> | [skull_stein](preview/b.smooth_plus/skull_stein.stl) | 2 | 5.154 | 15.468 | 10.312 | [^8] |
| <img src="preview/b.smooth_plus/T137_shrec11.png" width="120"/> | [T137_shrec11](preview/b.smooth_plus/T137_shrec11.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 9.388 | 28.164 | 18.776 | [^13] |
| <img src="preview/b.smooth_plus/teaport_gao.png" width="120"/> | [teaport_gao](preview/b.smooth_plus/teaport_gao.stl) | 1 | 13.464 | 40.392 | 26.928 | [^4] |
| <img src="preview/b.smooth_plus/teapot_loopy.png" width="120"/> | [teapot_loopy](preview/b.smooth_plus/teapot_loopy.stl) | 1 | 6.544 | 19.632 | 13.088 | [^9] |
| <img src="preview/b.smooth_plus/thai_statue_gao.png" width="120"/> | [thai_statue_gao](preview/b.smooth_plus/thai_statue_gao.stl) | 3 | 20.133 | 60.411 | 40.274 | [^4] |
| <img src="preview/b.smooth_plus/torus2_quadwild.png" width="120"/> | [torus2_quadwild](preview/b.smooth_plus/torus2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 2.915 | 8.751 | 5.834 | [^1] (repaired) |
| <img src="preview/b.smooth_plus/torus_stein.png" width="120"/> | [torus_stein](preview/b.smooth_plus/torus_stein.stl) | 1 | 2.304 | 6.912 | 4.608 | [^8] |
| <img src="preview/b.smooth_plus/tower_stein.png" width="120"/> | [tower_stein](preview/b.smooth_plus/tower_stein.stl) | 2 | 29.966 | 89.904 | 59.936 | [^8] (simplified) |
| <img src="preview/b.smooth_plus/Townley-Greyhounds_tds.png" width="120"/> | [Townley-Greyhounds_tds](preview/b.smooth_plus/Townley-Greyhounds_tds.stl) | 5 | 29.981 | 89.967 | 59.978 | [^15] (repaired, simplified) |
| <img src="preview/b.smooth_plus/vase0_quadwild.png" width="120"/> | [vase0_quadwild](preview/b.smooth_plus/vase0_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 2.651 | 7.953 | 5.302 | [^1] |
| <img src="preview/b.smooth_plus/Vertebrae_quadwild.png" width="120"/> | [Vertebrae_quadwild](preview/b.smooth_plus/Vertebrae_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 43.912 | 131.736 | 87.824 | [^1] |
| <img src="preview/b.smooth_plus/violin_stein.png" width="120"/> | [violin_stein](preview/b.smooth_plus/violin_stein.stl) | 5 | 29.991 | 89.997 | 59.998 | [^8] (simplified) |
| <img src="preview/b.smooth_plus/well_stein.png" width="120"/> | [well_stein](preview/b.smooth_plus/well_stein.stl) | 48 | 29.822 | 89.748 | 59.832 | [^8] (simplified) |
| <img src="preview/b.smooth_plus/wrench_gao.png" width="120"/> | [wrench_gao](preview/b.smooth_plus/wrench_gao.stl) | 1 | 12.997 | 38.991 | 25.994 | [^4] |

### (c) sharp (g=0, n=157)
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | model | genus | vertices | edges | triangles | source |
|-|-------|-------|----------|-------|-----------|--------|
| <img src="preview/c.sharp_zero/0_1875_BALL_CUTTER_esb.png" width="120"/> | [0_1875_BALL_CUTTER_esb](preview/c.sharp_zero/0_1875_BALL_CUTTER_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 3.399 | 10.191 | 6.794 | [^18] (repaired) |
| <img src="preview/c.sharp_zero/18020_skel.png" width="120"/> | [18020_skel](preview/c.sharp_zero/18020_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 24.786 | 74.352 | 49.568 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/1MOTOR_esb.png" width="120"/> | [1MOTOR_esb](preview/c.sharp_zero/1MOTOR_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 244 | 726 | 484 | [^18] |
| <img src="preview/c.sharp_zero/20306_skel.png" width="120"/> | [20306_skel](preview/c.sharp_zero/20306_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 300 | 894 | 596 | [^3] |
| <img src="preview/c.sharp_zero/20_esb.png" width="120"/> | [20_esb](preview/c.sharp_zero/20_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 24 | 66 | 44 | [^18] |
| <img src="preview/c.sharp_zero/21464_skel.png" width="120"/> | [21464_skel](preview/c.sharp_zero/21464_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 1.015 | 3.039 | 2.026 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/21788_skel.png" width="120"/> | [21788_skel](preview/c.sharp_zero/21788_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.877 | 14.625 | 9.750 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/22701_skel.png" width="120"/> | [22701_skel](preview/c.sharp_zero/22701_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 52.784 | 158.346 | 105.564 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/22826_skel.png" width="120"/> | [22826_skel](preview/c.sharp_zero/22826_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 1.765 | 5.289 | 3.526 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/22_esb.png" width="120"/> | [22_esb](preview/c.sharp_zero/22_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 20 | 54 | 36 | [^18] |
| <img src="preview/c.sharp_zero/23091_skel.png" width="120"/> | [23091_skel](preview/c.sharp_zero/23091_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.120 | 12.354 | 8.236 | [^3] |
| <img src="preview/c.sharp_zero/3035_gao.png" width="120"/> | [3035_gao](preview/c.sharp_zero/3035_gao.stl) | 0 | 3.568 | 10.698 | 7.132 | [^4] |
| <img src="preview/c.sharp_zero/3_octa-flower_gao.png" width="120"/> | [3_octa-flower_gao](preview/c.sharp_zero/3_octa-flower_gao.stl) | 0 | 7.919 | 23.751 | 15.834 | [^4] |
| <img src="preview/c.sharp_zero/86849_snoep.png" width="120"/> | [86849_snoep](preview/c.sharp_zero/86849_snoep.stl) | 0 | 7.569 | 22.701 | 15.134 | [^2] (remeshed, re-oriented) |
| <img src="preview/c.sharp_zero/86849_thingi.png" width="120"/> | [86849_thingi](preview/c.sharp_zero/86849_thingi.stl) | 0 | 5.054 | 15.156 | 10.104 | [^2] |
| <img src="preview/c.sharp_zero/aries70_new1a_1_gao.png" width="120"/> | [aries70_new1a_1_gao](preview/c.sharp_zero/aries70_new1a_1_gao.stl) | 0 | 4.357 | 13.065 | 8.710 | [^4] |
| <img src="preview/c.sharp_zero/B0_mambo.png" width="120"/> | [B0_mambo](preview/c.sharp_zero/B0_mambo.stl) | 0 | 560 | 1.674 | 1.116 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B11_mambo.png" width="120"/> | [B11_mambo](preview/c.sharp_zero/B11_mambo.stl) | 0 | 1.139 | 3.411 | 2.274 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B12_mambo.png" width="120"/> | [B12_mambo](preview/c.sharp_zero/B12_mambo.stl) | 0 | 885 | 2.649 | 1.766 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B14_mambo.png" width="120"/> | [B14_mambo](preview/c.sharp_zero/B14_mambo.stl) | 0 | 74.218 | 222.648 | 148.432 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B15_mambo.png" width="120"/> | [B15_mambo](preview/c.sharp_zero/B15_mambo.stl) | 0 | 10.769 | 32.301 | 21.534 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B16_mambo.png" width="120"/> | [B16_mambo](preview/c.sharp_zero/B16_mambo.stl) | 0 | 217 | 645 | 430 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B17_mambo.png" width="120"/> | [B17_mambo](preview/c.sharp_zero/B17_mambo.stl) | 0 | 363 | 1.083 | 722 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B18_mambo.png" width="120"/> | [B18_mambo](preview/c.sharp_zero/B18_mambo.stl) | 0 | 329 | 981 | 654 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B19_mambo.png" width="120"/> | [B19_mambo](preview/c.sharp_zero/B19_mambo.stl) | 0 | 1.641 | 4.917 | 3.278 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B20_mambo.png" width="120"/> | [B20_mambo](preview/c.sharp_zero/B20_mambo.stl) | 0 | 159 | 471 | 314 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B21_mambo.png" width="120"/> | [B21_mambo](preview/c.sharp_zero/B21_mambo.stl) | 0 | 478 | 1.428 | 952 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B23_mambo.png" width="120"/> | [B23_mambo](preview/c.sharp_zero/B23_mambo.stl) | 0 | 211 | 627 | 418 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B25_mambo.png" width="120"/> | [B25_mambo](preview/c.sharp_zero/B25_mambo.stl) | 0 | 1.816 | 5.442 | 3.628 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B27_mambo.png" width="120"/> | [B27_mambo](preview/c.sharp_zero/B27_mambo.stl) | 0 | 459 | 1.371 | 914 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B2_mambo.png" width="120"/> | [B2_mambo](preview/c.sharp_zero/B2_mambo.stl) | 0 | 918 | 2.748 | 1.832 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B30_mambo.png" width="120"/> | [B30_mambo](preview/c.sharp_zero/B30_mambo.stl) | 0 | 712 | 2.130 | 1.420 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B34_mambo.png" width="120"/> | [B34_mambo](preview/c.sharp_zero/B34_mambo.stl) | 0 | 514 | 1.536 | 1.024 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B35_mambo.png" width="120"/> | [B35_mambo](preview/c.sharp_zero/B35_mambo.stl) | 0 | 2.115 | 6.339 | 4.226 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B36_mambo.png" width="120"/> | [B36_mambo](preview/c.sharp_zero/B36_mambo.stl) | 0 | 3.991 | 11.967 | 7.978 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B37_mambo.png" width="120"/> | [B37_mambo](preview/c.sharp_zero/B37_mambo.stl) | 0 | 2.668 | 7.998 | 5.332 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B38_mambo.png" width="120"/> | [B38_mambo](preview/c.sharp_zero/B38_mambo.stl) | 0 | 1.956 | 5.862 | 3.908 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B39_mambo.png" width="120"/> | [B39_mambo](preview/c.sharp_zero/B39_mambo.stl) | 0 | 3.628 | 10.878 | 7.252 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B40_mambo.png" width="120"/> | [B40_mambo](preview/c.sharp_zero/B40_mambo.stl) | 0 | 3.171 | 9.507 | 6.338 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B41_mambo.png" width="120"/> | [B41_mambo](preview/c.sharp_zero/B41_mambo.stl) | 0 | 3.529 | 10.581 | 7.054 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B42_mambo.png" width="120"/> | [B42_mambo](preview/c.sharp_zero/B42_mambo.stl) | 0 | 1.843 | 5.523 | 3.682 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B43_mambo.png" width="120"/> | [B43_mambo](preview/c.sharp_zero/B43_mambo.stl) | 0 | 2.626 | 7.872 | 5.248 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B45_mambo.png" width="120"/> | [B45_mambo](preview/c.sharp_zero/B45_mambo.stl) | 0 | 736 | 2.202 | 1.468 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B46_mambo.png" width="120"/> | [B46_mambo](preview/c.sharp_zero/B46_mambo.stl) | 0 | 827 | 2.475 | 1.650 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B48_mambo.png" width="120"/> | [B48_mambo](preview/c.sharp_zero/B48_mambo.stl) | 0 | 1.146 | 3.432 | 2.288 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B49_mambo.png" width="120"/> | [B49_mambo](preview/c.sharp_zero/B49_mambo.stl) | 0 | 528 | 1.578 | 1.052 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B4_mambo.png" width="120"/> | [B4_mambo](preview/c.sharp_zero/B4_mambo.stl) | 0 | 1.216 | 3.642 | 2.428 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B50_mambo.png" width="120"/> | [B50_mambo](preview/c.sharp_zero/B50_mambo.stl) | 0 | 643 | 1.923 | 1.282 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B52_mambo.png" width="120"/> | [B52_mambo](preview/c.sharp_zero/B52_mambo.stl) | 0 | 545 | 1.629 | 1.086 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B54_mambo.png" width="120"/> | [B54_mambo](preview/c.sharp_zero/B54_mambo.stl) | 0 | 425 | 1.269 | 846 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B56_mambo.png" width="120"/> | [B56_mambo](preview/c.sharp_zero/B56_mambo.stl) | 0 | 586 | 1.752 | 1.168 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B57_mambo.png" width="120"/> | [B57_mambo](preview/c.sharp_zero/B57_mambo.stl) | 0 | 4.951 | 14.847 | 9.898 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B58_mambo.png" width="120"/> | [B58_mambo](preview/c.sharp_zero/B58_mambo.stl) | 0 | 735 | 2.199 | 1.466 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B59_mambo.png" width="120"/> | [B59_mambo](preview/c.sharp_zero/B59_mambo.stl) | 0 | 598 | 1.788 | 1.192 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B5_mambo.png" width="120"/> | [B5_mambo](preview/c.sharp_zero/B5_mambo.stl) | 0 | 613 | 1.833 | 1.222 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B60_mambo.png" width="120"/> | [B60_mambo](preview/c.sharp_zero/B60_mambo.stl) | 0 | 1.043 | 3.123 | 2.082 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B61_mambo.png" width="120"/> | [B61_mambo](preview/c.sharp_zero/B61_mambo.stl) | 0 | 1.125 | 3.369 | 2.246 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B67_mambo.png" width="120"/> | [B67_mambo](preview/c.sharp_zero/B67_mambo.stl) | 0 | 1.279 | 3.831 | 2.554 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B68_mambo.png" width="120"/> | [B68_mambo](preview/c.sharp_zero/B68_mambo.stl) | 0 | 1.137 | 3.405 | 2.270 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B69_mambo.png" width="120"/> | [B69_mambo](preview/c.sharp_zero/B69_mambo.stl) | 0 | 2.119 | 6.351 | 4.234 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B6_mambo.png" width="120"/> | [B6_mambo](preview/c.sharp_zero/B6_mambo.stl) | 0 | 659 | 1.971 | 1.314 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B70_mambo.png" width="120"/> | [B70_mambo](preview/c.sharp_zero/B70_mambo.stl) | 0 | 2.280 | 6.834 | 4.556 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B71_mambo.png" width="120"/> | [B71_mambo](preview/c.sharp_zero/B71_mambo.stl) | 0 | 2.175 | 6.519 | 4.346 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B72_mambo.png" width="120"/> | [B72_mambo](preview/c.sharp_zero/B72_mambo.stl) | 0 | 1.685 | 5.049 | 3.366 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B74_mambo.png" width="120"/> | [B74_mambo](preview/c.sharp_zero/B74_mambo.stl) | 0 | 1.313 | 3.933 | 2.622 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B75_mambo.png" width="120"/> | [B75_mambo](preview/c.sharp_zero/B75_mambo.stl) | 0 | 1.709 | 5.121 | 3.414 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B76_mambo.png" width="120"/> | [B76_mambo](preview/c.sharp_zero/B76_mambo.stl) | 0 | 508 | 1.518 | 1.012 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B7_mambo.png" width="120"/> | [B7_mambo](preview/c.sharp_zero/B7_mambo.stl) | 0 | 498 | 1.488 | 992 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B8_mambo.png" width="120"/> | [B8_mambo](preview/c.sharp_zero/B8_mambo.stl) | 0 | 2.794 | 8.376 | 5.584 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/B9_mambo.png" width="120"/> | [B9_mambo](preview/c.sharp_zero/B9_mambo.stl) | 0 | 790 | 2.364 | 1.576 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/bed2_left_sidepannel_esb.png" width="120"/> | [bed2_left_sidepannel_esb](preview/c.sharp_zero/bed2_left_sidepannel_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 36 | 102 | 68 | [^18] |
| <img src="preview/c.sharp_zero/beveled_shoulder_1_quadwild.png" width="120"/> | [beveled_shoulder_1_quadwild](preview/c.sharp_zero/beveled_shoulder_1_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 3.836 | 11.502 | 7.668 | [^1] |
| <img src="preview/c.sharp_zero/blacde_quadwild.png" width="120"/> | [blacde_quadwild](preview/c.sharp_zero/blacde_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 37.378 | 112.128 | 74.752 | [^1] |
| <img src="preview/c.sharp_zero/bladefem_loopy.png" width="120"/> | [bladefem_loopy](preview/c.sharp_zero/bladefem_loopy.stl) | 0 | 6.086 | 18.252 | 12.168 | [^9] |
| <img src="preview/c.sharp_zero/bmw_skel.png" width="120"/> | [bmw_skel](preview/c.sharp_zero/bmw_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 5.251 | 15.747 | 10.498 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/boat_loopy.png" width="120"/> | [boat_loopy](preview/c.sharp_zero/boat_loopy.stl) | 0 | 11.389 | 34.161 | 22.774 | [^9] |
| <img src="preview/c.sharp_zero/boat_stein.png" width="120"/> | [boat_stein](preview/c.sharp_zero/boat_stein.stl) | 0 | 16.210 | 48.624 | 32.416 | [^8] |
| <img src="preview/c.sharp_zero/CC0805_esb.png" width="120"/> | [CC0805_esb](preview/c.sharp_zero/CC0805_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 8 | 18 | 12 | [^18] |
| <img src="preview/c.sharp_zero/chess_pawn_mambo.png" width="120"/> | [chess_pawn_mambo](preview/c.sharp_zero/chess_pawn_mambo.stl) | 0 | 11.613 | 34.833 | 23.222 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/chess_rook_v1_mambo.png" width="120"/> | [chess_rook_v1_mambo](preview/c.sharp_zero/chess_rook_v1_mambo.stl) | 0 | 9.170 | 27.504 | 18.336 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/clef_loopy.png" width="120"/> | [clef_loopy](preview/c.sharp_zero/clef_loopy.stl) | 0 | 1.392 | 4.170 | 2.780 | [^9] |
| <img src="preview/c.sharp_zero/COLLECTOR_13920_esb.png" width="120"/> | [COLLECTOR_13920_esb](preview/c.sharp_zero/COLLECTOR_13920_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 3.173 | 9.513 | 6.342 | [^18] |
| <img src="preview/c.sharp_zero/coverrear_gao.png" width="120"/> | [coverrear_gao](preview/c.sharp_zero/coverrear_gao.stl) | 0 | 39.982 | 119.940 | 79.960 | [^4] |
| <img src="preview/c.sharp_zero/cube_carved_loopy.png" width="120"/> | [cube_carved_loopy](preview/c.sharp_zero/cube_carved_loopy.stl) | 0 | 1.820 | 5.454 | 3.636 | [^9] |
| <img src="preview/c.sharp_zero/cube_minus_sphere_loopy.png" width="120"/> | [cube_minus_sphere_loopy](preview/c.sharp_zero/cube_minus_sphere_loopy.stl) | 0 | 2.066 | 6.192 | 4.128 | [^9] |
| <img src="preview/c.sharp_zero/cube_stein.png" width="120"/> | [cube_stein](preview/c.sharp_zero/cube_stein.stl) | 0 | 26 | 72 | 48 | [^8] |
| <img src="preview/c.sharp_zero/cup_loopy.png" width="120"/> | [cup_loopy](preview/c.sharp_zero/cup_loopy.stl) | 0 | 214 | 636 | 424 | [^9] |
| <img src="preview/c.sharp_zero/cylinder_plate_loopy.png" width="120"/> | [cylinder_plate_loopy](preview/c.sharp_zero/cylinder_plate_loopy.stl) | 0 | 908 | 2.718 | 1.812 | [^9] |
| <img src="preview/c.sharp_zero/din6304_esb.png" width="120"/> | [din6304_esb](preview/c.sharp_zero/din6304_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 890 | 2.664 | 1.776 | [^18] |
| <img src="preview/c.sharp_zero/dpw6g0_nlr.png" width="120"/> | [dpw6g0_nlr](preview/c.sharp_zero/dpw6g0_nlr.stl) | 0 | 31.124 | 93.366 | 62.244 | [^20] (meshed by Stevie-Ray Janssen) |
| <img src="preview/c.sharp_zero/dpw7_nlr.png" width="120"/> | [dpw7_nlr](preview/c.sharp_zero/dpw7_nlr.stl) | 0 | 3.964 | 11.886 | 7.924 | [^20] (meshed by Stevie-Ray Janssen) |
| <img src="preview/c.sharp_zero/eraser_ball_loopy.png" width="120"/> | [eraser_ball_loopy](preview/c.sharp_zero/eraser_ball_loopy.stl) | 0 | 2.624 | 7.866 | 5.244 | [^9] |
| <img src="preview/c.sharp_zero/fandisk_jacobson.png" width="120"/> | [fandisk_jacobson](preview/c.sharp_zero/fandisk_jacobson.stl) | 0 | 6.475 | 19.419 | 12.946 | [^7] |
| <img src="preview/c.sharp_zero/fandisk_libigl.png" width="120"/> | [fandisk_libigl](preview/c.sharp_zero/fandisk_libigl.stl) | 0 | 7.229 | 21.681 | 14.454 | [^21] |
| <img src="preview/c.sharp_zero/feature_loft_mambo.png" width="120"/> | [feature_loft_mambo](preview/c.sharp_zero/feature_loft_mambo.stl) | 0 | 9.242 | 27.720 | 18.480 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/focal-octa_quadwild.png" width="120"/> | [focal-octa_quadwild](preview/c.sharp_zero/focal-octa_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 10.080 | 30.234 | 20.156 | [^1] |
| <img src="preview/c.sharp_zero/gear_loopy.png" width="120"/> | [gear_loopy](preview/c.sharp_zero/gear_loopy.stl) | 0 | 3.931 | 11.787 | 7.858 | [^9] |
| <img src="preview/c.sharp_zero/grandpiano_skel.png" width="120"/> | [grandpiano_skel](preview/c.sharp_zero/grandpiano_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 245 | 729 | 486 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/halved_oblique_scarf_1_quadwild.png" width="120"/> | [halved_oblique_scarf_1_quadwild](preview/c.sharp_zero/halved_oblique_scarf_1_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 1.174 | 3.516 | 2.344 | [^1] |
| <img src="preview/c.sharp_zero/halved_oblique_scarf_2_quadwild.png" width="120"/> | [halved_oblique_scarf_2_quadwild](preview/c.sharp_zero/halved_oblique_scarf_2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 5.566 | 16.692 | 11.128 | [^1] |
| <img src="preview/c.sharp_zero/halved_oblique_scarf_3_loopy.png" width="120"/> | [halved_oblique_scarf_3_loopy](preview/c.sharp_zero/halved_oblique_scarf_3_loopy.stl) | 0 | 36 | 102 | 68 | [^9] |
| <img src="preview/c.sharp_zero/hammer_stein.png" width="120"/> | [hammer_stein](preview/c.sharp_zero/hammer_stein.stl) | 0 | 30.082 | 90.240 | 60.160 | [^8] |
| <img src="preview/c.sharp_zero/heart_skel.png" width="120"/> | [heart_skel](preview/c.sharp_zero/heart_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.877 | 14.625 | 9.750 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/hlpw4_nlr.png" width="120"/> | [hlpw4_nlr](preview/c.sharp_zero/hlpw4_nlr.stl) | 0 | 33.144 | 99.426 | 66.284 | [^22] (meshed by Stevie-Ray Janssen) |
| <img src="preview/c.sharp_zero/hlpw5_nlr.png" width="120"/> | [hlpw5_nlr](preview/c.sharp_zero/hlpw5_nlr.stl) | 0 | 20.730 | 62.184 | 41.456 | [^22] (meshed by Stevie-Ray Janssen) |
| <img src="preview/c.sharp_zero/HMJ_esb.png" width="120"/> | [HMJ_esb](preview/c.sharp_zero/HMJ_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 394 | 1.176 | 784 | [^18] |
| <img src="preview/c.sharp_zero/ico_skel.png" width="120"/> | [ico_skel](preview/c.sharp_zero/ico_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 40.962 | 122.880 | 81.920 | [^3] |
| <img src="preview/c.sharp_zero/inlay_dovetail_1_quadwild.png" width="120"/> | [inlay_dovetail_1_quadwild](preview/c.sharp_zero/inlay_dovetail_1_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 6.956 | 20.862 | 13.908 | [^1] |
| <img src="preview/c.sharp_zero/inlay_dovetail_3_loopy.png" width="120"/> | [inlay_dovetail_3_loopy](preview/c.sharp_zero/inlay_dovetail_3_loopy.stl) | 0 | 32 | 90 | 60 | [^9] |
| <img src="preview/c.sharp_zero/israel_quadwild.png" width="120"/> | [israel_quadwild](preview/c.sharp_zero/israel_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 2.737 | 8.205 | 5.470 | [^1] |
| <img src="preview/c.sharp_zero/jwb-geom-v2-mm_nasa.png" width="120"/> | [jwb-geom-v2-mm_nasa](preview/c.sharp_zero/jwb-geom-v2-mm_nasa.stl) | 0 | 21.673 | 65.013 | 43.342 | [^23] (meshed) |
| <img src="preview/c.sharp_zero/lego_block_mambo.png" width="120"/> | [lego_block_mambo](preview/c.sharp_zero/lego_block_mambo.stl) | 0 | 21.494 | 64.476 | 42.984 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/lego_man_mambo.png" width="120"/> | [lego_man_mambo](preview/c.sharp_zero/lego_man_mambo.stl) | 0 | 7.059 | 21.171 | 14.114 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/lego_quadwild.png" width="120"/> | [lego_quadwild](preview/c.sharp_zero/lego_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 10.602 | 31.800 | 21.200 | [^1] |
| <img src="preview/c.sharp_zero/mech10_loopy.png" width="120"/> | [mech10_loopy](preview/c.sharp_zero/mech10_loopy.stl) | 0 | 256 | 762 | 508 | [^9] |
| <img src="preview/c.sharp_zero/mech_piece_loopy.png" width="120"/> | [mech_piece_loopy](preview/c.sharp_zero/mech_piece_loopy.stl) | 0 | 2.089 | 6.261 | 4.174 | [^9] |
| <img src="preview/c.sharp_zero/mechanical02_loopy.png" width="120"/> | [mechanical02_loopy](preview/c.sharp_zero/mechanical02_loopy.stl) | 0 | 3.588 | 10.758 | 7.172 | [^9] |
| <img src="preview/c.sharp_zero/mechanical04_quadwild.png" width="120"/> | [mechanical04_quadwild](preview/c.sharp_zero/mechanical04_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 4.756 | 14.262 | 9.508 | [^1] |
| <img src="preview/c.sharp_zero/mechanical05_loopy.png" width="120"/> | [mechanical05_loopy](preview/c.sharp_zero/mechanical05_loopy.stl) | 0 | 4.082 | 12.240 | 8.160 | [^9] |
| <img src="preview/c.sharp_zero/mechanical07_quadwild.png" width="120"/> | [mechanical07_quadwild](preview/c.sharp_zero/mechanical07_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 1.130 | 3.384 | 2.256 | [^1] |
| <img src="preview/c.sharp_zero/micscope_skel.png" width="120"/> | [micscope_skel](preview/c.sharp_zero/micscope_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 385 | 1.149 | 766 | [^3] (repaired) |
| <img src="preview/c.sharp_zero/n01o_cross_cyls_sr_hexme.png" width="120"/> | [n01o_cross_cyls_sr_hexme](preview/c.sharp_zero/n01o_cross_cyls_sr_hexme.stl) | 0 | 345 | 1.029 | 686 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n02o_skijump_anti_box_cyl_hexme.png" width="120"/> | [n02o_skijump_anti_box_cyl_hexme](preview/c.sharp_zero/n02o_skijump_anti_box_cyl_hexme.stl) | 0 | 726 | 2.172 | 1.448 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n03o_skijump_box_cyl_hexme.png" width="120"/> | [n03o_skijump_box_cyl_hexme](preview/c.sharp_zero/n03o_skijump_box_cyl_hexme.stl) | 0 | 848 | 2.538 | 1.692 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n06o_anti_pentapyr_hexme.png" width="120"/> | [n06o_anti_pentapyr_hexme](preview/c.sharp_zero/n06o_anti_pentapyr_hexme.stl) | 0 | 5.915 | 17.739 | 11.826 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n07o_anti_pyramid_hexme.png" width="120"/> | [n07o_anti_pyramid_hexme](preview/c.sharp_zero/n07o_anti_pyramid_hexme.stl) | 0 | 6.011 | 18.027 | 12.018 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n08o_pentapyr_hexme.png" width="120"/> | [n08o_pentapyr_hexme](preview/c.sharp_zero/n08o_pentapyr_hexme.stl) | 0 | 961 | 2.877 | 1.918 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n09o_pyramid_hexme.png" width="120"/> | [n09o_pyramid_hexme](preview/c.sharp_zero/n09o_pyramid_hexme.stl) | 0 | 1.274 | 3.816 | 2.544 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n12o_limit_cycle_genus0_hexme.png" width="120"/> | [n12o_limit_cycle_genus0_hexme](preview/c.sharp_zero/n12o_limit_cycle_genus0_hexme.stl) | 0 | 7.640 | 22.914 | 15.276 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n13o_acute_line_hexme.png" width="120"/> | [n13o_acute_line_hexme](preview/c.sharp_zero/n13o_acute_line_hexme.stl) | 0 | 660 | 1.974 | 1.316 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n14o_octahedron_hexme.png" width="120"/> | [n14o_octahedron_hexme](preview/c.sharp_zero/n14o_octahedron_hexme.stl) | 0 | 3.366 | 10.092 | 6.728 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/n15o_icosahedron_hexme.png" width="120"/> | [n15o_icosahedron_hexme](preview/c.sharp_zero/n15o_icosahedron_hexme.stl) | 0 | 6.252 | 18.750 | 12.500 | [^24] (meshed) |
| <img src="preview/c.sharp_zero/nugear_quadwild.png" width="120"/> | [nugear_quadwild](preview/c.sharp_zero/nugear_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 17.331 | 51.987 | 34.658 | [^1] |
| <img src="preview/c.sharp_zero/oloid_crane.png" width="120"/> | [oloid_crane](preview/c.sharp_zero/oloid_crane.stl) | 0 | 4.098 | 12.288 | 8.192 | [^10] |
| <img src="preview/c.sharp_zero/plane_stein.png" width="120"/> | [plane_stein](preview/c.sharp_zero/plane_stein.stl) | 0 | 8.730 | 26.184 | 17.456 | [^8] |
| <img src="preview/c.sharp_zero/Plate1_loopy.png" width="120"/> | [Plate1_loopy](preview/c.sharp_zero/Plate1_loopy.stl) | 0 | 5.980 | 17.934 | 11.956 | [^9] |
| <img src="preview/c.sharp_zero/Plate2_loopy.png" width="120"/> | [Plate2_loopy](preview/c.sharp_zero/Plate2_loopy.stl) | 0 | 4.199 | 12.591 | 8.394 | [^9] |
| <img src="preview/c.sharp_zero/Plate3_loopy.png" width="120"/> | [Plate3_loopy](preview/c.sharp_zero/Plate3_loopy.stl) | 0 | 2.467 | 7.395 | 4.930 | [^9] |
| <img src="preview/c.sharp_zero/Plate4_loopy.png" width="120"/> | [Plate4_loopy](preview/c.sharp_zero/Plate4_loopy.stl) | 0 | 17.795 | 53.379 | 35.586 | [^9] |
| <img src="preview/c.sharp_zero/plate_5_quadwild.png" width="120"/> | [plate_5_quadwild](preview/c.sharp_zero/plate_5_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 10.179 | 30.531 | 20.354 | [^1] |
| <img src="preview/c.sharp_zero/plate_6_quadwild.png" width="120"/> | [plate_6_quadwild](preview/c.sharp_zero/plate_6_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 31.236 | 93.702 | 62.468 | [^1] |
| <img src="preview/c.sharp_zero/prism_loopy.png" width="120"/> | [prism_loopy](preview/c.sharp_zero/prism_loopy.stl) | 0 | 990 | 2.964 | 1.976 | [^9] |
| <img src="preview/c.sharp_zero/rcube_skel.png" width="120"/> | [rcube_skel](preview/c.sharp_zero/rcube_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 24.578 | 73.728 | 49.152 | [^3] |
| <img src="preview/c.sharp_zero/S37_mambo.png" width="120"/> | [S37_mambo](preview/c.sharp_zero/S37_mambo.stl) | 0 | 15.725 | 47.169 | 31.446 | [^19] (meshed) |
| <img src="preview/c.sharp_zero/sbpw1_nlr.png" width="120"/> | [sbpw1_nlr](preview/c.sharp_zero/sbpw1_nlr.stl) | 0 | 22.799 | 68.391 | 45.594 | [^23] (meshed by Stevie-Ray Janssen) |
| <img src="preview/c.sharp_zero/sbpw2_nlr.png" width="120"/> | [sbpw2_nlr](preview/c.sharp_zero/sbpw2_nlr.stl) | 0 | 32.691 | 98.067 | 65.378 | [^23] (meshed by Stevie-Ray Janssen) |
| <img src="preview/c.sharp_zero/sbpw3_nlr.png" width="120"/> | [sbpw3_nlr](preview/c.sharp_zero/sbpw3_nlr.stl) | 0 | 32.348 | 97.038 | 64.692 | [^23] (meshed by Stevie-Ray Janssen) |
| <img src="preview/c.sharp_zero/sharp_sphere10k_quadwild.png" width="120"/> | [sharp_sphere10k_quadwild](preview/c.sharp_zero/sharp_sphere10k_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 21.204 | 63.606 | 42.404 | [^1] |
| <img src="preview/c.sharp_zero/smooth-feature_quadwild.png" width="120"/> | [smooth-feature_quadwild](preview/c.sharp_zero/smooth-feature_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 16.834 | 50.496 | 33.664 | [^1] |
| <img src="preview/c.sharp_zero/spiral_quadwild.png" width="120"/> | [spiral_quadwild](preview/c.sharp_zero/spiral_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 30.613 | 91.833 | 61.222 | [^1] |
| <img src="preview/c.sharp_zero/spring2_quadwild.png" width="120"/> | [spring2_quadwild](preview/c.sharp_zero/spring2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 1.130 | 3.384 | 2.256 | [^1] |
| <img src="preview/c.sharp_zero/spring_quadwild.png" width="120"/> | [spring_quadwild](preview/c.sharp_zero/spring_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 3.620 | 10.854 | 7.236 | [^1] |
| <img src="preview/c.sharp_zero/stab3_quadwild.png" width="120"/> | [stab3_quadwild](preview/c.sharp_zero/stab3_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 0 | 3.316 | 9.942 | 6.628 | [^1] |
| <img src="preview/c.sharp_zero/tris_closed_loopy.png" width="120"/> | [tris_closed_loopy](preview/c.sharp_zero/tris_closed_loopy.stl) | 0 | 690 | 2.064 | 1.376 | [^9] |
| <img src="preview/c.sharp_zero/wave_loopy.png" width="120"/> | [wave_loopy](preview/c.sharp_zero/wave_loopy.stl) | 0 | 576 | 1.722 | 1.148 | [^9] (repaired) |
| <img src="preview/c.sharp_zero/wedge_loopy.png" width="120"/> | [wedge_loopy](preview/c.sharp_zero/wedge_loopy.stl) | 0 | 2.236 | 6.702 | 4.468 | [^9] |
| <img src="preview/c.sharp_zero/wingnut_stein.png" width="120"/> | [wingnut_stein](preview/c.sharp_zero/wingnut_stein.stl) | 0 | 3.047 | 9.135 | 6.090 | [^8] |

### (d) sharp (g≥1, n=238)
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | model | genus | vertices | edges | triangles | source |
|-|-------|-------|----------|-------|-----------|--------|
| <img src="preview/d.sharp_plus/1012A_esb.png" width="120"/> | [1012A_esb](preview/d.sharp_plus/1012A_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 1.693 | 5.103 | 3.402 | [^18] |
| <img src="preview/d.sharp_plus/1142040_esb.png" width="120"/> | [1142040_esb](preview/d.sharp_plus/1142040_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 6 | 1.910 | 5.760 | 3.840 | [^18] |
| <img src="preview/d.sharp_plus/1145480_esb.png" width="120"/> | [1145480_esb](preview/d.sharp_plus/1145480_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 10 | 1.974 | 5.976 | 3.984 | [^18] |
| <img src="preview/d.sharp_plus/1181651_esb.png" width="120"/> | [1181651_esb](preview/d.sharp_plus/1181651_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 884 | 2.700 | 1.800 | [^18] |
| <img src="preview/d.sharp_plus/1236922_esb.png" width="120"/> | [1236922_esb](preview/d.sharp_plus/1236922_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 482 | 1.446 | 964 | [^18] |
| <img src="preview/d.sharp_plus/1274417_esb.png" width="120"/> | [1274417_esb](preview/d.sharp_plus/1274417_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 484 | 1.452 | 968 | [^18] |
| <img src="preview/d.sharp_plus/12_quadwild.png" width="120"/> | [12_quadwild](preview/d.sharp_plus/12_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 25 | 15.711 | 47.277 | 31.518 | [^1] |
| <img src="preview/d.sharp_plus/1305432_esb.png" width="120"/> | [1305432_esb](preview/d.sharp_plus/1305432_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 8 | 1.625 | 4.917 | 3.278 | [^18] |
| <img src="preview/d.sharp_plus/1546387_esb.png" width="120"/> | [1546387_esb](preview/d.sharp_plus/1546387_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 1.263 | 3.813 | 2.542 | [^18] |
| <img src="preview/d.sharp_plus/16t_2d_05w_esb.png" width="120"/> | [16t_2d_05w_esb](preview/d.sharp_plus/16t_2d_05w_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 554 | 1.662 | 1.108 | [^18] |
| <img src="preview/d.sharp_plus/1797609IN_esb.png" width="120"/> | [1797609IN_esb](preview/d.sharp_plus/1797609IN_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 24 | 3.668 | 11.142 | 7.428 | [^18] |
| <img src="preview/d.sharp_plus/20304_skel.png" width="120"/> | [20304_skel](preview/d.sharp_plus/20304_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 928 | 2.790 | 1.860 | [^3] |
| <img src="preview/d.sharp_plus/21362_skel.png" width="120"/> | [21362_skel](preview/d.sharp_plus/21362_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 64 | 1.828 | 5.862 | 3.908 | [^3] |
| <img src="preview/d.sharp_plus/21747_skel.png" width="120"/> | [21747_skel](preview/d.sharp_plus/21747_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 2.918 | 8.766 | 5.844 | [^3] |
| <img src="preview/d.sharp_plus/22081_skel.png" width="120"/> | [22081_skel](preview/d.sharp_plus/22081_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 3.970 | 11.934 | 7.956 | [^3] |
| <img src="preview/d.sharp_plus/22290_skel.png" width="120"/> | [22290_skel](preview/d.sharp_plus/22290_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 944 | 2.832 | 1.888 | [^3] |
| <img src="preview/d.sharp_plus/22601_skel.png" width="120"/> | [22601_skel](preview/d.sharp_plus/22601_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 8 | 12.554 | 37.704 | 25.136 | [^3] |
| <img src="preview/d.sharp_plus/22669_skel.png" width="120"/> | [22669_skel](preview/d.sharp_plus/22669_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 28.577 | 85.731 | 57.154 | [^3] (repaired) |
| <img src="preview/d.sharp_plus/22711_skel.png" width="120"/> | [22711_skel](preview/d.sharp_plus/22711_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 2.820 | 8.460 | 5.640 | [^3] |
| <img src="preview/d.sharp_plus/22808_skel.png" width="120"/> | [22808_skel](preview/d.sharp_plus/22808_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 9.640 | 28.920 | 19.280 | [^3] |
| <img src="preview/d.sharp_plus/2473396_esb.png" width="120"/> | [2473396_esb](preview/d.sharp_plus/2473396_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 11 | 1.445 | 4.395 | 2.930 | [^18] |
| <img src="preview/d.sharp_plus/2568b_esb.png" width="120"/> | [2568b_esb](preview/d.sharp_plus/2568b_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 894 | 2.688 | 1.792 | [^18] |
| <img src="preview/d.sharp_plus/48tooth-sprocket_esb.png" width="120"/> | [48tooth-sprocket_esb](preview/d.sharp_plus/48tooth-sprocket_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 988 | 3.012 | 2.008 | [^18] |
| <img src="preview/d.sharp_plus/53757_thingi.png" width="120"/> | [53757_thingi](preview/d.sharp_plus/53757_thingi.stl) | 8 | 240 | 762 | 508 | [^2] |
| <img src="preview/d.sharp_plus/54teeth2_esb.png" width="120"/> | [54teeth2_esb](preview/d.sharp_plus/54teeth2_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 148 | 444 | 296 | [^18] |
| <img src="preview/d.sharp_plus/a-arm2_esb.png" width="120"/> | [a-arm2_esb](preview/d.sharp_plus/a-arm2_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 212 | 684 | 456 | [^18] |
| <img src="preview/d.sharp_plus/advgr01_esb.png" width="120"/> | [advgr01_esb](preview/d.sharp_plus/advgr01_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 813 | 2.439 | 1.626 | [^18] |
| <img src="preview/d.sharp_plus/anc101_gao.png" width="120"/> | [anc101_gao](preview/d.sharp_plus/anc101_gao.stl) | 5 | 3.970 | 11.934 | 7.956 | [^4] |
| <img src="preview/d.sharp_plus/anc_101_a1_quadwild.png" width="120"/> | [anc_101_a1_quadwild](preview/d.sharp_plus/anc_101_a1_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 58.952 | 176.880 | 117.920 | [^1] |
| <img src="preview/d.sharp_plus/anti_backlash_nut_quadwild.png" width="120"/> | [anti_backlash_nut_quadwild](preview/d.sharp_plus/anti_backlash_nut_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 6.388 | 19.176 | 12.784 | [^1] |
| <img src="preview/d.sharp_plus/aries155_1_gao.png" width="120"/> | [aries155_1_gao](preview/d.sharp_plus/aries155_1_gao.stl) | 6 | 2.336 | 7.038 | 4.692 | [^4] |
| <img src="preview/d.sharp_plus/aries63_esb.png" width="120"/> | [aries63_esb](preview/d.sharp_plus/aries63_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 2.187 | 6.579 | 4.386 | [^18] |
| <img src="preview/d.sharp_plus/arm_group17_esb.png" width="120"/> | [arm_group17_esb](preview/d.sharp_plus/arm_group17_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 852 | 2.556 | 1.704 | [^18] |
| <img src="preview/d.sharp_plus/asm007_quadwild.png" width="120"/> | [asm007_quadwild](preview/d.sharp_plus/asm007_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 10.019 | 30.063 | 20.042 | [^1] |
| <img src="preview/d.sharp_plus/Asm11_esb.png" width="120"/> | [Asm11_esb](preview/d.sharp_plus/Asm11_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 2.159 | 6.483 | 4.322 | [^18] |
| <img src="preview/d.sharp_plus/assem_catch_esb.png" width="120"/> | [assem_catch_esb](preview/d.sharp_plus/assem_catch_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 108 | 324 | 216 | [^18] |
| <img src="preview/d.sharp_plus/atlanta2422220_esb.png" width="120"/> | [atlanta2422220_esb](preview/d.sharp_plus/atlanta2422220_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 1.034 | 3.102 | 2.068 | [^18] |
| <img src="preview/d.sharp_plus/B10_mambo.png" width="120"/> | [B10_mambo](preview/d.sharp_plus/B10_mambo.stl) | 1 | 1.506 | 4.518 | 3.012 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B13_mambo.png" width="120"/> | [B13_mambo](preview/d.sharp_plus/B13_mambo.stl) | 1 | 2.065 | 6.195 | 4.130 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B1_mambo.png" width="120"/> | [B1_mambo](preview/d.sharp_plus/B1_mambo.stl) | 1 | 1.741 | 5.223 | 3.482 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B28_mambo.png" width="120"/> | [B28_mambo](preview/d.sharp_plus/B28_mambo.stl) | 1 | 1.128 | 3.384 | 2.256 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B29_mambo.png" width="120"/> | [B29_mambo](preview/d.sharp_plus/B29_mambo.stl) | 1 | 1.941 | 5.823 | 3.882 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B31_mambo.png" width="120"/> | [B31_mambo](preview/d.sharp_plus/B31_mambo.stl) | 1 | 1.317 | 3.951 | 2.634 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B32_mambo.png" width="120"/> | [B32_mambo](preview/d.sharp_plus/B32_mambo.stl) | 1 | 1.364 | 4.092 | 2.728 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B33_mambo.png" width="120"/> | [B33_mambo](preview/d.sharp_plus/B33_mambo.stl) | 1 | 2.268 | 6.804 | 4.536 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B3_mambo.png" width="120"/> | [B3_mambo](preview/d.sharp_plus/B3_mambo.stl) | 2 | 3.495 | 10.491 | 6.994 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B44_mambo.png" width="120"/> | [B44_mambo](preview/d.sharp_plus/B44_mambo.stl) | 1 | 2.265 | 6.795 | 4.530 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B47_mambo.png" width="120"/> | [B47_mambo](preview/d.sharp_plus/B47_mambo.stl) | 1 | 2.161 | 6.483 | 4.322 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B51_mambo.png" width="120"/> | [B51_mambo](preview/d.sharp_plus/B51_mambo.stl) | 1 | 1.169 | 3.507 | 2.338 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B53_mambo.png" width="120"/> | [B53_mambo](preview/d.sharp_plus/B53_mambo.stl) | 1 | 984 | 2.952 | 1.968 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B55_mambo.png" width="120"/> | [B55_mambo](preview/d.sharp_plus/B55_mambo.stl) | 1 | 802 | 2.406 | 1.604 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B62_mambo.png" width="120"/> | [B62_mambo](preview/d.sharp_plus/B62_mambo.stl) | 1 | 1.016 | 3.048 | 2.032 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B63_mambo.png" width="120"/> | [B63_mambo](preview/d.sharp_plus/B63_mambo.stl) | 1 | 990 | 2.970 | 1.980 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B64_mambo.png" width="120"/> | [B64_mambo](preview/d.sharp_plus/B64_mambo.stl) | 1 | 852 | 2.556 | 1.704 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B65_mambo.png" width="120"/> | [B65_mambo](preview/d.sharp_plus/B65_mambo.stl) | 1 | 936 | 2.808 | 1.872 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B66_mambo.png" width="120"/> | [B66_mambo](preview/d.sharp_plus/B66_mambo.stl) | 2 | 1.159 | 3.483 | 2.322 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/B73_mambo.png" width="120"/> | [B73_mambo](preview/d.sharp_plus/B73_mambo.stl) | 1 | 2.320 | 6.960 | 4.640 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/back_plate_esb.png" width="120"/> | [back_plate_esb](preview/d.sharp_plus/back_plate_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 278 | 834 | 556 | [^18] |
| <img src="preview/d.sharp_plus/backdoor_esb.png" width="120"/> | [backdoor_esb](preview/d.sharp_plus/backdoor_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 1.368 | 4.104 | 2.736 | [^18] |
| <img src="preview/d.sharp_plus/bamboo_pen_quadwild.png" width="120"/> | [bamboo_pen_quadwild](preview/d.sharp_plus/bamboo_pen_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 8 | 17.832 | 53.538 | 35.692 | [^1] |
| <img src="preview/d.sharp_plus/bearing_208_esb.png" width="120"/> | [bearing_208_esb](preview/d.sharp_plus/bearing_208_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 310 | 930 | 620 | [^18] |
| <img src="preview/d.sharp_plus/bearing_plate_loopy.png" width="120"/> | [bearing_plate_loopy](preview/d.sharp_plus/bearing_plate_loopy.stl) | 5 | 4.907 | 14.745 | 9.830 | [^9] |
| <img src="preview/d.sharp_plus/BendTube_quadwild.png" width="120"/> | [BendTube_quadwild](preview/d.sharp_plus/BendTube_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 2.843 | 8.535 | 5.690 | [^1] |
| <img src="preview/d.sharp_plus/beveled_shoulder_2_loopy.png" width="120"/> | [beveled_shoulder_2_loopy](preview/d.sharp_plus/beveled_shoulder_2_loopy.stl) | 1 | 22 | 66 | 44 | [^9] |
| <img src="preview/d.sharp_plus/blech_quadwild.png" width="120"/> | [blech_quadwild](preview/d.sharp_plus/blech_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 26.100 | 78.324 | 52.216 | [^1] |
| <img src="preview/d.sharp_plus/block_gao.png" width="120"/> | [block_gao](preview/d.sharp_plus/block_gao.stl) | 3 | 8.052 | 24.168 | 16.112 | [^4] |
| <img src="preview/d.sharp_plus/blockLP_quadwild.png" width="120"/> | [blockLP_quadwild](preview/d.sharp_plus/blockLP_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 2.032 | 6.108 | 4.072 | [^1] |
| <img src="preview/d.sharp_plus/bolt_loopy.png" width="120"/> | [bolt_loopy](preview/d.sharp_plus/bolt_loopy.stl) | 1 | 4.752 | 14.256 | 9.504 | [^9] |
| <img src="preview/d.sharp_plus/BOOT_esb.png" width="120"/> | [BOOT_esb](preview/d.sharp_plus/BOOT_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 13.775 | 41.325 | 27.550 | [^18] |
| <img src="preview/d.sharp_plus/bracket2-Part_gao.png" width="120"/> | [bracket2-Part_gao](preview/d.sharp_plus/bracket2-Part_gao.stl) | 3 | 1.328 | 3.996 | 2.664 | [^4] |
| <img src="preview/d.sharp_plus/BracketInches_loopy.png" width="120"/> | [BracketInches_loopy](preview/d.sharp_plus/BracketInches_loopy.stl) | 6 | 8.301 | 24.933 | 16.622 | [^9] |
| <img src="preview/d.sharp_plus/c25d-flowthru-geom-v1-mm_nasa.png" width="120"/> | [c25d-flowthru-geom-v1-mm_nasa](preview/d.sharp_plus/c25d-flowthru-geom-v1-mm_nasa.stl) | 1 | 32.818 | 98.454 | 65.636 | [^23] (meshed) |
| <img src="preview/d.sharp_plus/cad5-tri_quadwild.png" width="120"/> | [cad5-tri_quadwild](preview/d.sharp_plus/cad5-tri_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 18.664 | 56.004 | 37.336 | [^1] |
| <img src="preview/d.sharp_plus/cami1_gao.png" width="120"/> | [cami1_gao](preview/d.sharp_plus/cami1_gao.stl) | 5 | 1.210 | 3.654 | 2.436 | [^4] |
| <img src="preview/d.sharp_plus/cami2_gao.png" width="120"/> | [cami2_gao](preview/d.sharp_plus/cami2_gao.stl) | 1 | 654 | 1.962 | 1.308 | [^4] |
| <img src="preview/d.sharp_plus/cap_thing_quadwild.png" width="120"/> | [cap_thing_quadwild](preview/d.sharp_plus/cap_thing_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 28.806 | 86.424 | 57.616 | [^1] |
| <img src="preview/d.sharp_plus/carter_gao.png" width="120"/> | [carter_gao](preview/d.sharp_plus/carter_gao.stl) | 7 | 67.436 | 202.344 | 134.896 | [^4] |
| <img src="preview/d.sharp_plus/casting2_quadwild.png" width="120"/> | [casting2_quadwild](preview/d.sharp_plus/casting2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 9.513 | 28.587 | 19.058 | [^1] |
| <img src="preview/d.sharp_plus/casting_gao.png" width="120"/> | [casting_gao](preview/d.sharp_plus/casting_gao.stl) | 9 | 26.034 | 78.150 | 52.100 | [^4] |
| <img src="preview/d.sharp_plus/center_link_esb.png" width="120"/> | [center_link_esb](preview/d.sharp_plus/center_link_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 2.534 | 7.602 | 5.068 | [^18] |
| <img src="preview/d.sharp_plus/cheese2_gao.png" width="120"/> | [cheese2_gao](preview/d.sharp_plus/cheese2_gao.stl) | 28 | 4.776 | 14.490 | 9.660 | [^4] |
| <img src="preview/d.sharp_plus/cheese3_gao.png" width="120"/> | [cheese3_gao](preview/d.sharp_plus/cheese3_gao.stl) | 81 | 14.156 | 42.948 | 28.632 | [^4] |
| <img src="preview/d.sharp_plus/cheese_gao.png" width="120"/> | [cheese_gao](preview/d.sharp_plus/cheese_gao.stl) | 176 | 31.240 | 94.770 | 63.180 | [^4] |
| <img src="preview/d.sharp_plus/cimplex_gao.png" width="120"/> | [cimplex_gao](preview/d.sharp_plus/cimplex_gao.stl) | 6 | 14.806 | 44.448 | 29.632 | [^4] |
| <img src="preview/d.sharp_plus/CLAMP_FINGER_esb.png" width="120"/> | [CLAMP_FINGER_esb](preview/d.sharp_plus/CLAMP_FINGER_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 786 | 2.406 | 1.604 | [^18] |
| <img src="preview/d.sharp_plus/clamp_quadwild.png" width="120"/> | [clamp_quadwild](preview/d.sharp_plus/clamp_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 27.186 | 81.570 | 54.380 | [^1] |
| <img src="preview/d.sharp_plus/clevis23_gao.png" width="120"/> | [clevis23_gao](preview/d.sharp_plus/clevis23_gao.stl) | 9 | 2.478 | 7.482 | 4.988 | [^4] |
| <img src="preview/d.sharp_plus/cognit_quadwild.png" width="120"/> | [cognit_quadwild](preview/d.sharp_plus/cognit_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 10 | 44.657 | 134.025 | 89.350 | [^1] |
| <img src="preview/d.sharp_plus/CoverSlipCleaningHolder2b_quadwild.png" width="120"/> | [CoverSlipCleaningHolder2b_quadwild](preview/d.sharp_plus/CoverSlipCleaningHolder2b_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 51 | 12.653 | 38.259 | 25.506 | [^1] |
| <img src="preview/d.sharp_plus/datatech_2_quadwild.png" width="120"/> | [datatech_2_quadwild](preview/d.sharp_plus/datatech_2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 7 | 65.466 | 196.434 | 130.956 | [^1] |
| <img src="preview/d.sharp_plus/deckel_gao.png" width="120"/> | [deckel_gao](preview/d.sharp_plus/deckel_gao.stl) | 4 | 20.018 | 60.072 | 40.048 | [^4] |
| <img src="preview/d.sharp_plus/deckel_loopy.png" width="120"/> | [deckel_loopy](preview/d.sharp_plus/deckel_loopy.stl) | 4 | 5.000 | 15.018 | 10.012 | [^9] |
| <img src="preview/d.sharp_plus/delta_arm2_remesh_quadwild.png" width="120"/> | [delta_arm2_remesh_quadwild](preview/d.sharp_plus/delta_arm2_remesh_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 48.668 | 146.022 | 97.348 | [^1] |
| <img src="preview/d.sharp_plus/delta_arm_base_quadwild.png" width="120"/> | [delta_arm_base_quadwild](preview/d.sharp_plus/delta_arm_base_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 7 | 18.641 | 55.959 | 37.306 | [^1] |
| <img src="preview/d.sharp_plus/delta_arm_end_effector_remesh_quadwild.png" width="120"/> | [delta_arm_end_effector_remesh_quadwild](preview/d.sharp_plus/delta_arm_end_effector_remesh_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 4 | 16.543 | 49.647 | 33.098 | [^1] |
| <img src="preview/d.sharp_plus/DEMO_REF_esb.png" width="120"/> | [DEMO_REF_esb](preview/d.sharp_plus/DEMO_REF_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 7.045 | 21.135 | 14.090 | [^18] |
| <img src="preview/d.sharp_plus/des6_loopy.png" width="120"/> | [des6_loopy](preview/d.sharp_plus/des6_loopy.stl) | 1 | 5.695 | 17.085 | 11.390 | [^9] |
| <img src="preview/d.sharp_plus/des7_quadwild.png" width="120"/> | [des7_quadwild](preview/d.sharp_plus/des7_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 11.061 | 33.189 | 22.126 | [^1] |
| <img src="preview/d.sharp_plus/din444_esb.png" width="120"/> | [din444_esb](preview/d.sharp_plus/din444_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 1.030 | 3.090 | 2.060 | [^18] |
| <img src="preview/d.sharp_plus/disk_esb.png" width="120"/> | [disk_esb](preview/d.sharp_plus/disk_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 676 | 2.034 | 1.356 | [^18] |
| <img src="preview/d.sharp_plus/dpw6g1_nlr.png" width="120"/> | [dpw6g1_nlr](preview/d.sharp_plus/dpw6g1_nlr.stl) | 1 | 31.591 | 94.773 | 63.182 | [^20] (meshed by Stevie-Ray Janssen) |
| <img src="preview/d.sharp_plus/EXTSUPPORT1_esb.png" width="120"/> | [EXTSUPPORT1_esb](preview/d.sharp_plus/EXTSUPPORT1_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 216 | 648 | 432 | [^18] |
| <img src="preview/d.sharp_plus/fender-gearbox2-left_esb.png" width="120"/> | [fender-gearbox2-left_esb](preview/d.sharp_plus/fender-gearbox2-left_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 7 | 1.336 | 4.044 | 2.696 | [^18] |
| <img src="preview/d.sharp_plus/freihand_quadwild.png" width="120"/> | [freihand_quadwild](preview/d.sharp_plus/freihand_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 48.514 | 145.542 | 97.028 | [^1] |
| <img src="preview/d.sharp_plus/ftc10_nist.png" width="120"/> | [ftc10_nist](preview/d.sharp_plus/ftc10_nist.stl) | 22 | 106.281 | 318.969 | 212.646 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/fusee_Lp_quadwild.png" width="120"/> | [fusee_Lp_quadwild](preview/d.sharp_plus/fusee_Lp_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 18 | 30.868 | 92.706 | 61.804 | [^1] |
| <img src="preview/d.sharp_plus/ganter_din_6330_esb.png" width="120"/> | [ganter_din_6330_esb](preview/d.sharp_plus/ganter_din_6330_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 1.251 | 3.753 | 2.502 | [^18] |
| <img src="preview/d.sharp_plus/gear_2_quadwild.png" width="120"/> | [gear_2_quadwild](preview/d.sharp_plus/gear_2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 10.976 | 32.928 | 21.952 | [^1] |
| <img src="preview/d.sharp_plus/gearbox_quadwild.png" width="120"/> | [gearbox_quadwild](preview/d.sharp_plus/gearbox_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 78 | 64.149 | 192.909 | 128.606 | [^1] |
| <img src="preview/d.sharp_plus/gehaeuse_gao.png" width="120"/> | [gehaeuse_gao](preview/d.sharp_plus/gehaeuse_gao.stl) | 3 | 4.241 | 12.735 | 8.490 | [^4] |
| <img src="preview/d.sharp_plus/gerwah_peter_dxk1501_esb.png" width="120"/> | [gerwah_peter_dxk1501_esb](preview/d.sharp_plus/gerwah_peter_dxk1501_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 374 | 1.128 | 752 | [^18] |
| <img src="preview/d.sharp_plus/gimbal_1_gao.png" width="120"/> | [gimbal_1_gao](preview/d.sharp_plus/gimbal_1_gao.stl) | 5 | 838 | 2.538 | 1.692 | [^4] |
| <img src="preview/d.sharp_plus/gps_25_cut_quadwild.png" width="120"/> | [gps_25_cut_quadwild](preview/d.sharp_plus/gps_25_cut_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 26.980 | 80.946 | 53.964 | [^1] |
| <img src="preview/d.sharp_plus/groschopp_IGK65-40-2pole_esb.png" width="120"/> | [groschopp_IGK65-40-2pole_esb](preview/d.sharp_plus/groschopp_IGK65-40-2pole_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 6 | 10.274 | 30.852 | 20.568 | [^18] (repaired) |
| <img src="preview/d.sharp_plus/gyroidpuzzle_loopy.png" width="120"/> | [gyroidpuzzle_loopy](preview/d.sharp_plus/gyroidpuzzle_loopy.stl) | 15 | 13.077 | 39.315 | 26.210 | [^9] |
| <img src="preview/d.sharp_plus/hanger_gao.png" width="120"/> | [hanger_gao](preview/d.sharp_plus/hanger_gao.stl) | 2 | 16.110 | 48.336 | 32.224 | [^4] |
| <img src="preview/d.sharp_plus/hanger_loopy.png" width="120"/> | [hanger_loopy](preview/d.sharp_plus/hanger_loopy.stl) | 2 | 4.026 | 12.084 | 8.056 | [^9] |
| <img src="preview/d.sharp_plus/helmet_quadwild.png" width="120"/> | [helmet_quadwild](preview/d.sharp_plus/helmet_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 496 | 1.500 | 1.000 | [^1] |
| <img src="preview/d.sharp_plus/heptoroid100k_quadwild.png" width="120"/> | [heptoroid100k_quadwild](preview/d.sharp_plus/heptoroid100k_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 22 | 49.958 | 150.000 | 100.000 | [^1] |
| <img src="preview/d.sharp_plus/hinge_loopy.png" width="120"/> | [hinge_loopy](preview/d.sharp_plus/hinge_loopy.stl) | 5 | 9.544 | 28.656 | 19.104 | [^9] |
| <img src="preview/d.sharp_plus/hip_quadwild.png" width="120"/> | [hip_quadwild](preview/d.sharp_plus/hip_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 48.104 | 144.318 | 96.212 | [^1] |
| <img src="preview/d.sharp_plus/holes10_1_gao.png" width="120"/> | [holes10_1_gao](preview/d.sharp_plus/holes10_1_gao.stl) | 100 | 4.808 | 15.018 | 10.012 | [^4] |
| <img src="preview/d.sharp_plus/hub2_quadwild.png" width="120"/> | [hub2_quadwild](preview/d.sharp_plus/hub2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 6 | 21.211 | 63.663 | 42.442 | [^1] |
| <img src="preview/d.sharp_plus/Hub_quadwild.png" width="120"/> | [Hub_quadwild](preview/d.sharp_plus/Hub_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 21 | 6.450 | 19.470 | 12.980 | [^1] |
| <img src="preview/d.sharp_plus/i10o_simp_hexme.png" width="120"/> | [i10o_simp_hexme](preview/d.sharp_plus/i10o_simp_hexme.stl) | 1 | 5.024 | 15.072 | 10.048 | [^24] (meshed) |
| <img src="preview/d.sharp_plus/impeller_housing_1_gao.png" width="120"/> | [impeller_housing_1_gao](preview/d.sharp_plus/impeller_housing_1_gao.stl) | 1 | 1.024 | 3.072 | 2.048 | [^4] |
| <img src="preview/d.sharp_plus/impeller_loopy.png" width="120"/> | [impeller_loopy](preview/d.sharp_plus/impeller_loopy.stl) | 1 | 13.063 | 39.189 | 26.126 | [^9] |
| <img src="preview/d.sharp_plus/In_Green_Company_Surface_Saver_Ring_10_Terra_Cotta_gso.png" width="120"/> | [In_Green_Company_Surface_Saver_Ring_10_Terra_Cotta_gso](preview/d.sharp_plus/In_Green_Company_Surface_Saver_Ring_10_Terra_Cotta_gso.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 9.136 | 27.408 | 18.272 | [^6] |
| <img src="preview/d.sharp_plus/joint_gao.png" width="120"/> | [joint_gao](preview/d.sharp_plus/joint_gao.stl) | 2 | 8.014 | 24.048 | 16.032 | [^4] |
| <img src="preview/d.sharp_plus/joint_loopy.png" width="120"/> | [joint_loopy](preview/d.sharp_plus/joint_loopy.stl) | 2 | 4.381 | 13.149 | 8.766 | [^9] |
| <img src="preview/d.sharp_plus/knob_loopy.png" width="120"/> | [knob_loopy](preview/d.sharp_plus/knob_loopy.stl) | 1 | 6.908 | 20.724 | 13.816 | [^9] |
| <img src="preview/d.sharp_plus/lever_arm_loopy.png" width="120"/> | [lever_arm_loopy](preview/d.sharp_plus/lever_arm_loopy.stl) | 2 | 4.028 | 12.090 | 8.060 | [^9] |
| <img src="preview/d.sharp_plus/lock_gao.png" width="120"/> | [lock_gao](preview/d.sharp_plus/lock_gao.stl) | 3 | 85.084 | 255.264 | 170.176 | [^4] |
| <img src="preview/d.sharp_plus/LowerControlArm_quadwild.png" width="120"/> | [LowerControlArm_quadwild](preview/d.sharp_plus/LowerControlArm_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 3 | 9.317 | 27.963 | 18.642 | [^1] |
| <img src="preview/d.sharp_plus/M1_mambo.png" width="120"/> | [M1_mambo](preview/d.sharp_plus/M1_mambo.stl) | 9 | 52.248 | 156.792 | 104.528 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/M2_mambo.png" width="120"/> | [M2_mambo](preview/d.sharp_plus/M2_mambo.stl) | 3 | 4.268 | 12.816 | 8.544 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/M3_mambo.png" width="120"/> | [M3_mambo](preview/d.sharp_plus/M3_mambo.stl) | 5 | 74.796 | 224.412 | 149.608 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/M4_mambo.png" width="120"/> | [M4_mambo](preview/d.sharp_plus/M4_mambo.stl) | 3 | 31.868 | 95.616 | 63.744 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/M5_mambo.png" width="120"/> | [M5_mambo](preview/d.sharp_plus/M5_mambo.stl) | 7 | 57.780 | 173.376 | 115.584 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/M6_mambo.png" width="120"/> | [M6_mambo](preview/d.sharp_plus/M6_mambo.stl) | 4 | 54.507 | 163.539 | 109.026 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/M8_mambo.png" width="120"/> | [M8_mambo](preview/d.sharp_plus/M8_mambo.stl) | 1 | 146.305 | 438.915 | 292.610 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/M9_mambo.png" width="120"/> | [M9_mambo](preview/d.sharp_plus/M9_mambo.stl) | 5 | 67.770 | 203.334 | 135.556 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/mazewheel_quadwild.png" width="120"/> | [mazewheel_quadwild](preview/d.sharp_plus/mazewheel_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 16 | 13.607 | 40.911 | 27.274 | [^1] |
| <img src="preview/d.sharp_plus/mech09_quadwild.png" width="120"/> | [mech09_quadwild](preview/d.sharp_plus/mech09_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 4.045 | 12.141 | 8.094 | [^1] |
| <img src="preview/d.sharp_plus/mechanical01_quadwild.png" width="120"/> | [mechanical01_quadwild](preview/d.sharp_plus/mechanical01_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 17 | 22.900 | 68.796 | 45.864 | [^1] |
| <img src="preview/d.sharp_plus/mechanical03_quadwild.png" width="120"/> | [mechanical03_quadwild](preview/d.sharp_plus/mechanical03_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 2 | 2.210 | 6.636 | 4.424 | [^1] |
| <img src="preview/d.sharp_plus/mechanical06_loopy.png" width="120"/> | [mechanical06_loopy](preview/d.sharp_plus/mechanical06_loopy.stl) | 1 | 4.545 | 13.635 | 9.090 | [^9] |
| <img src="preview/d.sharp_plus/mechanical08_loopy.png" width="120"/> | [mechanical08_loopy](preview/d.sharp_plus/mechanical08_loopy.stl) | 1 | 1.464 | 4.392 | 2.928 | [^9] |
| <img src="preview/d.sharp_plus/metatron_loopy.png" width="120"/> | [metatron_loopy](preview/d.sharp_plus/metatron_loopy.stl) | 11 | 7.171 | 21.573 | 14.382 | [^9] |
| <img src="preview/d.sharp_plus/mid2Fem_quadwild.png" width="120"/> | [mid2Fem_quadwild](preview/d.sharp_plus/mid2Fem_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 8.868 | 26.628 | 17.752 | [^1] |
| <img src="preview/d.sharp_plus/mnf07HeadFem_quadwild.png" width="120"/> | [mnf07HeadFem_quadwild](preview/d.sharp_plus/mnf07HeadFem_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 18.908 | 56.772 | 37.848 | [^1] |
| <img src="preview/d.sharp_plus/motor_tail_loopy.png" width="120"/> | [motor_tail_loopy](preview/d.sharp_plus/motor_tail_loopy.stl) | 13 | 7.600 | 22.872 | 15.248 | [^9] |
| <img src="preview/d.sharp_plus/mount_quadwild.png" width="120"/> | [mount_quadwild](preview/d.sharp_plus/mount_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 2.715 | 8.169 | 5.446 | [^1] |
| <img src="preview/d.sharp_plus/n05o_box_min_pcyls_hexme.png" width="120"/> | [n05o_box_min_pcyls_hexme](preview/d.sharp_plus/n05o_box_min_pcyls_hexme.stl) | 1 | 1.122 | 3.366 | 2.244 | [^24] (meshed) |
| <img src="preview/d.sharp_plus/n11o_limit_cycle_hexme.png" width="120"/> | [n11o_limit_cycle_hexme](preview/d.sharp_plus/n11o_limit_cycle_hexme.stl) | 1 | 8.413 | 25.239 | 16.826 | [^24] (meshed) |
| <img src="preview/d.sharp_plus/nasty_cheese-tri_quadwild.png" width="120"/> | [nasty_cheese-tri_quadwild](preview/d.sharp_plus/nasty_cheese-tri_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 133 | 194.722 | 584.958 | 389.972 | [^1] |
| <img src="preview/d.sharp_plus/nasty_cheese2_quadwild.png" width="120"/> | [nasty_cheese2_quadwild](preview/d.sharp_plus/nasty_cheese2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 133 | 30.062 | 90.978 | 60.652 | [^1] |
| <img src="preview/d.sharp_plus/nautilus-20k-closed-tri_quadwild.png" width="120"/> | [nautilus-20k-closed-tri_quadwild](preview/d.sharp_plus/nautilus-20k-closed-tri_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 7 | 25.207 | 75.657 | 50.438 | [^1] |
| <img src="preview/d.sharp_plus/nist_ctc_01_asme1_rd_nist.png" width="120"/> | [nist_ctc_01_asme1_rd_nist](preview/d.sharp_plus/nist_ctc_01_asme1_rd_nist.stl) | 10 | 24.141 | 72.477 | 48.318 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/nist_ctc_03_asme1_rc_nist.png" width="120"/> | [nist_ctc_03_asme1_rc_nist](preview/d.sharp_plus/nist_ctc_03_asme1_rc_nist.stl) | 17 | 39.785 | 119.451 | 79.634 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/nist_ftc_06_asme1_rd_nist.png" width="120"/> | [nist_ftc_06_asme1_rd_nist](preview/d.sharp_plus/nist_ftc_06_asme1_rd_nist.stl) | 10 | 69.446 | 208.392 | 138.928 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/nist_ftc_07_asme1_rd_nist.png" width="120"/> | [nist_ftc_07_asme1_rd_nist](preview/d.sharp_plus/nist_ftc_07_asme1_rd_nist.stl) | 15 | 258.863 | 776.673 | 517.782 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/nist_ftc_08_asme1_rc_nist.png" width="120"/> | [nist_ftc_08_asme1_rc_nist](preview/d.sharp_plus/nist_ftc_08_asme1_rc_nist.stl) | 25 | 167.330 | 502.134 | 334.756 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/nist_ftc_09_asme1_rd_nist.png" width="120"/> | [nist_ftc_09_asme1_rd_nist](preview/d.sharp_plus/nist_ftc_09_asme1_rd_nist.stl) | 34 | 41.888 | 125.862 | 83.908 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/nist_ftc_11_asme1_rb_nist.png" width="120"/> | [nist_ftc_11_asme1_rb_nist](preview/d.sharp_plus/nist_ftc_11_asme1_rb_nist.stl) | 1 | 13.533 | 40.599 | 27.066 | [^25] (meshed) |
| <img src="preview/d.sharp_plus/nut_refine_tet_surf_quadwild.png" width="120"/> | [nut_refine_tet_surf_quadwild](preview/d.sharp_plus/nut_refine_tet_surf_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 24.243 | 72.729 | 48.486 | [^1] |
| <img src="preview/d.sharp_plus/Orion_Capsule_no_fbc_nasa.png" width="120"/> | [Orion_Capsule_no_fbc_nasa](preview/d.sharp_plus/Orion_Capsule_no_fbc_nasa.stl) | 7 | 25.852 | 77.592 | 51.728 | [^26] (repaired) |
| <img src="preview/d.sharp_plus/part10_gao.png" width="120"/> | [part10_gao](preview/d.sharp_plus/part10_gao.stl) | 3 | 1.288 | 3.876 | 2.584 | [^4] |
| <img src="preview/d.sharp_plus/part11_gao.png" width="120"/> | [part11_gao](preview/d.sharp_plus/part11_gao.stl) | 6 | 4.530 | 13.620 | 9.080 | [^4] |
| <img src="preview/d.sharp_plus/part2_quadwild.png" width="120"/> | [part2_quadwild](preview/d.sharp_plus/part2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 8 | 5.341 | 16.065 | 10.710 | [^1] |
| <img src="preview/d.sharp_plus/part_gao.png" width="120"/> | [part_gao](preview/d.sharp_plus/part_gao.stl) | 3 | 17.056 | 51.180 | 34.120 | [^4] |
| <img src="preview/d.sharp_plus/pinion_1_gao.png" width="120"/> | [pinion_1_gao](preview/d.sharp_plus/pinion_1_gao.stl) | 1 | 1.298 | 3.894 | 2.596 | [^4] |
| <img src="preview/d.sharp_plus/pinion_loopy.png" width="120"/> | [pinion_loopy](preview/d.sharp_plus/pinion_loopy.stl) | 1 | 21.439 | 64.317 | 42.878 | [^9] |
| <img src="preview/d.sharp_plus/pipe_skel.png" width="120"/> | [pipe_skel](preview/d.sharp_plus/pipe_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 2.820 | 8.460 | 5.640 | [^3] |
| <img src="preview/d.sharp_plus/plate_Lp-tri_quadwild.png" width="120"/> | [plate_Lp-tri_quadwild](preview/d.sharp_plus/plate_Lp-tri_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 45.674 | 137.070 | 91.380 | [^1] |
| <img src="preview/d.sharp_plus/plate_lp_mid_quadwild.png" width="120"/> | [plate_lp_mid_quadwild](preview/d.sharp_plus/plate_lp_mid_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 39.233 | 117.747 | 78.498 | [^1] |
| <img src="preview/d.sharp_plus/pulley100K_quadwild.png" width="120"/> | [pulley100K_quadwild](preview/d.sharp_plus/pulley100K_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 50.000 | 150.000 | 100.000 | [^1] |
| <img src="preview/d.sharp_plus/pump_2_quadwild.png" width="120"/> | [pump_2_quadwild](preview/d.sharp_plus/pump_2_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 6 | 41.888 | 125.694 | 83.796 | [^1] |
| <img src="preview/d.sharp_plus/pump_quadwild.png" width="120"/> | [pump_quadwild](preview/d.sharp_plus/pump_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 10 | 10.318 | 31.008 | 20.672 | [^1] |
| <img src="preview/d.sharp_plus/rocker-arm_jacobson.png" width="120"/> | [rocker-arm_jacobson](preview/d.sharp_plus/rocker-arm_jacobson.stl) | 1 | 10.044 | 30.132 | 20.088 | [^7] |
| <img src="preview/d.sharp_plus/rocker_gao.png" width="120"/> | [rocker_gao](preview/d.sharp_plus/rocker_gao.stl) | 1 | 26.656 | 79.968 | 53.312 | [^4] |
| <img src="preview/d.sharp_plus/rod_gao.png" width="120"/> | [rod_gao](preview/d.sharp_plus/rod_gao.stl) | 2 | 8.814 | 26.448 | 17.632 | [^4] |
| <img src="preview/d.sharp_plus/rod_loopy.png" width="120"/> | [rod_loopy](preview/d.sharp_plus/rod_loopy.stl) | 2 | 2.202 | 6.612 | 4.408 | [^9] |
| <img src="preview/d.sharp_plus/rolling_stage_gao.png" width="120"/> | [rolling_stage_gao](preview/d.sharp_plus/rolling_stage_gao.stl) | 7 | 15.387 | 46.197 | 30.798 | [^4] |
| <img src="preview/d.sharp_plus/rotor_skel.png" width="120"/> | [rotor_skel](preview/d.sharp_plus/rotor_skel.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 21 | 2.328 | 7.104 | 4.736 | [^3] |
| <img src="preview/d.sharp_plus/RotorHub_quadwild.png" width="120"/> | [RotorHub_quadwild](preview/d.sharp_plus/RotorHub_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 7 | 1.434 | 4.338 | 2.892 | [^1] |
| <img src="preview/d.sharp_plus/S0_mambo.png" width="120"/> | [S0_mambo](preview/d.sharp_plus/S0_mambo.stl) | 3 | 85.962 | 257.898 | 171.932 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S1_mambo.png" width="120"/> | [S1_mambo](preview/d.sharp_plus/S1_mambo.stl) | 3 | 60.440 | 181.332 | 120.888 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S20_mambo.png" width="120"/> | [S20_mambo](preview/d.sharp_plus/S20_mambo.stl) | 7 | 10.211 | 30.669 | 20.446 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S22_mambo.png" width="120"/> | [S22_mambo](preview/d.sharp_plus/S22_mambo.stl) | 3 | 42.465 | 127.407 | 84.938 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S23_mambo.png" width="120"/> | [S23_mambo](preview/d.sharp_plus/S23_mambo.stl) | 2 | 37.229 | 111.693 | 74.462 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S24_mambo.png" width="120"/> | [S24_mambo](preview/d.sharp_plus/S24_mambo.stl) | 3 | 59.706 | 179.130 | 119.420 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S25_mambo.png" width="120"/> | [S25_mambo](preview/d.sharp_plus/S25_mambo.stl) | 3 | 78.708 | 236.136 | 157.424 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S26_mambo.png" width="120"/> | [S26_mambo](preview/d.sharp_plus/S26_mambo.stl) | 4 | 107.960 | 323.898 | 215.932 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S27_mambo.png" width="120"/> | [S27_mambo](preview/d.sharp_plus/S27_mambo.stl) | 5 | 25.417 | 76.275 | 50.850 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S31_mambo.png" width="120"/> | [S31_mambo](preview/d.sharp_plus/S31_mambo.stl) | 7 | 13.704 | 41.148 | 27.432 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S33_mambo.png" width="120"/> | [S33_mambo](preview/d.sharp_plus/S33_mambo.stl) | 1 | 12.097 | 36.291 | 24.194 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S34_mambo.png" width="120"/> | [S34_mambo](preview/d.sharp_plus/S34_mambo.stl) | 3 | 51.472 | 154.428 | 102.952 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S35_mambo.png" width="120"/> | [S35_mambo](preview/d.sharp_plus/S35_mambo.stl) | 1 | 30.639 | 91.917 | 61.278 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S36_mambo.png" width="120"/> | [S36_mambo](preview/d.sharp_plus/S36_mambo.stl) | 1 | 126.068 | 378.204 | 252.136 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S38_mambo.png" width="120"/> | [S38_mambo](preview/d.sharp_plus/S38_mambo.stl) | 3 | 21.918 | 65.766 | 43.844 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S39_mambo.png" width="120"/> | [S39_mambo](preview/d.sharp_plus/S39_mambo.stl) | 2 | 23.428 | 70.290 | 46.860 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S3_mambo.png" width="120"/> | [S3_mambo](preview/d.sharp_plus/S3_mambo.stl) | 2 | 3.298 | 9.900 | 6.600 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S40_mambo.png" width="120"/> | [S40_mambo](preview/d.sharp_plus/S40_mambo.stl) | 1 | 37.574 | 112.722 | 75.148 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S41_mambo.png" width="120"/> | [S41_mambo](preview/d.sharp_plus/S41_mambo.stl) | 1 | 36.315 | 108.945 | 72.630 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S42_mambo.png" width="120"/> | [S42_mambo](preview/d.sharp_plus/S42_mambo.stl) | 1 | 35.625 | 106.875 | 71.250 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S43_mambo.png" width="120"/> | [S43_mambo](preview/d.sharp_plus/S43_mambo.stl) | 1 | 35.242 | 105.726 | 70.484 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S44_mambo.png" width="120"/> | [S44_mambo](preview/d.sharp_plus/S44_mambo.stl) | 1 | 35.363 | 106.089 | 70.726 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S45_mambo.png" width="120"/> | [S45_mambo](preview/d.sharp_plus/S45_mambo.stl) | 1 | 34.921 | 104.763 | 69.842 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S4_mambo.png" width="120"/> | [S4_mambo](preview/d.sharp_plus/S4_mambo.stl) | 3 | 31.644 | 94.944 | 63.296 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S5_mambo.png" width="120"/> | [S5_mambo](preview/d.sharp_plus/S5_mambo.stl) | 7 | 41.492 | 124.512 | 83.008 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S6_mambo.png" width="120"/> | [S6_mambo](preview/d.sharp_plus/S6_mambo.stl) | 5 | 68.976 | 206.952 | 137.968 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S7_mambo.png" width="120"/> | [S7_mambo](preview/d.sharp_plus/S7_mambo.stl) | 2 | 61.013 | 183.045 | 122.030 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S8_mambo.png" width="120"/> | [S8_mambo](preview/d.sharp_plus/S8_mambo.stl) | 1 | 48.998 | 146.994 | 97.996 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/S9_mambo.png" width="120"/> | [S9_mambo](preview/d.sharp_plus/S9_mambo.stl) | 3 | 281.281 | 843.855 | 562.570 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/s_bracket_1_gao.png" width="120"/> | [s_bracket_1_gao](preview/d.sharp_plus/s_bracket_1_gao.stl) | 2 | 1.300 | 3.906 | 2.604 | [^4] |
| <img src="preview/d.sharp_plus/schmersal_AZ-17-1_esb.png" width="120"/> | [schmersal_AZ-17-1_esb](preview/d.sharp_plus/schmersal_AZ-17-1_esb.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 923 | 2.793 | 1.862 | [^18] |
| <img src="preview/d.sharp_plus/sculpt_gao.png" width="120"/> | [sculpt_gao](preview/d.sharp_plus/sculpt_gao.stl) | 2 | 14.682 | 44.052 | 29.368 | [^4] |
| <img src="preview/d.sharp_plus/sculpt_loopy.png" width="120"/> | [sculpt_loopy](preview/d.sharp_plus/sculpt_loopy.stl) | 2 | 3.669 | 11.013 | 7.342 | [^9] |
| <img src="preview/d.sharp_plus/socket1-Part_gao.png" width="120"/> | [socket1-Part_gao](preview/d.sharp_plus/socket1-Part_gao.stl) | 7 | 1.194 | 3.618 | 2.412 | [^4] |
| <img src="preview/d.sharp_plus/socket2-Part_gao.png" width="120"/> | [socket2-Part_gao](preview/d.sharp_plus/socket2-Part_gao.stl) | 7 | 1.198 | 3.630 | 2.420 | [^4] |
| <img src="preview/d.sharp_plus/Space_Launch_System_SLS_Block_1_nasa.png" width="120"/> | [Space_Launch_System_SLS_Block_1_nasa](preview/d.sharp_plus/Space_Launch_System_SLS_Block_1_nasa.stl) | 7 | 29.988 | 90.000 | 60.000 | [^26] (repaired, simplified) |
| <img src="preview/d.sharp_plus/support_frame_1_gao.png" width="120"/> | [support_frame_1_gao](preview/d.sharp_plus/support_frame_1_gao.stl) | 5 | 554 | 1.686 | 1.124 | [^4] |
| <img src="preview/d.sharp_plus/switchmec_Lp_quadwild.png" width="120"/> | [switchmec_Lp_quadwild](preview/d.sharp_plus/switchmec_Lp_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 8 | 5.000 | 15.042 | 10.028 | [^1] |
| <img src="preview/d.sharp_plus/swivel2-Part_gao.png" width="120"/> | [swivel2-Part_gao](preview/d.sharp_plus/swivel2-Part_gao.stl) | 2 | 406 | 1.224 | 816 | [^4] |
| <img src="preview/d.sharp_plus/team2_gao.png" width="120"/> | [team2_gao](preview/d.sharp_plus/team2_gao.stl) | 9 | 4.303 | 12.957 | 8.638 | [^4] |
| <img src="preview/d.sharp_plus/threecees_paardekooper.png" width="120"/> | [threecees_paardekooper](preview/d.sharp_plus/threecees_paardekooper.stl) | 1 | 1.788 | 5.364 | 3.576 | [^27] |
| <img src="preview/d.sharp_plus/toothbrush_holder_quadwild.png" width="120"/> | [toothbrush_holder_quadwild](preview/d.sharp_plus/toothbrush_holder_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 12 | 2.702 | 8.172 | 5.448 | [^1] |
| <img src="preview/d.sharp_plus/TransmissionHousingFem_quadwild.png" width="120"/> | [TransmissionHousingFem_quadwild](preview/d.sharp_plus/TransmissionHousingFem_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 9 | 14.596 | 43.836 | 29.224 | [^1] |
| <img src="preview/d.sharp_plus/triangular_base_mambo.png" width="120"/> | [triangular_base_mambo](preview/d.sharp_plus/triangular_base_mambo.stl) | 4 | 15.070 | 45.228 | 30.152 | [^19] (meshed) |
| <img src="preview/d.sharp_plus/trim-star_quadwild.png" width="120"/> | [trim-star_quadwild](preview/d.sharp_plus/trim-star_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 18.117 | 54.351 | 36.234 | [^1] |
| <img src="preview/d.sharp_plus/tris_open_loopy.png" width="120"/> | [tris_open_loopy](preview/d.sharp_plus/tris_open_loopy.stl) | 1 | 720 | 2.160 | 1.440 | [^9] |
| <img src="preview/d.sharp_plus/turbine_Lp_quadwild.png" width="120"/> | [turbine_Lp_quadwild](preview/d.sharp_plus/turbine_Lp_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 11 | 57.000 | 171.060 | 114.040 | [^1] |
| <img src="preview/d.sharp_plus/twirl_quadwild.png" width="120"/> | [twirl_quadwild](preview/d.sharp_plus/twirl_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 5.201 | 15.603 | 10.402 | [^1] |
| <img src="preview/d.sharp_plus/ujoint_loopy.png" width="120"/> | [ujoint_loopy](preview/d.sharp_plus/ujoint_loopy.stl) | 2 | 5.574 | 16.728 | 11.152 | [^9] |
| <img src="preview/d.sharp_plus/WheelDassault_quadwild.png" width="120"/> | [WheelDassault_quadwild](preview/d.sharp_plus/WheelDassault_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 39.852 | 119.580 | 79.720 | [^1] |
| <img src="preview/d.sharp_plus/wrench_loopy.png" width="120"/> | [wrench_loopy](preview/d.sharp_plus/wrench_loopy.stl) | 1 | 2.248 | 6.744 | 4.496 | [^9] |
| <img src="preview/d.sharp_plus/www_re_quadwild.png" width="120"/> | [www_re_quadwild](preview/d.sharp_plus/www_re_quadwild.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 1 | 28.712 | 86.136 | 57.424 | [^1] |

### (e) nightmares (g≥0, n=24)
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | model | genus | vertices | edges | triangles | source |
|-|-------|-------|----------|-------|-----------|--------|
| <img src="preview/e.nightmares/509316_thingi.png" width="120"/> | [509316_thingi](preview/e.nightmares/509316_thingi.stl) | 119 | 28.564 | 86.400 | 57.600 | [^2] |
| <img src="preview/e.nightmares/7-connected_nop.png" width="120"/> | [7-connected_nop](preview/e.nightmares/7-connected_nop.stl) | 0 | 76.326 | 228.972 | 152.648 | [^28] |
| <img src="preview/e.nightmares/7-connected_snoep.png" width="120"/> | [7-connected_snoep](preview/e.nightmares/7-connected_snoep.stl) | 0 | 6.890 | 20.664 | 13.776 | [^28] (simplified) |
| <img src="preview/e.nightmares/8-connected_nop.png" width="120"/> | [8-connected_nop](preview/e.nightmares/8-connected_nop.stl) | 0 | 114.112 | 342.330 | 228.220 | [^28] |
| <img src="preview/e.nightmares/8-connected_snoep.png" width="120"/> | [8-connected_snoep](preview/e.nightmares/8-connected_snoep.stl) | 0 | 10.424 | 31.266 | 20.844 | [^28] (simplified) |
| <img src="preview/e.nightmares/conjoined_twins_nop.png" width="120"/> | [conjoined_twins_nop](preview/e.nightmares/conjoined_twins_nop.stl) | 0 | 63.873 | 191.613 | 127.742 | [^28] |
| <img src="preview/e.nightmares/conjoined_twins_snoep.png" width="120"/> | [conjoined_twins_snoep](preview/e.nightmares/conjoined_twins_snoep.stl) | 0 | 9.272 | 27.810 | 18.540 | [^28] (simplified) |
| <img src="preview/e.nightmares/Csaszar_crane.png" width="120"/> | [Csaszar_crane](preview/e.nightmares/Csaszar_crane.stl) | 1 | 448 | 1.344 | 896 | [^10] (remeshed) |
| <img src="preview/e.nightmares/cuboid_screw_thread_nop.png" width="120"/> | [cuboid_screw_thread_nop](preview/e.nightmares/cuboid_screw_thread_nop.stl) | 0 | 88.075 | 264.219 | 176.146 | [^28] |
| <img src="preview/e.nightmares/cuboid_screw_thread_snoep.png" width="120"/> | [cuboid_screw_thread_snoep](preview/e.nightmares/cuboid_screw_thread_snoep.stl) | 0 | 15.424 | 46.266 | 30.844 | [^28] (simplified) |
| <img src="preview/e.nightmares/cuboid_torus_with_step_nop.png" width="120"/> | [cuboid_torus_with_step_nop](preview/e.nightmares/cuboid_torus_with_step_nop.stl) | 1 | 80.371 | 241.113 | 160.742 | [^28] |
| <img src="preview/e.nightmares/cuboid_torus_with_step_snoep.png" width="120"/> | [cuboid_torus_with_step_snoep](preview/e.nightmares/cuboid_torus_with_step_snoep.stl) | 1 | 4.268 | 12.804 | 8.536 | [^28] (simplified) |
| <img src="preview/e.nightmares/cuboid_tray_with_step_nop.png" width="120"/> | [cuboid_tray_with_step_nop](preview/e.nightmares/cuboid_tray_with_step_nop.stl) | 0 | 79.151 | 237.447 | 158.298 | [^28] |
| <img src="preview/e.nightmares/cuboid_tray_with_step_snoep.png" width="120"/> | [cuboid_tray_with_step_snoep](preview/e.nightmares/cuboid_tray_with_step_snoep.stl) | 0 | 8.562 | 25.680 | 17.120 | [^28] (simplified) |
| <img src="preview/e.nightmares/encrusted_cube_nop.png" width="120"/> | [encrusted_cube_nop](preview/e.nightmares/encrusted_cube_nop.stl) | 0 | 24.823 | 74.463 | 49.642 | [^28] |
| <img src="preview/e.nightmares/encrusted_cube_snoep.png" width="120"/> | [encrusted_cube_snoep](preview/e.nightmares/encrusted_cube_snoep.stl) | 0 | 17.660 | 52.974 | 35.316 | [^28] (simplified) |
| <img src="preview/e.nightmares/in-volume_knot_nop.png" width="120"/> | [in-volume_knot_nop](preview/e.nightmares/in-volume_knot_nop.stl) | 1 | 13.375 | 40.125 | 26.750 | [^28] (meshed) |
| <img src="preview/e.nightmares/in-volume_twist_nop.png" width="120"/> | [in-volume_twist_nop](preview/e.nightmares/in-volume_twist_nop.stl) | 2 | 78.524 | 235.578 | 157.052 | [^28] |
| <img src="preview/e.nightmares/kid14_topkids.png" width="120"/> | [kid14_topkids](preview/e.nightmares/kid14_topkids.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 8 | 9.585 | 28.797 | 19.198 | [^12] (repaired) |
| <img src="preview/e.nightmares/kid15_topkids.png" width="120"/> | [kid15_topkids](preview/e.nightmares/kid15_topkids.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 6 | 8.860 | 26.610 | 17.740 | [^12] (repaired) |
| <img src="preview/e.nightmares/kid18_topkids.png" width="120"/> | [kid18_topkids](preview/e.nightmares/kid18_topkids.stl) <img src="https://img.shields.io/badge/-NEW-e11d48" alt="NEW"/> | 5 | 11.176 | 33.552 | 22.368 | [^12] (repaired) |
| <img src="preview/e.nightmares/pipe_helix_7_nop.png" width="120"/> | [pipe_helix_7_nop](preview/e.nightmares/pipe_helix_7_nop.stl) | 7 | 90.136 | 270.444 | 180.296 | [^28] |
| <img src="preview/e.nightmares/pipe_helix_nop.png" width="120"/> | [pipe_helix_nop](preview/e.nightmares/pipe_helix_nop.stl) | 1 | 53.939 | 161.817 | 107.878 | [^28] |
| <img src="preview/e.nightmares/yeahright_crane.png" width="120"/> | [yeahright_crane](preview/e.nightmares/yeahright_crane.stl) | 131 | 377.084 | 1.132.032 | 754.688 | [^10] |

[^1]: PIETRONI N., NUVOLI S., ALDERIGHI T., CIGNONI P., TARINI M., PANOZZO D.: Reliable feature-line driven quad-remeshing. _ACM Transactions on Graphics 40_, 4 (2021). [doi:10.1145/3450626.3459941](https://doi.org/10.1145/3450626.3459941)
[^2]: ZHOU Q., JACOBSON A.: Thingi10K: a dataset of 10,000 3D-printing models. arXiv:1605.04797 (2016). [doi:10.48550/arXiv.1605.04797](https://doi.org/10.48550/arXiv.1605.04797)
[^3]: TELEA A.: Skeletonization benchmark: 3D mesh shapes. [webspace.science.uu.nl/~telea001/Shapes/SkelBenchmark](https://webspace.science.uu.nl/~telea001/Shapes/SkelBenchmark)
[^4]: GAO X., SHEN H., PANOZZO D.: Feature preserving octree-based hexahedral meshing. _Computer Graphics Forum (SGP) 38_, 5 (2019). [doi:10.1111/cgf.13795](https://doi.org/10.1111/cgf.13795)
[^5]: FACUNLA J.: Among Us crewmate. Sketchfab. [sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0](https://sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0)
[^6]: DOWNS L., FRANCIS A., KOENIG N., KINMAN B., HICKMAN R., REYMANN K., MCHUGH T. B., VANHOUCKE V.: Google Scanned Objects: a high-quality dataset of 3D scanned household items. In _IEEE International Conference on Robotics and Automation (ICRA)_ (2022). [doi:10.1109/ICRA46639.2022.9811809](https://doi.org/10.1109/ICRA46639.2022.9811809)
[^7]: JACOBSON A.: Common 3D test models. [github.com/alecjacobson/common-3d-test-models](https://github.com/alecjacobson/common-3d-test-models)
[^8]: STEIN O.: meshes. [github.com/odedstein/meshes](https://github.com/odedstein/meshes)
[^9]: LIVESU M., PIETRONI N., PUPPO E., SHEFFER A., CIGNONI P.: LoopyCuts: practical feature-preserving block decomposition for strongly hex-dominant meshing. _ACM Transactions on Graphics 39_, 4 (2020). [doi:10.1145/3386569.3392472](https://doi.org/10.1145/3386569.3392472)
[^10]: CRANE K.: Keenan's 3D model repository. [cs.cmu.edu/~kmcrane/Projects/ModelRepository](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/)
[^11]: LIVESU M., VINING N., SHEFFER A., GREGSON J., SCATENI R.: PolyCut: monotone graph-cuts for polycube base-complex construction. _ACM Transactions on Graphics 32_, 6 (2013). [doi:10.1145/2508363.2508388](https://doi.org/10.1145/2508363.2508388)
[^12]: LÄHNER Z., RODOLÀ E., BRONSTEIN M. M., CREMERS D., ET AL.: SHREC'16: matching of deformable shapes with topological noise. In _Eurographics Workshop on 3D Object Retrieval_ (2016). [cvg.cit.tum.de/data/datasets/topkids](https://cvg.cit.tum.de/data/datasets/topkids)
[^13]: LIAN Z., GODIL A., BUSTOS B., DAOUDI M., HERMANS J., KAWAMURA S., KURITA Y., LAVOUÉ G., ET AL.: SHREC'11 track: shape retrieval on non-rigid 3D watertight meshes. In _Eurographics Workshop on 3D Object Retrieval_ (2011). [doi:10.2312/3DOR/3DOR11/079-088](https://doi.org/10.2312/3DOR/3DOR11/079-088)
[^14]: SCHAREIN R., BOOTH K. S.: Interactive knot theory with KnotPlot. In _Multimedia Tools for Communicating Mathematics_, Mathematics and Visualization (2002). [doi:10.1007/978-3-642-56240-2_17](https://doi.org/10.1007/978-3-642-56240-2_17)
[^15]: LARIC O.: Three D Scans. [threedscans.com](https://threedscans.com), via [huggingface.co/datasets/alecjacobson/threedscans](https://huggingface.co/datasets/alecjacobson/threedscans)
[^16]: TURK G., LEVOY M.: Zippered polygon meshes from range images. In _SIGGRAPH_ (1994). [doi:10.1145/192161.192241](https://doi.org/10.1145/192161.192241); CURLESS B., LEVOY M.: A volumetric method for building complex models from range images. In _SIGGRAPH_ (1996). [doi:10.1145/237170.237269](https://doi.org/10.1145/237170.237269). Via the [Stanford 3D scanning repository](https://graphics.stanford.edu/data/3Dscanrep/)
[^17]: THE CGAL PROJECT: _CGAL User and Reference Manual_. CGAL Editorial Board. Test meshes from [github.com/CGAL/cgal/tree/main/Data/data/meshes](https://github.com/CGAL/cgal/tree/main/Data/data/meshes)
[^18]: JAYANTI S., KALYANARAMAN Y., IYER N., RAMANI K.: Developing an engineering shape benchmark for CAD models. _Computer-Aided Design 38_, 9 (2006). [doi:10.1016/j.cad.2006.06.007](https://doi.org/10.1016/j.cad.2006.06.007)
[^19]: LEDOUX F.: MAMBO: Model dAtabase Mesh BlOcking. [gitlab.com/franck.ledoux/mambo](https://gitlab.com/franck.ledoux/mambo)
[^20]: VASSBERG J. C., DEHAAN M. A., RIVERS S. M., WAHLS R. A.: Development of a common research model for applied CFD validation studies. In _26th AIAA Applied Aerodynamics Conference_ (2008). [doi:10.2514/6.2008-6919](https://doi.org/10.2514/6.2008-6919). Geometry from the [AIAA CFD Drag Prediction Workshop](https://aiaa-dpw.larc.nasa.gov/)
[^21]: JACOBSON A., PANOZZO D.: libigl: prototyping geometry processing research in C++. In _SIGGRAPH Asia Courses_ (2017). [doi:10.1145/3134472.3134497](https://doi.org/10.1145/3134472.3134497). Data from [github.com/libigl/libigl-tutorial-data](https://github.com/libigl/libigl-tutorial-data)
[^22]: LACY D. S., SCLAFANI A. J.: Development of the High Lift Common Research Model (HL-CRM): a representative high lift configuration for transonic transports. In _54th AIAA Aerospace Sciences Meeting_ (2016). [doi:10.2514/6.2016-0308](https://doi.org/10.2514/6.2016-0308). Geometry from the [AIAA CFD High Lift Prediction Workshop](https://www.nasa.gov/reference/aiaa-cfd-high-lift-prediction-workshop/)
[^23]: PARK M. A., MORGENSTERN J. M.: Summary and statistical analysis of the first AIAA sonic boom prediction workshop. _Journal of Aircraft 53_, 2 (2016). [doi:10.2514/1.C033449](https://doi.org/10.2514/1.C033449). Geometry from the [AIAA Sonic Boom Prediction Workshop](https://lbpw.larc.nasa.gov/)
[^24]: BEAUFORT P.-A., REBEROL M., KALMYKOV D., LIU H., LEDOUX F., BOMMES D.: Hex me if you can. _Computer Graphics Forum (SGP) 41_, 5 (2022). [doi:10.1111/cgf.14608](https://doi.org/10.1111/cgf.14608)
[^25]: LIPMAN R., LUBELL J.: Conformance checking of PMI representation in CAD model STEP data exchange files. _Computer-Aided Design 66_ (2015). [doi:10.1016/j.cad.2015.04.002](https://doi.org/10.1016/j.cad.2015.04.002). Models from the [NIST MBE PMI test system](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0)
[^26]: NASA: NASA 3D Resources. [github.com/nasa/NASA-3D-Resources](https://github.com/nasa/NASA-3D-Resources)
[^27]: PAARDEKOOPER B.: threecees. Personal communication.
[^28]: MESTRALLET S., BOURCIER C., LEDOUX F.: Nightmare of polycubes, version 2.0.0 (dataset). [github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes)
