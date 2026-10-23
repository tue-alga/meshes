"""Full citations for the README footnotes, keyed by the (collection) URL in sources.csv.

DOIs were checked against Crossref/DataCite. Add an entry here when adding a new source;
sources without an entry fall back to "<source> — <url>".
"""

CITATIONS = {
    "https://cims.nyu.edu/gcl/publications.html":
        "GAO X., SHEN H., PANOZZO D.: Feature preserving octree-based hexahedral meshing. "
        "_Computer Graphics Forum (SGP) 38_, 5 (2019). [doi:10.1111/cgf.13795](https://doi.org/10.1111/cgf.13795)",
    "https://gitlab.com/franck.ledoux/mambo":
        "LEDOUX F.: MAMBO: a CAD model dataset for hexahedral meshing. [gitlab.com/franck.ledoux/mambo](https://gitlab.com/franck.ledoux/mambo)",
    "https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes":
        "MESTRALLET S.: Nightmare of polycubes. "
        "[github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes)",
    "https://github.com/cgg-bern/hex-me-if-you-can":
        "BEAUFORT P.-A., REBEROL M., KALMYKOV D., LIU H., LEDOUX F., BOMMES D.: Hex me if you can. "
        "_Computer Graphics Forum (SGP) 41_, 5 (2022). [doi:10.1111/cgf.14608](https://doi.org/10.1111/cgf.14608)",
    "https://github.com/mlivesu/LoopyCuts/tree/master/test_data":
        "LIVESU M., PIETRONI N., PUPPO E., SHEFFER A., CIGNONI P.: LoopyCuts: practical feature-preserving block "
        "decomposition for strongly hex-dominant meshing. _ACM Transactions on Graphics 39_, 4 (2020). "
        "[doi:10.1145/3386569.3392472](https://doi.org/10.1145/3386569.3392472)",
    "https://github.com/odedstein/meshes":
        "STEIN O.: meshes. [github.com/odedstein/meshes](https://github.com/odedstein/meshes)",
    "https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/":
        "CRANE K.: Keenan's 3D model repository. "
        "[cs.cmu.edu/~kmcrane/Projects/ModelRepository](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/)",
    "https://github.com/alecjacobson/common-3d-test-models":
        "JACOBSON A.: Common 3D test models. "
        "[github.com/alecjacobson/common-3d-test-models](https://github.com/alecjacobson/common-3d-test-models)",
    "https://github.com/libigl/libigl-tutorial-data":
        "JACOBSON A., PANOZZO D., ET AL.: libigl tutorial data. "
        "[github.com/libigl/libigl-tutorial-data](https://github.com/libigl/libigl-tutorial-data)",
    "https://ten-thousand-models.appspot.com":
        "ZHOU Q., JACOBSON A.: Thingi10K: a dataset of 10,000 3D-printing models. arXiv:1605.04797 (2016). "
        "[doi:10.48550/arXiv.1605.04797](https://doi.org/10.48550/arXiv.1605.04797)",
    "https://graphics.stanford.edu/data/3Dscanrep/":
        "STANFORD COMPUTER GRAPHICS LABORATORY: The Stanford 3D scanning repository. "
        "[graphics.stanford.edu/data/3Dscanrep](https://graphics.stanford.edu/data/3Dscanrep/)",
    "https://huggingface.co/datasets/alecjacobson/threedscans":
        "LARIC O.: Three D Scans. [threedscans.com](https://threedscans.com), via "
        "[huggingface.co/datasets/alecjacobson/threedscans](https://huggingface.co/datasets/alecjacobson/threedscans)",
    "https://github.com/CGAL/cgal/tree/main/Data/data/meshes":
        "THE CGAL PROJECT: CGAL test meshes. "
        "[github.com/CGAL/cgal/tree/main/Data/data/meshes](https://github.com/CGAL/cgal/tree/main/Data/data/meshes)",
    "https://github.com/nasa/NASA-3D-Resources":
        "NASA: NASA 3D Resources. [github.com/nasa/NASA-3D-Resources](https://github.com/nasa/NASA-3D-Resources)",
    "https://lbpw.larc.nasa.gov/":
        "NASA: AIAA Sonic Boom Prediction Workshop geometry. [lbpw.larc.nasa.gov](https://lbpw.larc.nasa.gov/)",
    "https://aiaa-dpw.larc.nasa.gov/":
        "NASA: AIAA CFD Drag Prediction Workshop geometry. [aiaa-dpw.larc.nasa.gov](https://aiaa-dpw.larc.nasa.gov/)",
    "https://www.nasa.gov/reference/aiaa-cfd-high-lift-prediction-workshop/":
        "NASA: AIAA CFD High Lift Prediction Workshop geometry. "
        "[nasa.gov/reference/aiaa-cfd-high-lift-prediction-workshop](https://www.nasa.gov/reference/aiaa-cfd-high-lift-prediction-workshop/)",
    "https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0":
        "NIST: MBE PMI validation and conformance testing models. "
        "[nist.gov](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0)",
    "https://www.quadmesh.cloud/":
        "PIETRONI N., NUVOLI S., ALDERIGHI T., CIGNONI P., TARINI M., PANOZZO D.: Reliable feature-line driven "
        "quad-remeshing. _ACM Transactions on Graphics 40_, 4 (2021). "
        "[doi:10.1145/3450626.3459941](https://doi.org/10.1145/3450626.3459941)",
    "https://webspace.science.uu.nl/~telea001/Shapes/SkelBenchmark":
        "SOBIECKI A., YASAN H. C., JALBA A. C., TELEA A. C.: Qualitative comparison of contraction-based curve "
        "skeletonization methods. In _Mathematical Morphology and Its Applications to Signal and Image Processing "
        "(ISMM)_ (2013). [doi:10.1007/978-3-642-38294-9_36](https://doi.org/10.1007/978-3-642-38294-9_36)",
    "https://data.nist.gov/od/id/mds2-2215":
        "LIAN Z., GODIL A., BUSTOS B., DAOUDI M., HERMANS J., KAWAMURA S., KURITA Y., LAVOUÉ G., ET AL.: "
        "SHREC'11 track: shape retrieval on non-rigid 3D watertight meshes. In _Eurographics Workshop on 3D Object "
        "Retrieval_ (2011). [doi:10.2312/3DOR/3DOR11/079-088](https://doi.org/10.2312/3DOR/3DOR11/079-088)",
    "https://engineering.purdue.edu/cdesign/wp/?p=1386":
        "JAYANTI S., KALYANARAMAN Y., IYER N., RAMANI K.: Developing an engineering shape benchmark for CAD models. "
        "_Computer-Aided Design 38_, 9 (2006). [doi:10.1016/j.cad.2006.06.007](https://doi.org/10.1016/j.cad.2006.06.007)",
    "https://cvg.cit.tum.de/data/datasets/topkids":
        "LÄHNER Z., RODOLÀ E., BRONSTEIN M. M., CREMERS D., ET AL.: SHREC'16: matching of deformable shapes with "
        "topological noise. In _Eurographics Workshop on 3D Object Retrieval_ (2016). "
        "[cvg.cit.tum.de/data/datasets/topkids](https://cvg.cit.tum.de/data/datasets/topkids)",
    "https://www.cs.ubc.ca/labs/imager/tr/2013/polycut/":
        "LIVESU M., VINING N., SHEFFER A., GREGSON J., SCATENI R.: PolyCut: monotone graph-cuts for polycube "
        "base-complex construction. _ACM Transactions on Graphics 32_, 6 (2013). "
        "[doi:10.1145/2508363.2508388](https://doi.org/10.1145/2508363.2508388)",
    "https://knotplot.com/":
        "SCHAREIN R.: KnotPlot. [knotplot.com](https://knotplot.com/)",
    "https://research.google/pubs/pub51437":
        "DOWNS L., FRANCIS A., KOENIG N., KINMAN B., HICKMAN R., REYMANN K., MCHUGH T. B., VANHOUCKE V.: "
        "Google Scanned Objects: a high-quality dataset of 3D scanned household items. In _IEEE International "
        "Conference on Robotics and Automation (ICRA)_ (2022). "
        "[doi:10.1109/ICRA46639.2022.9811809](https://doi.org/10.1109/ICRA46639.2022.9811809)",
    "https://sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0":
        "FACUNLA J.: Among Us crewmate. Sketchfab. "
        "[sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0](https://sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0)",
    "Bas Paardekooper":
        "PAARDEKOOPER B.: threecees. Personal communication.",
}
