This repository contains a curated collection of 132 triangle meshes spanning a wide variety of shapes. All meshes are verified to be connected, watertight, orientable, and manifold. You can refer to a specific version of the dataset (e.g., in a publication) through the [releases](https://github.com/tue-alga/meshes/releases) page.

> 💡 **Tip:** GitHub has a built-in STL viewer. Click on any model in the repository to preview it interactively in 3D.

All meshes are provided in `.obj` and `.stl` format. The collection is organized into five categories based on geometric character and topological complexity: (a) **bouba genus 0**, (b) **bouba genus ≥ 1**, (c) **kiki genus 0**, (d) **kiki genus ≥ 1**, and (e) **nightmares**. Here, *bouba* refers to smooth or organic shapes, *kiki* to CAD or mechanical shapes, and *nightmares* to very challenging shapes with unusual geometric or topological quirks.

Note that some shapes did not originally come from a triangle mesh, or came from a very poor or broken one. In those cases, we processed the shape into a connected watertight orientable manifold triangle mesh.

### (a) bouba (g=0, n=41)
| model | genus | vertices | edges | triangles | source |
|-------|-------|----------|-------|-----------|--------|
| [airplane1](dataset/a.bouba_zero/airplane1.stl) | 0 | 9.417 | 28.245 | 18.830 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [airplane2](dataset/a.bouba_zero/airplane2.stl) | 0 | 26.806 | 80.412 | 53.608 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [amogus](dataset/a.bouba_zero/amogus.stl) | 0 | 964 | 2.886 | 1.924 | [joshua facunla](https://sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0) |
| [armadillo](dataset/a.bouba_zero/armadillo.stl) | 0 | 14.587 | 43.755 | 29.170 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/armadillo) |
| [armchair](dataset/a.bouba_zero/armchair.stl) | 0 | 12.972 | 38.910 | 25.940 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [bimba](dataset/a.bouba_zero/bimba.stl) | 0 | 10.797 | 32.385 | 21.590 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [bird](dataset/a.bouba_zero/bird.stl) | 0 | 17.318 | 51.948 | 34.632 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [blade](dataset/a.bouba_zero/blade.stl) | 0 | 14.106 | 42.312 | 28.208 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [blocktopus](dataset/a.bouba_zero/blocktopus.stl) | 0 | 5.054 | 15.156 | 10.104 | [Thingi10K](https://ten-thousand-models.appspot.com/detail.html?file_id=86849) |
| [blub](dataset/a.bouba_zero/blub.stl) | 0 | 7.106 | 21.312 | 14.208 | [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| [bone](dataset/a.bouba_zero/bone.stl) | 0 | 6.046 | 18.132 | 12.088 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [bumpysphere](dataset/a.bouba_zero/bumpysphere.stl) | 0 | 22.890 | 68.664 | 45.776 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [bunny](dataset/a.bouba_zero/bunny.stl) | 0 | 11.120 | 33.354 | 22.236 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/bunny) |
| [buste](dataset/a.bouba_zero/buste.stl) | 0 | 6.070 | 18.204 | 12.136 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| [camillehand](dataset/a.bouba_zero/camillehand.stl) | 0 | 16.565 | 49.689 | 33.126 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [cat](dataset/a.bouba_zero/cat.stl) | 0 | 7.949 | 23.841 | 15.894 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/cat) |
| [chineselion](dataset/a.bouba_zero/chineselion.stl) | 0 | 4.248 | 12.738 | 8.492 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| [david](dataset/a.bouba_zero/david.stl) | 0 | 25.434 | 76.296 | 50.864 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [deformedarmadillo](dataset/a.bouba_zero/deformedarmadillo.stl) | 0 | 87.286 | 261.852 | 174.568 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dente](dataset/a.bouba_zero/dente.stl) | 0 | 12.195 | 36.579 | 24.386 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dilo](dataset/a.bouba_zero/dilo.stl) | 0 | 22.154 | 66.456 | 44.304 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dino](dataset/a.bouba_zero/dino.stl) | 0 | 16.634 | 49.896 | 33.264 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dino2](dataset/a.bouba_zero/dino2.stl) | 0 | 10.178 | 30.528 | 20.352 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [duck](dataset/a.bouba_zero/duck.stl) | 0 | 3.598 | 10.788 | 7.192 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [duck2](dataset/a.bouba_zero/duck2.stl) | 0 | 9.640 | 28.914 | 19.276 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [fish1](dataset/a.bouba_zero/fish1.stl) | 0 | 11.895 | 35.679 | 23.786 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [fish2](dataset/a.bouba_zero/fish2.stl) | 0 | 10.604 | 31.806 | 21.204 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [foot](dataset/a.bouba_zero/foot.stl) | 0 | 10.342 | 31.020 | 20.680 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [gargoyle](dataset/a.bouba_zero/gargoyle.stl) | 0 | 13.024 | 39.066 | 26.044 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [ghost](dataset/a.bouba_zero/ghost.stl) | 0 | 1.698 | 5.088 | 3.392 | [Thingi10K](https://ten-thousand-models.appspot.com/detail.html?file_id=40746) |
| [goathead](dataset/a.bouba_zero/goathead.stl) | 0 | 2.763 | 8.283 | 5.522 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/goathead) |
| [homer](dataset/a.bouba_zero/homer.stl) | 0 | 13.639 | 40.911 | 27.274 | [Alec Jacobson](https://github.com/alecjacobson/common-3d-test-models) |
| [igea](dataset/a.bouba_zero/igea.stl) | 0 | 25.282 | 75.840 | 50.560 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [insect](dataset/a.bouba_zero/insect.stl) | 0 | 39.370 | 118.104 | 78.736 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [koala](dataset/a.bouba_zero/koala.stl) | 0 | 3.560 | 10.674 | 7.116 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [moai](dataset/a.bouba_zero/moai.stl) | 0 | 10.002 | 30.000 | 20.000 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [sphinx](dataset/a.bouba_zero/sphinx.stl) | 0 | 10.608 | 31.818 | 21.212 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [spot](dataset/a.bouba_zero/spot.stl) | 0 | 11.533 | 34.593 | 23.062 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/spot) |
| [toy1](dataset/a.bouba_zero/toy1.stl) | 0 | 13.452 | 40.350 | 26.900 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [toy2](dataset/a.bouba_zero/toy2.stl) | 0 | 10.755 | 32.259 | 21.506 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [venus](dataset/a.bouba_zero/venus.stl) | 0 | 10.874 | 32.616 | 21.744 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |

### (b) bouba (g≥1, n=25)
| model | genus | vertices | edges | triangles | source |
|-------|-------|----------|-------|-----------|--------|
| [bob](dataset/b.bouba_plus/bob.stl) | 1 | 5.344 | 16.032 | 10.688 | [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| [botijo](dataset/b.bouba_plus/botijo.stl) | 5 | 12.127 | 36.405 | 24.270 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [bottle1](dataset/b.bouba_plus/bottle1.stl) | 1 | 14.832 | 44.496 | 29.664 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [bottle2](dataset/b.bouba_plus/bottle2.stl) | 1 | 14.595 | 43.785 | 29.190 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [bumpytorus](dataset/b.bouba_plus/bumpytorus.stl) | 1 | 15.279 | 45.837 | 30.558 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [camel](dataset/b.bouba_plus/camel.stl) | 1 | 34.546 | 103.638 | 69.092 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [carter](dataset/b.bouba_plus/carter.stl) | 7 | 67.436 | 202.344 | 134.896 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [chair](dataset/b.bouba_plus/chair.stl) | 7 | 23.081 | 69.279 | 46.186 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [chair1](dataset/b.bouba_plus/chair1.stl) | 4 | 11.421 | 34.281 | 22.854 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [cup](dataset/b.bouba_plus/cup.stl) | 2 | 10.495 | 31.491 | 20.994 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [cup1](dataset/b.bouba_plus/cup1.stl) | 1 | 15.564 | 46.692 | 31.128 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dancer](dataset/b.bouba_plus/dancer.stl) | 1 | 12.048 | 36.144 | 24.096 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dancer2](dataset/b.bouba_plus/dancer2.stl) | 1 | 30.248 | 90.744 | 60.496 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dancingchildren](dataset/b.bouba_plus/dancingchildren.stl) | 8 | 12.163 | 36.531 | 24.354 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dragonstand](dataset/b.bouba_plus/dragonstand.stl) | 1 | 21.042 | 63.126 | 42.084 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dragonstand2](dataset/b.bouba_plus/dragonstand2.stl) | 1 | 30.561 | 91.683 | 61.122 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [dtorus](dataset/b.bouba_plus/dtorus.stl) | 2 | 10.090 | 30.276 | 20.184 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [eight](dataset/b.bouba_plus/eight.stl) | 2 | 5.544 | 16.638 | 11.092 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [elephant](dataset/b.bouba_plus/elephant.stl) | 3 | 38.084 | 114.264 | 76.176 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [elk](dataset/b.bouba_plus/elk.stl) | 1 | 23.114 | 69.342 | 46.228 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [fertility](dataset/b.bouba_plus/fertility.stl) | 4 | 26.222 | 78.684 | 52.456 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [genus3](dataset/b.bouba_plus/genus3.stl) | 3 | 33.952 | 101.868 | 67.912 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [grayloc](dataset/b.bouba_plus/grayloc.stl) | 9 | 11.339 | 34.065 | 22.710 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [oilpump](dataset/b.bouba_plus/oilpump.stl) | 4 | 68.742 | 206.244 | 137.496 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [teapot](dataset/b.bouba_plus/teapot.stl) | 1 | 13.464 | 40.392 | 26.928 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |

### (c) kiki (g=0, n=56)
| model | genus | vertices | edges | triangles | source |
|-------|-------|----------|-------|-----------|--------|
| [B0](dataset/c.kiki_zero/B0.stl) | 0 | 20.610 | 61.824 | 41.216 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B11](dataset/c.kiki_zero/B11.stl) | 0 | 7.426 | 22.272 | 14.848 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B12](dataset/c.kiki_zero/B12.stl) | 0 | 8.130 | 24.384 | 16.256 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B14](dataset/c.kiki_zero/B14.stl) | 0 | 9.154 | 27.456 | 18.304 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B15](dataset/c.kiki_zero/B15.stl) | 0 | 8.258 | 24.768 | 16.512 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B16](dataset/c.kiki_zero/B16.stl) | 0 | 7.298 | 21.888 | 14.592 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B17](dataset/c.kiki_zero/B17.stl) | 0 | 18.306 | 54.912 | 36.608 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B18](dataset/c.kiki_zero/B18.stl) | 0 | 11.906 | 35.712 | 23.808 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B19](dataset/c.kiki_zero/B19.stl) | 0 | 20.546 | 61.632 | 41.088 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B2](dataset/c.kiki_zero/B2.stl) | 0 | 11.650 | 34.944 | 23.296 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B20](dataset/c.kiki_zero/B20.stl) | 0 | 10.050 | 30.144 | 20.096 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B21](dataset/c.kiki_zero/B21.stl) | 0 | 15.234 | 45.696 | 30.464 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B23](dataset/c.kiki_zero/B23.stl) | 0 | 13.378 | 40.128 | 26.752 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B25](dataset/c.kiki_zero/B25.stl) | 0 | 15.554 | 46.656 | 31.104 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B27](dataset/c.kiki_zero/B27.stl) | 0 | 17.602 | 52.800 | 35.200 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B30](dataset/c.kiki_zero/B30.stl) | 0 | 10.754 | 32.256 | 21.504 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B34](dataset/c.kiki_zero/B34.stl) | 0 | 13.954 | 41.856 | 27.904 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B35](dataset/c.kiki_zero/B35.stl) | 0 | 17.218 | 51.648 | 34.432 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B36](dataset/c.kiki_zero/B36.stl) | 0 | 29.890 | 89.664 | 59.776 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B37](dataset/c.kiki_zero/B37.stl) | 0 | 22.018 | 66.048 | 44.032 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B38](dataset/c.kiki_zero/B38.stl) | 0 | 9.474 | 28.416 | 18.944 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B39](dataset/c.kiki_zero/B39.stl) | 0 | 13.570 | 40.704 | 27.136 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B4](dataset/c.kiki_zero/B4.stl) | 0 | 21.250 | 63.744 | 42.496 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B40](dataset/c.kiki_zero/B40.stl) | 0 | 14.082 | 42.240 | 28.160 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B41](dataset/c.kiki_zero/B41.stl) | 0 | 18.306 | 54.912 | 36.608 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B42](dataset/c.kiki_zero/B42.stl) | 0 | 10.754 | 32.256 | 21.504 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B43](dataset/c.kiki_zero/B43.stl) | 0 | 13.890 | 41.664 | 27.776 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B45](dataset/c.kiki_zero/B45.stl) | 0 | 14.466 | 43.392 | 28.928 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B46](dataset/c.kiki_zero/B46.stl) | 0 | 15.490 | 46.464 | 30.976 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B48](dataset/c.kiki_zero/B48.stl) | 0 | 10.626 | 31.872 | 21.248 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B49](dataset/c.kiki_zero/B49.stl) | 0 | 18.178 | 54.528 | 36.352 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B5](dataset/c.kiki_zero/B5.stl) | 0 | 13.506 | 40.512 | 27.008 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B50](dataset/c.kiki_zero/B50.stl) | 0 | 13.698 | 41.088 | 27.392 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B52](dataset/c.kiki_zero/B52.stl) | 0 | 12.546 | 37.632 | 25.088 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B54](dataset/c.kiki_zero/B54.stl) | 0 | 10.242 | 30.720 | 20.480 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B56](dataset/c.kiki_zero/B56.stl) | 0 | 11.138 | 33.408 | 22.272 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B57](dataset/c.kiki_zero/B57.stl) | 0 | 19.778 | 59.328 | 39.552 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B58](dataset/c.kiki_zero/B58.stl) | 0 | 22.722 | 68.160 | 45.440 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B59](dataset/c.kiki_zero/B59.stl) | 0 | 20.290 | 60.864 | 40.576 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B6](dataset/c.kiki_zero/B6.stl) | 0 | 16.002 | 48.000 | 32.000 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B60](dataset/c.kiki_zero/B60.stl) | 0 | 9.602 | 28.800 | 19.200 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B61](dataset/c.kiki_zero/B61.stl) | 0 | 10.498 | 31.488 | 20.992 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B67](dataset/c.kiki_zero/B67.stl) | 0 | 13.890 | 41.664 | 27.776 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B68](dataset/c.kiki_zero/B68.stl) | 0 | 16.898 | 50.688 | 33.792 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B69](dataset/c.kiki_zero/B69.stl) | 0 | 11.650 | 34.944 | 23.296 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B7](dataset/c.kiki_zero/B7.stl) | 0 | 12.354 | 37.056 | 24.704 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B70](dataset/c.kiki_zero/B70.stl) | 0 | 13.122 | 39.360 | 26.240 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B71](dataset/c.kiki_zero/B71.stl) | 0 | 11.778 | 35.328 | 23.552 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B72](dataset/c.kiki_zero/B72.stl) | 0 | 14.082 | 42.240 | 28.160 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B74](dataset/c.kiki_zero/B74.stl) | 0 | 13.698 | 41.088 | 27.392 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B75](dataset/c.kiki_zero/B75.stl) | 0 | 14.850 | 44.544 | 29.696 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B76](dataset/c.kiki_zero/B76.stl) | 0 | 19.586 | 58.752 | 39.168 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B8](dataset/c.kiki_zero/B8.stl) | 0 | 17.858 | 53.568 | 35.712 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B9](dataset/c.kiki_zero/B9.stl) | 0 | 8.770 | 26.304 | 17.536 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [fandisk](dataset/c.kiki_zero/fandisk.stl) | 0 | 7.229 | 21.681 | 14.454 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [S37](dataset/c.kiki_zero/S37.stl) | 0 | 19.010 | 57.024 | 38.016 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |

### (d) kiki (g≥1, n=58)
| model | genus | vertices | edges | triangles | source |
|-------|-------|----------|-------|-----------|--------|
| [B1](dataset/d.kiki_plus/B1.stl) | 1 | 12.800 | 38.400 | 25.600 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B10](dataset/d.kiki_plus/B10.stl) | 1 | 22.016 | 66.048 | 44.032 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B13](dataset/d.kiki_plus/B13.stl) | 1 | 11.520 | 34.560 | 23.040 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B28](dataset/d.kiki_plus/B28.stl) | 1 | 21.248 | 63.744 | 42.496 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B29](dataset/d.kiki_plus/B29.stl) | 1 | 19.072 | 57.216 | 38.144 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B3](dataset/d.kiki_plus/B3.stl) | 2 | 25.726 | 77.184 | 51.456 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B31](dataset/d.kiki_plus/B31.stl) | 1 | 19.904 | 59.712 | 39.808 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B32](dataset/d.kiki_plus/B32.stl) | 1 | 23.808 | 71.424 | 47.616 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B33](dataset/d.kiki_plus/B33.stl) | 1 | 23.616 | 70.848 | 47.232 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B44](dataset/d.kiki_plus/B44.stl) | 1 | 14.912 | 44.736 | 29.824 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B47](dataset/d.kiki_plus/B47.stl) | 1 | 19.840 | 59.520 | 39.680 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B51](dataset/d.kiki_plus/B51.stl) | 1 | 15.360 | 46.080 | 30.720 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B53](dataset/d.kiki_plus/B53.stl) | 1 | 14.400 | 43.200 | 28.800 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B55](dataset/d.kiki_plus/B55.stl) | 1 | 11.904 | 35.712 | 23.808 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B62](dataset/d.kiki_plus/B62.stl) | 1 | 16.320 | 48.960 | 32.640 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B63](dataset/d.kiki_plus/B63.stl) | 1 | 16.192 | 48.576 | 32.384 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B64](dataset/d.kiki_plus/B64.stl) | 1 | 16.000 | 48.000 | 32.000 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B65](dataset/d.kiki_plus/B65.stl) | 1 | 16.384 | 49.152 | 32.768 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B66](dataset/d.kiki_plus/B66.stl) | 2 | 18.110 | 54.336 | 36.224 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B73](dataset/d.kiki_plus/B73.stl) | 1 | 15.744 | 47.232 | 31.488 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [block](dataset/d.kiki_plus/block.stl) | 3 | 8.052 | 24.168 | 16.112 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [M1](dataset/d.kiki_plus/M1.stl) | 9 | 43.376 | 130.176 | 86.784 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M2](dataset/d.kiki_plus/M2.stl) | 3 | 19.772 | 59.328 | 39.552 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M3](dataset/d.kiki_plus/M3.stl) | 5 | 41.336 | 124.032 | 82.688 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M4](dataset/d.kiki_plus/M4.stl) | 3 | 31.868 | 95.616 | 63.744 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M5](dataset/d.kiki_plus/M5.stl) | 7 | 57.780 | 173.376 | 115.584 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M6](dataset/d.kiki_plus/M6.stl) | 4 | 29.306 | 87.936 | 58.624 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M8](dataset/d.kiki_plus/M8.stl) | 1 | 26.496 | 79.488 | 52.992 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M9](dataset/d.kiki_plus/M9.stl) | 5 | 34.360 | 103.104 | 68.736 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [rocker](dataset/d.kiki_plus/rocker.stl) | 1 | 26.656 | 79.968 | 53.312 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [rod](dataset/d.kiki_plus/rod.stl) | 2 | 8.814 | 26.448 | 17.632 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [S0](dataset/d.kiki_plus/S0.stl) | 3 | 24.572 | 73.728 | 49.152 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S1](dataset/d.kiki_plus/S1.stl) | 3 | 21.500 | 64.512 | 43.008 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S20](dataset/d.kiki_plus/S20.stl) | 7 | 36.660 | 110.016 | 73.344 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S22](dataset/d.kiki_plus/S22.stl) | 3 | 24.316 | 72.960 | 48.640 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S23](dataset/d.kiki_plus/S23.stl) | 2 | 24.510 | 73.536 | 49.024 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S24](dataset/d.kiki_plus/S24.stl) | 3 | 17.980 | 53.952 | 35.968 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S25](dataset/d.kiki_plus/S25.stl) | 3 | 25.916 | 77.760 | 51.840 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S26](dataset/d.kiki_plus/S26.stl) | 4 | 28.922 | 86.784 | 57.856 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S27](dataset/d.kiki_plus/S27.stl) | 5 | 33.016 | 99.072 | 66.048 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S3](dataset/d.kiki_plus/S3.stl) | 2 | 26.174 | 78.528 | 52.352 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S33](dataset/d.kiki_plus/S33.stl) | 1 | 17.600 | 52.800 | 35.200 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S34](dataset/d.kiki_plus/S34.stl) | 3 | 36.284 | 108.864 | 72.576 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S35](dataset/d.kiki_plus/S35.stl) | 1 | 18.240 | 54.720 | 36.480 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S36](dataset/d.kiki_plus/S36.stl) | 1 | 23.296 | 69.888 | 46.592 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S38](dataset/d.kiki_plus/S38.stl) | 3 | 22.652 | 67.968 | 45.312 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S39](dataset/d.kiki_plus/S39.stl) | 2 | 22.718 | 68.160 | 45.440 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S4](dataset/d.kiki_plus/S4.stl) | 3 | 22.460 | 67.392 | 44.928 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S40](dataset/d.kiki_plus/S40.stl) | 1 | 21.056 | 63.168 | 42.112 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S41](dataset/d.kiki_plus/S41.stl) | 1 | 18.432 | 55.296 | 36.864 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S42](dataset/d.kiki_plus/S42.stl) | 1 | 17.408 | 52.224 | 34.816 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S43](dataset/d.kiki_plus/S43.stl) | 1 | 16.000 | 48.000 | 32.000 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S44](dataset/d.kiki_plus/S44.stl) | 1 | 15.744 | 47.232 | 31.488 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S45](dataset/d.kiki_plus/S45.stl) | 1 | 14.720 | 44.160 | 29.440 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S5](dataset/d.kiki_plus/S5.stl) | 7 | 36.916 | 110.784 | 73.856 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S6](dataset/d.kiki_plus/S6.stl) | 5 | 43.000 | 129.024 | 86.016 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S7](dataset/d.kiki_plus/S7.stl) | 2 | 20.734 | 62.208 | 41.472 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S8](dataset/d.kiki_plus/S8.stl) | 1 | 27.072 | 81.216 | 54.144 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |

### (e) nightmares (g≥0, n=11)
| model | genus | vertices | edges | triangles | source |
|-------|-------|----------|-------|-----------|--------|
| [7connected](dataset/e.nightmares/7connected.stl) | 0 | 6.890 | 20.664 | 13.776 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [8connected](dataset/e.nightmares/8connected.stl) | 0 | 10.424 | 31.266 | 20.844 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [encrusted](dataset/e.nightmares/encrusted.stl) | 0 | 17.660 | 52.974 | 35.316 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [pipehelix](dataset/e.nightmares/pipehelix.stl) | 1 | 53.939 | 161.817 | 107.878 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [pipehelix7](dataset/e.nightmares/pipehelix7.stl) | 7 | 90.136 | 270.444 | 180.296 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [screw](dataset/e.nightmares/screw.stl) | 0 | 15.424 | 46.266 | 30.844 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [torusstep](dataset/e.nightmares/torusstep.stl) | 1 | 4.268 | 12.804 | 8.536 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [traystep](dataset/e.nightmares/traystep.stl) | 0 | 8.562 | 25.680 | 17.120 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [twins](dataset/e.nightmares/twins.stl) | 0 | 9.272 | 27.810 | 18.540 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [twist](dataset/e.nightmares/twist.stl) | 2 | 78.524 | 235.578 | 157.052 | [Sébastien Mestrallet](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| [yeahright](dataset/e.nightmares/yeahright.stl) | 131 | 377.084 | 1.132.032 | 754.688 | [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |