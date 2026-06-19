This repository contains a curated collection of 192 triangle meshes spanning a wide variety of shapes. All meshes are verified to be connected, watertight, orientable, and manifold. You can refer to a specific version of the dataset (e.g., in a publication) through the [releases](https://github.com/tue-alga/meshes/releases) page.

> 💡 **Tip:** GitHub has a built-in STL viewer. Click on any model in the repository to preview it interactively in 3D.

All meshes are provided in `.obj` and `.stl` format. The collection is organized into five categories based on geometric character and topological complexity: (a) **bouba genus 0**, (b) **bouba genus ≥ 1**, (c) **kiki genus 0**, (d) **kiki genus ≥ 1**, and (e) **nightmares**. Here, *bouba* refers to smooth or organic shapes, *kiki* to CAD or mechanical shapes, and *nightmares* to very challenging shapes with unusual geometric or topological quirks. The naming system is inspired by [the bouba/kiki effect](https://en.wikipedia.org/wiki/Bouba/kiki_effect).

Note that some shapes did not originally come from a triangle mesh, or came from a very poor or broken one. In those cases, we processed the shape into a connected watertight orientable manifold triangle mesh.

### (a) bouba (g=0, n=67)
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
| [glass1](dataset/a.bouba_zero/glass1.stl) | 0 | 29.674 | 89.016 | 59.344 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [glass2](dataset/a.bouba_zero/glass2.stl) | 0 | 11.710 | 35.124 | 23.416 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [goathead](dataset/a.bouba_zero/goathead.stl) | 0 | 2.763 | 8.283 | 5.522 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/goathead) |
| [hand](dataset/a.bouba_zero/hand.stl) | 0 | 13.982 | 41.940 | 27.960 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [head1](dataset/a.bouba_zero/head1.stl) | 0 | 14.399 | 43.191 | 28.794 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [head2](dataset/a.bouba_zero/head2.stl) | 0 | 14.754 | 44.256 | 29.504 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [homer](dataset/a.bouba_zero/homer.stl) | 0 | 13.639 | 40.911 | 27.274 | [Alec Jacobson](https://github.com/alecjacobson/common-3d-test-models) |
| [horse](dataset/a.bouba_zero/horse.stl) | 0 | 19.851 | 59.547 | 39.698 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [human1](dataset/a.bouba_zero/human1.stl) | 0 | 10.231 | 30.687 | 20.458 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [human2](dataset/a.bouba_zero/human2.stl) | 0 | 12.794 | 38.376 | 25.584 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [human3](dataset/a.bouba_zero/human3.stl) | 0 | 12.329 | 36.981 | 24.654 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [igea](dataset/a.bouba_zero/igea.stl) | 0 | 25.282 | 75.840 | 50.560 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [insect](dataset/a.bouba_zero/insect.stl) | 0 | 39.370 | 118.104 | 78.736 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [isidorehorse](dataset/a.bouba_zero/isidorehorse.stl) | 0 | 19.465 | 58.389 | 38.926 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [koala](dataset/a.bouba_zero/koala.stl) | 0 | 3.560 | 10.674 | 7.116 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [lion](dataset/a.bouba_zero/lion.stl) | 0 | 27.899 | 83.691 | 55.794 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [max](dataset/a.bouba_zero/max.stl) | 0 | 9.936 | 29.802 | 19.868 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [moai](dataset/a.bouba_zero/moai.stl) | 0 | 10.002 | 30.000 | 20.000 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [mouse](dataset/a.bouba_zero/mouse.stl) | 0 | 13.961 | 41.877 | 27.918 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [oni](dataset/a.bouba_zero/oni.stl) | 0 | 12.887 | 38.655 | 25.770 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [pear](dataset/a.bouba_zero/pear.stl) | 0 | 10.754 | 32.256 | 21.504 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [pensatore](dataset/a.bouba_zero/pensatore.stl) | 0 | 19.624 | 58.866 | 39.244 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [pierrot](dataset/a.bouba_zero/pierrot.stl) | 0 | 16.551 | 49.647 | 33.098 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [pig](dataset/a.bouba_zero/pig.stl) | 0 | 15.594 | 46.776 | 31.184 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [ramses](dataset/a.bouba_zero/ramses.stl) | 0 | 13.505 | 40.509 | 27.006 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [redbox](dataset/a.bouba_zero/redbox.stl) | 0 | 50.002 | 150.000 | 100.000 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [retinal](dataset/a.bouba_zero/retinal.stl) | 0 | 14.566 | 43.692 | 29.128 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [santa](dataset/a.bouba_zero/santa.stl) | 0 | 10.406 | 31.212 | 20.808 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [screwdriver](dataset/a.bouba_zero/screwdriver.stl) | 0 | 24.568 | 73.698 | 49.132 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [sediapatch](dataset/a.bouba_zero/sediapatch.stl) | 0 | 15.584 | 46.746 | 31.164 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [sphinx](dataset/a.bouba_zero/sphinx.stl) | 0 | 10.608 | 31.818 | 21.212 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [spot](dataset/a.bouba_zero/spot.stl) | 0 | 11.533 | 34.593 | 23.062 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/spot) |
| [toy1](dataset/a.bouba_zero/toy1.stl) | 0 | 13.452 | 40.350 | 26.900 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [toy2](dataset/a.bouba_zero/toy2.stl) | 0 | 10.755 | 32.259 | 21.506 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [uumemento](dataset/a.bouba_zero/uumemento.stl) | 0 | 46.510 | 139.524 | 93.016 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [venus](dataset/a.bouba_zero/venus.stl) | 0 | 10.874 | 32.616 | 21.744 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [woodenfish](dataset/a.bouba_zero/woodenfish.stl) | 0 | 15.940 | 47.814 | 31.876 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |

### (b) bouba (g≥0, n=34)
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
| [eros](dataset/b.bouba_plus/eros.stl) | 0 | 25.001 | 74.997 | 49.998 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [fertility](dataset/b.bouba_plus/fertility.stl) | 4 | 26.222 | 78.684 | 52.456 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [genus3](dataset/b.bouba_plus/genus3.stl) | 3 | 33.952 | 101.868 | 67.912 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [grayloc](dataset/b.bouba_plus/grayloc.stl) | 9 | 11.339 | 34.065 | 22.710 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [greek](dataset/b.bouba_plus/greek.stl) | 4 | 12.501 | 37.521 | 25.014 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [holes3](dataset/b.bouba_plus/holes3.stl) | 3 | 14.396 | 43.200 | 28.800 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [kiss](dataset/b.bouba_plus/kiss.stl) | 3 | 10.192 | 30.588 | 20.392 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [kitten](dataset/b.bouba_plus/kitten.stl) | 1 | 10.183 | 30.549 | 20.366 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [mastercylinder](dataset/b.bouba_plus/mastercylinder.stl) | 3 | 13.689 | 41.079 | 27.386 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [oilpump](dataset/b.bouba_plus/oilpump.stl) | 4 | 68.742 | 206.244 | 137.496 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [rollingstage](dataset/b.bouba_plus/rollingstage.stl) | 7 | 15.387 | 46.197 | 30.798 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [teapot](dataset/b.bouba_plus/teapot.stl) | 1 | 13.464 | 40.392 | 26.928 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [thaistatue](dataset/b.bouba_plus/thaistatue.stl) | 3 | 20.133 | 60.411 | 40.274 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [wrench](dataset/b.bouba_plus/wrench.stl) | 1 | 12.997 | 38.991 | 25.994 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |

### (c) kiki (g=0, n=56)
| model | genus | vertices | edges | triangles | source |
|-------|-------|----------|-------|-----------|--------|
| [B0](dataset/c.kiki_zero/B0.stl) | 0 | 560 | 1.674 | 1.116 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B11](dataset/c.kiki_zero/B11.stl) | 0 | 1.139 | 3.411 | 2.274 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B12](dataset/c.kiki_zero/B12.stl) | 0 | 885 | 2.649 | 1.766 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B14](dataset/c.kiki_zero/B14.stl) | 0 | 74.218 | 222.648 | 148.432 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B15](dataset/c.kiki_zero/B15.stl) | 0 | 10.769 | 32.301 | 21.534 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B16](dataset/c.kiki_zero/B16.stl) | 0 | 217 | 645 | 430 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B17](dataset/c.kiki_zero/B17.stl) | 0 | 363 | 1.083 | 722 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B18](dataset/c.kiki_zero/B18.stl) | 0 | 329 | 981 | 654 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B19](dataset/c.kiki_zero/B19.stl) | 0 | 1.641 | 4.917 | 3.278 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B2](dataset/c.kiki_zero/B2.stl) | 0 | 918 | 2.748 | 1.832 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B20](dataset/c.kiki_zero/B20.stl) | 0 | 159 | 471 | 314 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B21](dataset/c.kiki_zero/B21.stl) | 0 | 478 | 1.428 | 952 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B23](dataset/c.kiki_zero/B23.stl) | 0 | 211 | 627 | 418 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B25](dataset/c.kiki_zero/B25.stl) | 0 | 1.816 | 5.442 | 3.628 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B27](dataset/c.kiki_zero/B27.stl) | 0 | 459 | 1.371 | 914 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B30](dataset/c.kiki_zero/B30.stl) | 0 | 712 | 2.130 | 1.420 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B34](dataset/c.kiki_zero/B34.stl) | 0 | 514 | 1.536 | 1.024 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B35](dataset/c.kiki_zero/B35.stl) | 0 | 2.115 | 6.339 | 4.226 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B36](dataset/c.kiki_zero/B36.stl) | 0 | 3.991 | 11.967 | 7.978 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B37](dataset/c.kiki_zero/B37.stl) | 0 | 2.668 | 7.998 | 5.332 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B38](dataset/c.kiki_zero/B38.stl) | 0 | 1.956 | 5.862 | 3.908 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B39](dataset/c.kiki_zero/B39.stl) | 0 | 3.628 | 10.878 | 7.252 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B4](dataset/c.kiki_zero/B4.stl) | 0 | 1.216 | 3.642 | 2.428 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B40](dataset/c.kiki_zero/B40.stl) | 0 | 3.171 | 9.507 | 6.338 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B41](dataset/c.kiki_zero/B41.stl) | 0 | 3.529 | 10.581 | 7.054 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B42](dataset/c.kiki_zero/B42.stl) | 0 | 1.843 | 5.523 | 3.682 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B43](dataset/c.kiki_zero/B43.stl) | 0 | 2.626 | 7.872 | 5.248 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B45](dataset/c.kiki_zero/B45.stl) | 0 | 736 | 2.202 | 1.468 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B46](dataset/c.kiki_zero/B46.stl) | 0 | 827 | 2.475 | 1.650 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B48](dataset/c.kiki_zero/B48.stl) | 0 | 1.146 | 3.432 | 2.288 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B49](dataset/c.kiki_zero/B49.stl) | 0 | 528 | 1.578 | 1.052 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B5](dataset/c.kiki_zero/B5.stl) | 0 | 613 | 1.833 | 1.222 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B50](dataset/c.kiki_zero/B50.stl) | 0 | 643 | 1.923 | 1.282 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B52](dataset/c.kiki_zero/B52.stl) | 0 | 545 | 1.629 | 1.086 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B54](dataset/c.kiki_zero/B54.stl) | 0 | 425 | 1.269 | 846 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B56](dataset/c.kiki_zero/B56.stl) | 0 | 586 | 1.752 | 1.168 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B57](dataset/c.kiki_zero/B57.stl) | 0 | 4.951 | 14.847 | 9.898 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B58](dataset/c.kiki_zero/B58.stl) | 0 | 735 | 2.199 | 1.466 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B59](dataset/c.kiki_zero/B59.stl) | 0 | 598 | 1.788 | 1.192 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B6](dataset/c.kiki_zero/B6.stl) | 0 | 659 | 1.971 | 1.314 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B60](dataset/c.kiki_zero/B60.stl) | 0 | 1.043 | 3.123 | 2.082 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B61](dataset/c.kiki_zero/B61.stl) | 0 | 1.125 | 3.369 | 2.246 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B67](dataset/c.kiki_zero/B67.stl) | 0 | 1.279 | 3.831 | 2.554 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B68](dataset/c.kiki_zero/B68.stl) | 0 | 1.137 | 3.405 | 2.270 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B69](dataset/c.kiki_zero/B69.stl) | 0 | 2.119 | 6.351 | 4.234 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B7](dataset/c.kiki_zero/B7.stl) | 0 | 498 | 1.488 | 992 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B70](dataset/c.kiki_zero/B70.stl) | 0 | 2.280 | 6.834 | 4.556 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B71](dataset/c.kiki_zero/B71.stl) | 0 | 2.175 | 6.519 | 4.346 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B72](dataset/c.kiki_zero/B72.stl) | 0 | 1.685 | 5.049 | 3.366 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B74](dataset/c.kiki_zero/B74.stl) | 0 | 1.313 | 3.933 | 2.622 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B75](dataset/c.kiki_zero/B75.stl) | 0 | 1.709 | 5.121 | 3.414 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B76](dataset/c.kiki_zero/B76.stl) | 0 | 508 | 1.518 | 1.012 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B8](dataset/c.kiki_zero/B8.stl) | 0 | 2.794 | 8.376 | 5.584 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B9](dataset/c.kiki_zero/B9.stl) | 0 | 790 | 2.364 | 1.576 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [fandisk](dataset/c.kiki_zero/fandisk.stl) | 0 | 7.229 | 21.681 | 14.454 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [S37](dataset/c.kiki_zero/S37.stl) | 0 | 15.725 | 47.169 | 31.446 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |

### (d) kiki (g≥1, n=60)
| model | genus | vertices | edges | triangles | source |
|-------|-------|----------|-------|-----------|--------|
| [B1](dataset/d.kiki_plus/B1.stl) | 1 | 1.741 | 5.223 | 3.482 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B10](dataset/d.kiki_plus/B10.stl) | 1 | 1.506 | 4.518 | 3.012 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B13](dataset/d.kiki_plus/B13.stl) | 1 | 2.065 | 6.195 | 4.130 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B28](dataset/d.kiki_plus/B28.stl) | 1 | 1.128 | 3.384 | 2.256 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B29](dataset/d.kiki_plus/B29.stl) | 1 | 1.941 | 5.823 | 3.882 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B3](dataset/d.kiki_plus/B3.stl) | 2 | 3.495 | 10.491 | 6.994 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B31](dataset/d.kiki_plus/B31.stl) | 1 | 1.317 | 3.951 | 2.634 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B32](dataset/d.kiki_plus/B32.stl) | 1 | 1.364 | 4.092 | 2.728 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B33](dataset/d.kiki_plus/B33.stl) | 1 | 2.268 | 6.804 | 4.536 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B44](dataset/d.kiki_plus/B44.stl) | 1 | 2.265 | 6.795 | 4.530 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B47](dataset/d.kiki_plus/B47.stl) | 1 | 2.161 | 6.483 | 4.322 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B51](dataset/d.kiki_plus/B51.stl) | 1 | 1.169 | 3.507 | 2.338 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B53](dataset/d.kiki_plus/B53.stl) | 1 | 984 | 2.952 | 1.968 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B55](dataset/d.kiki_plus/B55.stl) | 1 | 802 | 2.406 | 1.604 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B62](dataset/d.kiki_plus/B62.stl) | 1 | 1.016 | 3.048 | 2.032 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B63](dataset/d.kiki_plus/B63.stl) | 1 | 990 | 2.970 | 1.980 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B64](dataset/d.kiki_plus/B64.stl) | 1 | 852 | 2.556 | 1.704 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B65](dataset/d.kiki_plus/B65.stl) | 1 | 936 | 2.808 | 1.872 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B66](dataset/d.kiki_plus/B66.stl) | 2 | 1.159 | 3.483 | 2.322 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [B73](dataset/d.kiki_plus/B73.stl) | 1 | 2.320 | 6.960 | 4.640 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [block](dataset/d.kiki_plus/block.stl) | 3 | 8.052 | 24.168 | 16.112 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [M1](dataset/d.kiki_plus/M1.stl) | 9 | 52.248 | 156.792 | 104.528 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M2](dataset/d.kiki_plus/M2.stl) | 3 | 4.268 | 12.816 | 8.544 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M3](dataset/d.kiki_plus/M3.stl) | 5 | 74.796 | 224.412 | 149.608 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M4](dataset/d.kiki_plus/M4.stl) | 3 | 31.868 | 95.616 | 63.744 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M5](dataset/d.kiki_plus/M5.stl) | 7 | 57.780 | 173.376 | 115.584 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M6](dataset/d.kiki_plus/M6.stl) | 4 | 54.507 | 163.539 | 109.026 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M8](dataset/d.kiki_plus/M8.stl) | 1 | 146.305 | 438.915 | 292.610 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [M9](dataset/d.kiki_plus/M9.stl) | 5 | 67.770 | 203.334 | 135.556 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [rocker](dataset/d.kiki_plus/rocker.stl) | 1 | 26.656 | 79.968 | 53.312 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [rod](dataset/d.kiki_plus/rod.stl) | 2 | 8.814 | 26.448 | 17.632 | [Xifeng Gao](https://cims.nyu.edu/gcl/papers/2019-OctreeMeshing.zip) |
| [S0](dataset/d.kiki_plus/S0.stl) | 3 | 85.962 | 257.898 | 171.932 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S1](dataset/d.kiki_plus/S1.stl) | 3 | 60.440 | 181.332 | 120.888 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S20](dataset/d.kiki_plus/S20.stl) | 7 | 10.211 | 30.669 | 20.446 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S22](dataset/d.kiki_plus/S22.stl) | 3 | 42.465 | 127.407 | 84.938 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S23](dataset/d.kiki_plus/S23.stl) | 2 | 37.229 | 111.693 | 74.462 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S24](dataset/d.kiki_plus/S24.stl) | 3 | 59.706 | 179.130 | 119.420 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S25](dataset/d.kiki_plus/S25.stl) | 3 | 78.708 | 236.136 | 157.424 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S26](dataset/d.kiki_plus/S26.stl) | 4 | 107.960 | 323.898 | 215.932 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S27](dataset/d.kiki_plus/S27.stl) | 5 | 25.417 | 76.275 | 50.850 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S3](dataset/d.kiki_plus/S3.stl) | 2 | 3.298 | 9.900 | 6.600 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S31](dataset/d.kiki_plus/S31.stl) | 7 | 13.704 | 41.148 | 27.432 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S33](dataset/d.kiki_plus/S33.stl) | 1 | 12.097 | 36.291 | 24.194 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S34](dataset/d.kiki_plus/S34.stl) | 3 | 51.472 | 154.428 | 102.952 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S35](dataset/d.kiki_plus/S35.stl) | 1 | 30.639 | 91.917 | 61.278 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S36](dataset/d.kiki_plus/S36.stl) | 1 | 126.068 | 378.204 | 252.136 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S38](dataset/d.kiki_plus/S38.stl) | 3 | 21.918 | 65.766 | 43.844 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S39](dataset/d.kiki_plus/S39.stl) | 2 | 23.428 | 70.290 | 46.860 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S4](dataset/d.kiki_plus/S4.stl) | 3 | 31.644 | 94.944 | 63.296 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S40](dataset/d.kiki_plus/S40.stl) | 1 | 37.574 | 112.722 | 75.148 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S41](dataset/d.kiki_plus/S41.stl) | 1 | 36.315 | 108.945 | 72.630 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S42](dataset/d.kiki_plus/S42.stl) | 1 | 35.625 | 106.875 | 71.250 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S43](dataset/d.kiki_plus/S43.stl) | 1 | 35.242 | 105.726 | 70.484 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S44](dataset/d.kiki_plus/S44.stl) | 1 | 35.363 | 106.089 | 70.726 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S45](dataset/d.kiki_plus/S45.stl) | 1 | 34.921 | 104.763 | 69.842 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S5](dataset/d.kiki_plus/S5.stl) | 7 | 41.492 | 124.512 | 83.008 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S6](dataset/d.kiki_plus/S6.stl) | 5 | 68.976 | 206.952 | 137.968 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S7](dataset/d.kiki_plus/S7.stl) | 2 | 61.013 | 183.045 | 122.030 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S8](dataset/d.kiki_plus/S8.stl) | 1 | 48.998 | 146.994 | 97.996 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| [S9](dataset/d.kiki_plus/S9.stl) | 3 | 281.281 | 843.855 | 562.570 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |

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
