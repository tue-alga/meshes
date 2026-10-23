# Changes in this version

Every mesh is now named `<shape>_<source>`, so the same shape can appear once per source (for example `bunny_loopy`, `bunny_gao` and `bunny_jacobson`). STL files and thumbnails moved from `dataset/` to `preview/`; `dataset/` holds only the `.obj` files. The separate aerospace folder (`f.aerospace`) was merged into kiki: its genus-0 meshes are now in `c.kiki_zero`, the others in `d.kiki_plus`. `blocktopus_thingi` (previously `blocktopus`) moved from bouba to `c.kiki_zero`, and `carter_gao` (previously `carter`) from bouba to `d.kiki_plus`.

All meshes from the previous version were rebuilt from a fresh download of their original source. The table below lists every mesh whose geometry or pose differs from the previous version, plus the meshes that could not be rebuilt and were kept as they were. The remaining 210 meshes are identical to the previous version and are only renamed.

The previous versions of the changed meshes are still included, named `<shape>_snoep` and credited to the original source plus Maxim Snoep (*simplified* for the nightmares, *re-oriented* for the rest).

Rotations are given as the transform that maps the **new** (original-source) mesh onto the **previous** dataset mesh, so you can re-create a previous orientation from the new file.


## Credits

When a mesh was made by someone other than the original author, the source is credited as `<original source> + <person> (<what they did>)`:

- **meshed**: tessellated from a CAD file (STEP/BREP/IGES), because the source provides no mesh.
- **remeshed**: retriangulated, for example finer or more uniform.
- **simplified**: remeshed to fewer triangles (decimated or coarsened).
- **re-oriented**: rotated (and possibly moved) without changing the triangulation.
- **repaired**: small holes closed and stray parts or non-manifold spots removed (MeshFix).

Credit changes in this version:

- **Mambo** (118 meshes, `*_mambo`): now credited as *Franck Ledoux + Maxim Snoep (meshed)*. The Mambo repository only provides CAD files; the meshes are tessellations made with `tools/step_to_obj.py` (gmsh). The 110 meshes from the previous version that could be rebuilt are identical to before. `M4_mambo` and `M5_mambo` are Maxim Snoep's own remeshes and were kept as they were (meshing the upstream STEP with gmsh gives degenerate triangles for M4 and does not finish for M5).
- **Aerospace workshop models** (`dpw6g0`, `dpw6g1`, `dpw7`, `hlpw4`, `hlpw5`, `sbpw1`, `sbpw2`, `sbpw3`): credited as *NASA + Stevie-Ray Janssen (meshed)* and named `*_nlr`.
- **`*_snoep`**: previous versions of changed meshes, credited as *<original source> + Maxim Snoep (simplified / re-oriented)*.
- **`blocktopus_snoep`**: a new feature-preserving isotropic remesh of `blocktopus_thingi`, re-oriented upright with the face towards +Z, credited to Thingi10K + Maxim Snoep (remeshed, re-oriented).
- **`amogus_snoep`**: a new feature-preserving isotropic remesh of `amogus_sketchfab` (6.118 triangles), credited to Maxim Snoep.

- **Meshed from CAD by us**: the HexMe models (`*_hexme`), `involumeknot_nop`, `c25dflowthru_nasa`, `jwb_nasa` and the NIST parts (`*_nist`) are credited as *<source> + Maxim Snoep (meshed)*.


## Changed geometry or pose

| previous name | new name | what differs from the original |
|---|---|---|
| `7connected` | `7connected_nop` | scaled ×0.001; retriangulated (6890 → 76326 vertices); previous version kept as `7connected_snoep` |
| `8connected` | `8connected_nop` | rotated (axis permutation [[0,0,-1],[0,1,0],[1,0,0]]); scaled ×0.001; translated; retriangulated (10424 → 114112 vertices); previous version kept as `8connected_snoep` |
| `bunny` | `bunny_loopy` | rotated (xyz Euler -90°, -12.5°, -0°); translated; source corrected: Oded Stein → Marco Livesu; previous version kept as `bunny_snoep` |
| `buste` | `buste_loopy` | rotated (axis permutation [[0,1,0],[1,0,0],[0,0,-1]]); translated; previous version kept as `buste_snoep` |
| `chineselion` | `chineselion_loopy` | rotated (xyz Euler -16.2°, 0°, 0°); translated; previous version kept as `chineselion_snoep` |
| `encrusted` | `encrusted_nop` | rotated (axis permutation [[0,1,0],[0,0,1],[1,0,0]]); retriangulated (17660 → 24823 vertices); previous version kept as `encrusted_snoep` |
| `ghost` | `ghost_thingi` | rotated (axis permutation [[1,0,0],[0,0,1],[0,-1,0]]); translated; previous version kept as `ghost_snoep` |
| `goathead` | `goathead_stein` | rotated (axis permutation [[0,0,1],[0,1,0],[-1,0,0]]); translated; previous version kept as `goathead_snoep` |
| `screw` | `screw_nop` | rotated (axis permutation [[-1,0,0],[0,-1,0],[0,0,1]]); scaled ×0.001; translated; retriangulated (15424 → 88075 vertices); previous version kept as `screw_snoep` |
| `spot` | `spot_stein` | rotated (axis permutation [[-1,0,0],[0,1,0],[0,0,-1]]); translated; previous version kept as `spot_snoep` |
| `torusstep` | `torusstep_nop` | scaled ×0.001; retriangulated (4268 → 80371 vertices); previous version kept as `torusstep_snoep` |
| `traystep` | `traystep_nop` | scaled ×0.001; retriangulated (8562 → 79151 vertices); previous version kept as `traystep_snoep` |
| `twins` | `twins_nop` | rotated (axis permutation [[-1,0,0],[0,1,0],[0,0,-1]]); scaled ×0.001; translated; retriangulated (9272 → 63873 vertices); previous version kept as `twins_snoep` |

## Kept as in the previous version

| previous name | new name | reason |
|---|---|---|
| `amogus` | `amogus_sketchfab` | original source not found |
| `dpw6g0` | `dpw6g0_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `dpw6g1` | `dpw6g1_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `dpw7` | `dpw7_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `hlpw4` | `hlpw4_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `hlpw5` | `hlpw5_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `M4` | `M4_mambo` | own remesh kept (meshing the upstream STEP with gmsh gives degenerate triangles) |
| `M5` | `M5_mambo` | own remesh kept (meshing the upstream STEP with gmsh does not finish) |
| `sbpw1` | `sbpw1_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `sbpw2` | `sbpw2_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `sbpw3` | `sbpw3_nlr` | meshed by Stevie-Ray Janssen from the NASA workshop geometry; credited as NASA + Stevie-Ray Janssen (meshed) |
| `threecees` | `threecees_paardekooper` | original source not found |

## Source corrected (identical mesh)

| previous name | new name | correct source |
|---|---|---|
| `fandisk` | `fandisk_libigl` | [libigl tutorial data](https://github.com/libigl/libigl-tutorial-data) (`fandisk.off`) |
| `koala` | `koala_stein` | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/koala) (`koala_low_resolution.obj`, originally YahooJAPAN via Thingiverse) |

## Renamed only

`airplane1` → `airplane1_gao`, `airplane2` → `airplane2_gao`, `armadillo` → `armadillo_stein`, `armchair` → `armchair_gao`, `B0` → `B0_mambo`, `B1` → `B1_mambo`, `B10` → `B10_mambo`, `B11` → `B11_mambo`, `B12` → `B12_mambo`, `B13` → `B13_mambo`, `B14` → `B14_mambo`, `B15` → `B15_mambo`, `B16` → `B16_mambo`, `B17` → `B17_mambo`, `B18` → `B18_mambo`, `B19` → `B19_mambo`, `B2` → `B2_mambo`, `B20` → `B20_mambo`, `B21` → `B21_mambo`, `B23` → `B23_mambo`, `B25` → `B25_mambo`, `B27` → `B27_mambo`, `B28` → `B28_mambo`, `B29` → `B29_mambo`, `B3` → `B3_mambo`, `B30` → `B30_mambo`, `B31` → `B31_mambo`, `B32` → `B32_mambo`, `B33` → `B33_mambo`, `B34` → `B34_mambo`, `B35` → `B35_mambo`, `B36` → `B36_mambo`, `B37` → `B37_mambo`, `B38` → `B38_mambo`, `B39` → `B39_mambo`, `B4` → `B4_mambo`, `B40` → `B40_mambo`, `B41` → `B41_mambo`, `B42` → `B42_mambo`, `B43` → `B43_mambo`, `B44` → `B44_mambo`, `B45` → `B45_mambo`, `B46` → `B46_mambo`, `B47` → `B47_mambo`, `B48` → `B48_mambo`, `B49` → `B49_mambo`, `B5` → `B5_mambo`, `B50` → `B50_mambo`, `B51` → `B51_mambo`, `B52` → `B52_mambo`, `B53` → `B53_mambo`, `B54` → `B54_mambo`, `B55` → `B55_mambo`, `B56` → `B56_mambo`, `B57` → `B57_mambo`, `B58` → `B58_mambo`, `B59` → `B59_mambo`, `B6` → `B6_mambo`, `B60` → `B60_mambo`, `B61` → `B61_mambo`, `B62` → `B62_mambo`, `B63` → `B63_mambo`, `B64` → `B64_mambo`, `B65` → `B65_mambo`, `B66` → `B66_mambo`, `B67` → `B67_mambo`, `B68` → `B68_mambo`, `B69` → `B69_mambo`, `B7` → `B7_mambo`, `B70` → `B70_mambo`, `B71` → `B71_mambo`, `B72` → `B72_mambo`, `B73` → `B73_mambo`, `B74` → `B74_mambo`, `B75` → `B75_mambo`, `B76` → `B76_mambo`, `B8` → `B8_mambo`, `B9` → `B9_mambo`, `bimba` → `bimba_gao`, `bird` → `bird_gao`, `blade` → `blade_gao`, `block` → `block_gao`, `blocktopus` → `blocktopus_thingi`, `blub` → `blub_crane`, `bob` → `bob_crane`, `bone` → `bone_gao`, `botijo` → `botijo_gao`, `bottle1` → `bottle1_gao`, `bottle2` → `bottle2_gao`, `bumpysphere` → `bumpysphere_gao`, `bumpytorus` → `bumpytorus_gao`, `camel` → `camel_gao`, `camillehand` → `camillehand_gao`, `carter` → `carter_gao`, `cat` → `cat_stein`, `chair` → `chair_gao`, `chair1` → `chair1_gao`, `cup` → `cup_gao`, `cup1` → `cup1_gao`, `dancer` → `dancer_gao`, `dancer2` → `dancer2_gao`, `dancingchildren` → `dancingchildren_gao`, `david` → `david_gao`, `deformedarmadillo` → `deformedarmadillo_gao`, `dente` → `dente_gao`, `dilo` → `dilo_gao`, `dino` → `dino_gao`, `dino2` → `dino2_gao`, `dragonstand` → `dragonstand_gao`, `dragonstand2` → `dragonstand2_gao`, `dtorus` → `dtorus_gao`, `duck` → `duck_gao`, `duck2` → `duck2_gao`, `eight` → `eight_gao`, `elephant` → `elephant_gao`, `elk` → `elk_gao`, `eros` → `eros_gao`, `fertility` → `fertility_gao`, `fish1` → `fish1_gao`, `fish2` → `fish2_gao`, `foot` → `foot_gao`, `gargoyle` → `gargoyle_gao`, `genus3` → `genus3_gao`, `glass1` → `glass1_gao`, `glass2` → `glass2_gao`, `grayloc` → `grayloc_gao`, `greek` → `greek_gao`, `hand` → `hand_gao`, `head1` → `head1_gao`, `head2` → `head2_gao`, `holes3` → `holes3_gao`, `homer` → `homer_gao`, `horse` → `horse_gao`, `human1` → `human1_gao`, `human2` → `human2_gao`, `human3` → `human3_gao`, `igea` → `igea_gao`, `insect` → `insect_gao`, `isidorehorse` → `isidorehorse_gao`, `kiss` → `kiss_gao`, `kitten` → `kitten_gao`, `lion` → `lion_gao`, `M1` → `M1_mambo`, `M2` → `M2_mambo`, `M3` → `M3_mambo`, `M6` → `M6_mambo`, `M8` → `M8_mambo`, `M9` → `M9_mambo`, `mastercylinder` → `mastercylinder_gao`, `max` → `max_gao`, `moai` → `moai_gao`, `mouse` → `mouse_gao`, `oilpump` → `oilpump_gao`, `oni` → `oni_gao`, `pear` → `pear_gao`, `pensatore` → `pensatore_gao`, `pierrot` → `pierrot_gao`, `pig` → `pig_gao`, `pipehelix` → `pipehelix_nop`, `pipehelix7` → `pipehelix7_nop`, `ramses` → `ramses_gao`, `redbox` → `redbox_gao`, `retinal` → `retinal_gao`, `rocker` → `rocker_gao`, `rod` → `rod_gao`, `rollingstage` → `rollingstage_gao`, `S0` → `S0_mambo`, `S1` → `S1_mambo`, `S20` → `S20_mambo`, `S22` → `S22_mambo`, `S23` → `S23_mambo`, `S24` → `S24_mambo`, `S25` → `S25_mambo`, `S26` → `S26_mambo`, `S27` → `S27_mambo`, `S3` → `S3_mambo`, `S31` → `S31_mambo`, `S33` → `S33_mambo`, `S34` → `S34_mambo`, `S35` → `S35_mambo`, `S36` → `S36_mambo`, `S37` → `S37_mambo`, `S38` → `S38_mambo`, `S39` → `S39_mambo`, `S4` → `S4_mambo`, `S40` → `S40_mambo`, `S41` → `S41_mambo`, `S42` → `S42_mambo`, `S43` → `S43_mambo`, `S44` → `S44_mambo`, `S45` → `S45_mambo`, `S5` → `S5_mambo`, `S6` → `S6_mambo`, `S7` → `S7_mambo`, `S8` → `S8_mambo`, `S9` → `S9_mambo`, `santa` → `santa_gao`, `screwdriver` → `screwdriver_gao`, `sediapatch` → `sediapatch_gao`, `sphinx` → `sphinx_gao`, `teapot` → `teapot_gao`, `thaistatue` → `thaistatue_gao`, `toy1` → `toy1_gao`, `toy2` → `toy2_gao`, `twist` → `twist_nop`, `uumemento` → `uumemento_gao`, `venus` → `venus_gao`, `woodenfish` → `woodenfish_gao`, `wrench` → `wrench_gao`, `yeahright` → `yeahright_crane`


## Added

208 models that were not in the previous version (the `_snoep` meshes are previous versions under a new name and are listed under *Changed geometry or pose*).

| new name | folder | genus | triangles | source |
|---|---|---|---|---|
| `amogus_snoep` | a.bouba_zero | 0 | 6.118 | Maxim Snoep (feature-preserving isotropic remesh of `amogus_sketchfab`) |
| `armadillo_gao` | a.bouba_zero | 0 | 31.012 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `armadillo_jacobson` | a.bouba_zero | 0 | 99.976 | [Alec Jacobson](https://github.com/alecjacobson/common-3d-test-models) |
| `bimba_jacobson` | a.bouba_zero | 0 | 59.986 | [Alec Jacobson + Maxim Snoep (simplified)](https://github.com/alecjacobson/common-3d-test-models) |
| `bimba_loopy` | a.bouba_zero | 0 | 23.540 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `blade_loopy` | a.bouba_zero | 0 | 29.060 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `bladefem_loopy` | c.kiki_zero | 0 | 12.168 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `blocktopus_snoep` | c.kiki_zero | 0 | 15.134 | [Thingi10K + Maxim Snoep (remeshed, re-oriented)](https://ten-thousand-models.appspot.com/detail.html?file_id=86849) |
| `boat_loopy` | a.bouba_zero | 0 | 22.774 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `boat_stein` | a.bouba_zero | 0 | 32.416 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/boat) |
| `bone1_loopy` | a.bouba_zero | 0 | 3.128 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `bonefemur_loopy` | a.bouba_zero | 0 | 9.328 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `brucewick_stein` | a.bouba_zero | 0 | 2.858 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/brucewick) |
| `bunny_gao` | a.bouba_zero | 0 | 22.490 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `bunny_jacobson` | a.bouba_zero | 0 | 70.372 | [Alec Jacobson + Maxim Snoep (repaired)](https://github.com/alecjacobson/common-3d-test-models) |
| `bunny_stein` | a.bouba_zero | 0 | 6.598 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/bunny) |
| `buste_gao` | a.bouba_zero | 0 | 34.678 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `cactus_loopy` | a.bouba_zero | 0 | 1.396 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `camillehand_loopy` | a.bouba_zero | 0 | 7.406 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `cat_loopy` | a.bouba_zero | 0 | 4.660 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `cheese_stein` | a.bouba_zero | 0 | 60.000 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/cheese) |
| `chineselion_gao` | a.bouba_zero | 0 | 50.384 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `clef_loopy` | c.kiki_zero | 0 | 2.780 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `cup_loopy` | c.kiki_zero | 0 | 424 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `dog_loopy` | a.bouba_zero | 0 | 6.164 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `ellipse_loopy` | a.bouba_zero | 0 | 1.104 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `eraserball_loopy` | c.kiki_zero | 0 | 5.244 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `falconstatue_stein` | a.bouba_zero | 0 | 51.674 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/falconstatue) |
| `fish_stein` | a.bouba_zero | 0 | 21.568 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/fish) |
| `hand_loopy` | a.bouba_zero | 0 | 4.944 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `hand_stein` | a.bouba_zero | 0 | 15.982 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/hand) |
| `horse_jacobson` | a.bouba_zero | 0 | 96.966 | [Alec Jacobson](https://github.com/alecjacobson/common-3d-test-models) |
| `humanman_stein` | a.bouba_zero | 0 | 13.776 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/human) |
| `humanneutral_stein` | a.bouba_zero | 0 | 18.870 | [Oded Stein + Maxim Snoep (repaired)](https://github.com/odedstein/meshes/tree/master/objects/human) |
| `humanwoman_stein` | a.bouba_zero | 0 | 13.776 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/human) |
| `igea_jacobson` | a.bouba_zero | 0 | 59.998 | [Alec Jacobson + Maxim Snoep (simplified)](https://github.com/alecjacobson/common-3d-test-models) |
| `inigo_crane` | a.bouba_zero | 0 | 59.986 | [Keenan Crane + Maxim Snoep (repaired, simplified)](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `kong_loopy` | a.bouba_zero | 0 | 31.552 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `max_jacobson` | a.bouba_zero | 0 | 102.420 | [Alec Jacobson + Maxim Snoep (repaired)](https://github.com/alecjacobson/common-3d-test-models) |
| `mushroom_stein` | a.bouba_zero | 0 | 23.166 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/mushroom) |
| `nefertiti_crane` | a.bouba_zero | 0 | 59.994 | [Keenan Crane + Maxim Snoep (simplified)](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `nefertiti_stein` | a.bouba_zero | 0 | 59.994 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/nefertiti) |
| `ogre_crane` | a.bouba_zero | 0 | 38.888 | [Keenan Crane + Maxim Snoep (repaired)](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `ogre_jacobson` | a.bouba_zero | 0 | 51.334 | [Alec Jacobson + Maxim Snoep (repaired, simplified)](https://github.com/alecjacobson/common-3d-test-models) |
| `penguin_stein` | a.bouba_zero | 0 | 6.720 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/penguin) |
| `pig_crane` | a.bouba_zero | 0 | 8.864 | [Keenan Crane + Maxim Snoep (repaired)](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `pig_loopy` | a.bouba_zero | 0 | 6.328 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `rabbit_loopy` | a.bouba_zero | 0 | 16.000 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `scorpion_stein` | a.bouba_zero | 0 | 12.626 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/scorpion) |
| `sphere_stein` | a.bouba_zero | 0 | 1.280 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/sphere) |
| `sphinx_loopy` | a.bouba_zero | 0 | 20.364 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `spot_crane` | a.bouba_zero | 0 | 5.856 | [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `strawberry_stein` | a.bouba_zero | 0 | 59.980 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/strawberry) |
| `stuffedtoy_stein` | a.bouba_zero | 0 | 13.334 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/stuffedtoy) |
| `torque1_loopy` | a.bouba_zero | 0 | 5.696 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `torque_loopy` | a.bouba_zero | 0 | 3.300 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `trebol_loopy` | a.bouba_zero | 0 | 36.348 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `tree_stein` | a.bouba_zero | 0 | 59.996 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/tree) |
| `wave_loopy` | c.kiki_zero | 0 | 1.148 | [Marco Livesu + Maxim Snoep (repaired)](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `boot_stein` | b.bouba_plus | 12 | 39.906 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/boot) |
| `buddha_stanford` | b.bouba_plus | 10 | 58.874 | [Stanford + Maxim Snoep (repaired, simplified)](https://graphics.stanford.edu/data/3Dscanrep/) |
| `centaur_tds` | b.bouba_plus | 9 | 59.978 | [Three D Scans + Maxim Snoep (repaired, simplified)](https://huggingface.co/datasets/alecjacobson/threedscans) |
| `cow_stein` | b.bouba_plus | 1 | 59.982 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/cow) |
| `dancer_loopy` | b.bouba_plus | 1 | 49.996 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `demosthenes_stein` | b.bouba_plus | 1 | 59.930 | [Oded Stein + Maxim Snoep (repaired, simplified)](https://github.com/odedstein/meshes/tree/master/objects/demosthenes) |
| `desertrose_crane` | b.bouba_plus | 1 | 63.360 | [Keenan Crane + Maxim Snoep (repaired)](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `dragon_stanford` | b.bouba_plus | 3 | 59.508 | [Stanford + Maxim Snoep (repaired, simplified)](https://graphics.stanford.edu/data/3Dscanrep/) |
| `greyhounds_tds` | b.bouba_plus | 5 | 59.978 | [Three D Scans + Maxim Snoep (repaired, simplified)](https://huggingface.co/datasets/alecjacobson/threedscans) |
| `holes2_loopy` | b.bouba_plus | 2 | 5.848 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `indorelax_loopy` | b.bouba_plus | 2 | 24.260 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `kiss_loopy` | b.bouba_plus | 3 | 25.484 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `kitten_loopy` | b.bouba_plus | 1 | 6.356 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `lionstatue_stein` | b.bouba_plus | 3 | 74.326 | [Oded Stein + Maxim Snoep (repaired)](https://github.com/odedstein/meshes/tree/master/objects/lionstatue) |
| `parsnip_stein` | b.bouba_plus | 12 | 59.474 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/parsnip) |
| `pittsburghbridge_crane` | b.bouba_plus | 3 | 59.998 | [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `pizza_stein` | b.bouba_plus | 65 | 57.584 | [Oded Stein + Maxim Snoep (repaired)](https://github.com/odedstein/meshes/tree/master/objects/pizza) |
| `skull_stein` | b.bouba_plus | 2 | 10.312 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/skull) |
| `teapot_loopy` | b.bouba_plus | 1 | 13.088 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `torus_stein` | b.bouba_plus | 1 | 4.608 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/torus) |
| `violin_stein` | b.bouba_plus | 5 | 59.998 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/violin) |
| `3035_gao` | c.kiki_zero | 0 | 7.132 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `aries70_gao` | c.kiki_zero | 0 | 8.710 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `chesspawn_mambo` | c.kiki_zero | 0 | 23.222 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| `chessrook_mambo` | c.kiki_zero | 0 | 18.336 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| `completepart16_gao` | c.kiki_zero | 0 | 7.676 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `completepart63_gao` | c.kiki_zero | 0 | 7.676 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `coverrear_gao` | c.kiki_zero | 0 | 79.960 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `cube_stein` | c.kiki_zero | 0 | 48 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/cube) |
| `cubecarved_loopy` | c.kiki_zero | 0 | 3.636 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `cubeminussphere_loopy` | c.kiki_zero | 0 | 4.128 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `cylinderplate_loopy` | c.kiki_zero | 0 | 1.812 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `fandisk_jacobson` | c.kiki_zero | 0 | 12.946 | [Alec Jacobson](https://github.com/alecjacobson/common-3d-test-models) |
| `featureloft_mambo` | c.kiki_zero | 0 | 18.480 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| `gear_loopy` | c.kiki_zero | 0 | 7.858 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `hammer_stein` | c.kiki_zero | 0 | 60.160 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/hammer) |
| `jwb_nasa` | c.kiki_zero | 0 | 43.342 | [NASA + Maxim Snoep (meshed)](https://lbpw.larc.nasa.gov/) |
| `legoblock_mambo` | c.kiki_zero | 0 | 42.984 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| `legoman_mambo` | c.kiki_zero | 0 | 14.114 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| `mech10_loopy` | c.kiki_zero | 0 | 508 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `mechanical02_loopy` | c.kiki_zero | 0 | 7.172 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `mechanical05_loopy` | c.kiki_zero | 0 | 8.160 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `mechpiece_loopy` | c.kiki_zero | 0 | 4.174 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `plane_stein` | c.kiki_zero | 0 | 17.456 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/plane) |
| `plate1_loopy` | c.kiki_zero | 0 | 11.956 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `plate2_loopy` | c.kiki_zero | 0 | 8.394 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `plate3_loopy` | c.kiki_zero | 0 | 4.930 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `plate4_loopy` | c.kiki_zero | 0 | 35.586 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `prism_loopy` | c.kiki_zero | 0 | 1.976 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `springer_stein` | c.kiki_zero | 0 | 19.368 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/springer) |
| `sword_stein` | c.kiki_zero | 0 | 44.582 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/sword) |
| `trisclosed_loopy` | c.kiki_zero | 0 | 1.376 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `vessel_loopy` | c.kiki_zero | 0 | 5.312 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `wedge_loopy` | c.kiki_zero | 0 | 4.468 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `wingnut_stein` | c.kiki_zero | 0 | 6.090 | [Oded Stein](https://github.com/odedstein/meshes/tree/master/objects/wingnut) |
| `anc101_gao` | d.kiki_plus | 5 | 7.956 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `aries155_gao` | d.kiki_plus | 6 | 4.692 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `bearingplate_loopy` | d.kiki_plus | 5 | 9.830 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `bolt_loopy` | d.kiki_plus | 1 | 9.504 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `bracket2_gao` | d.kiki_plus | 3 | 2.664 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `bracketinches_loopy` | d.kiki_plus | 6 | 16.622 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `c25dflowthru_nasa` | d.kiki_plus | 1 | 65.636 | [NASA + Maxim Snoep (meshed)](https://lbpw.larc.nasa.gov/) |
| `cami1_gao` | d.kiki_plus | 5 | 2.436 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `cami2_gao` | d.kiki_plus | 1 | 1.308 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `casting_gao` | d.kiki_plus | 9 | 52.100 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `cheese2_gao` | d.kiki_plus | 28 | 9.660 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `cheese3_gao` | d.kiki_plus | 81 | 28.632 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `cheese_gao` | d.kiki_plus | 176 | 63.180 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `cimplex_gao` | d.kiki_plus | 6 | 29.632 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `clevis23_gao` | d.kiki_plus | 9 | 4.988 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `ctc01_nist` | d.kiki_plus | 10 | 48.318 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `ctc03_nist` | d.kiki_plus | 17 | 79.634 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `deckel_gao` | d.kiki_plus | 4 | 40.048 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `deckel_loopy` | d.kiki_plus | 4 | 10.012 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `des6_loopy` | d.kiki_plus | 1 | 11.390 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `ftc06_nist` | d.kiki_plus | 10 | 138.928 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `ftc07_nist` | d.kiki_plus | 15 | 517.782 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `ftc08_nist` | d.kiki_plus | 25 | 334.756 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `ftc09_nist` | d.kiki_plus | 34 | 83.908 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `ftc10_nist` | d.kiki_plus | 22 | 212.646 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `ftc11_nist` | d.kiki_plus | 1 | 27.066 | [NIST + Maxim Snoep (meshed)](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0) |
| `gehaeuse_gao` | d.kiki_plus | 3 | 8.490 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `gimbal_gao` | d.kiki_plus | 5 | 1.692 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `gyroidpuzzle_loopy` | d.kiki_plus | 15 | 26.210 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `hanger_gao` | d.kiki_plus | 2 | 32.224 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `hanger_loopy` | d.kiki_plus | 2 | 8.056 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `hinge_loopy` | d.kiki_plus | 5 | 19.104 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `holes10_gao` | d.kiki_plus | 100 | 10.012 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `house_stein` | d.kiki_plus | 36 | 58.020 | [Oded Stein + Maxim Snoep (repaired, simplified)](https://github.com/odedstein/meshes/tree/master/objects/house) |
| `impeller_loopy` | d.kiki_plus | 1 | 26.126 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `impellerhousing_gao` | d.kiki_plus | 1 | 2.048 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `joint_gao` | d.kiki_plus | 2 | 16.032 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `joint_loopy` | d.kiki_plus | 2 | 8.766 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `knob_loopy` | d.kiki_plus | 1 | 13.816 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `leverarm_loopy` | d.kiki_plus | 2 | 8.060 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `lock_gao` | d.kiki_plus | 3 | 170.176 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `mechanical06_loopy` | d.kiki_plus | 1 | 9.090 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `mechanical08_loopy` | d.kiki_plus | 1 | 2.928 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `motortail_loopy` | d.kiki_plus | 13 | 15.248 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `orion_nasa` | d.kiki_plus | 7 | 51.728 | [NASA + Maxim Snoep (repaired)](https://github.com/nasa/NASA-3D-Resources/tree/master/3D%20Printing/Orion%20Capsule) |
| `part10_gao` | d.kiki_plus | 3 | 2.584 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `part11_gao` | d.kiki_plus | 6 | 9.080 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `part_gao` | d.kiki_plus | 3 | 34.120 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `pinion_gao` | d.kiki_plus | 1 | 2.596 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `pinion_loopy` | d.kiki_plus | 1 | 42.878 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `rocker_jacobson` | d.kiki_plus | 1 | 20.088 | [Alec Jacobson](https://github.com/alecjacobson/common-3d-test-models) |
| `rod_loopy` | d.kiki_plus | 2 | 4.408 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `sbracket_gao` | d.kiki_plus | 2 | 2.604 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `sculpt_gao` | d.kiki_plus | 2 | 29.368 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `sculpt_loopy` | d.kiki_plus | 2 | 7.342 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `simp_hexme` | d.kiki_plus | 1 | 10.048 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `sls_nasa` | d.kiki_plus | 7 | 60.000 | [NASA + Maxim Snoep (repaired, simplified)](https://github.com/nasa/NASA-3D-Resources/tree/master/3D%20Printing/Space%20Launch%20System%20(SLS)%20Block%201) |
| `socket1_gao` | d.kiki_plus | 7 | 2.412 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `socket2_gao` | d.kiki_plus | 7 | 2.420 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `supportframe_gao` | d.kiki_plus | 5 | 1.124 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `swivel2_gao` | d.kiki_plus | 2 | 816 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `team2_gao` | d.kiki_plus | 9 | 8.638 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `tower_stein` | d.kiki_plus | 2 | 59.936 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/tower) |
| `triangularbase_mambo` | d.kiki_plus | 4 | 30.152 | [Franck Ledoux](https://gitlab.com/franck.ledoux/mambo) |
| `trisopen_loopy` | d.kiki_plus | 1 | 1.440 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `ujoint_loopy` | d.kiki_plus | 2 | 11.152 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `well_stein` | d.kiki_plus | 48 | 59.832 | [Oded Stein + Maxim Snoep (simplified)](https://github.com/odedstein/meshes/tree/master/objects/well) |
| `wrench_loopy` | d.kiki_plus | 1 | 4.496 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `acuteline_hexme` | e.nightmares | 0 | 1.316 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `antipentapyramid_hexme` | e.nightmares | 0 | 11.826 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `antipyramid_hexme` | e.nightmares | 0 | 12.018 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `antiskijump_hexme` | e.nightmares | 0 | 1.448 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `beveledshoulder2_loopy` | e.nightmares | 1 | 44 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `boxpcyls_hexme` | e.nightmares | 1 | 2.244 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `catalanwire_thingi` | e.nightmares | 119 | 57.600 | [Thingi10K](https://ten-thousand-models.appspot.com/detail.html?file_id=509316) |
| `constantwidth_crane` | e.nightmares | 0 | 39.600 | [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `crosscyls_hexme` | e.nightmares | 0 | 686 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `csaszar_crane` | e.nightmares | 1 | 896 | [Keenan Crane + Maxim Snoep (remeshed)](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `halvedobliquescarf3_loopy` | e.nightmares | 0 | 68 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `hilbertcube_thingi` | e.nightmares | 8 | 508 | [Thingi10K](https://ten-thousand-models.appspot.com/detail.html?file_id=53757) |
| `icosahedron_hexme` | e.nightmares | 0 | 12.500 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `inlaydovetail3_loopy` | e.nightmares | 0 | 60 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `involumeknot_nop` | e.nightmares | 1 | 26.750 | [Sébastien Mestrallet + Maxim Snoep (meshed)](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes) |
| `knot1_cgal` | e.nightmares | 1 | 6.400 | [CGAL](https://github.com/CGAL/cgal/tree/main/Data/data/meshes) |
| `knot_cgal` | e.nightmares | 1 | 4.160 | [CGAL](https://github.com/CGAL/cgal/tree/main/Data/data/meshes) |
| `limitcycle_hexme` | e.nightmares | 1 | 16.826 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `limitcycleg0_hexme` | e.nightmares | 0 | 15.276 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `metatron_loopy` | e.nightmares | 11 | 14.382 | [Marco Livesu](https://github.com/mlivesu/LoopyCuts/tree/master/test_data) |
| `octaflower_gao` | e.nightmares | 0 | 15.834 | [Xifeng Gao](https://cims.nyu.edu/gcl/publications.html) |
| `octahedron_hexme` | e.nightmares | 0 | 6.728 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `oloid_crane` | e.nightmares | 0 | 8.192 | [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) |
| `pentapyramid_hexme` | e.nightmares | 0 | 1.918 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `pyramid_hexme` | e.nightmares | 0 | 2.544 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |
| `skijump_hexme` | e.nightmares | 0 | 1.692 | [HexMe + Maxim Snoep (meshed)](https://github.com/cgg-bern/hex-me-if-you-can) |