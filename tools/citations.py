"""Full citations for the README footnotes, keyed by the (collection) URL in sources.csv
(or by the source name when there is no URL).

Where a dataset belongs to a paper, the paper is cited. DOIs were checked against Crossref/DataCite.
Add an entry here when adding a new source; sources without an entry fall back to "<source>. <url>".
"""

CITATIONS = {
    # --- polycube / hex-meshing and remeshing papers
    "https://cims.nyu.edu/gcl/publications.html":
        "GAO X., SHEN H., PANOZZO D.: Feature preserving octree-based hexahedral meshing. "
        "_Computer Graphics Forum (SGP) 38_, 5 (2019). [doi:10.1111/cgf.13795](https://doi.org/10.1111/cgf.13795)",
    "https://github.com/mlivesu/LoopyCuts/tree/master/test_data":
        "LIVESU M., PIETRONI N., PUPPO E., SHEFFER A., CIGNONI P.: LoopyCuts: practical feature-preserving block "
        "decomposition for strongly hex-dominant meshing. _ACM Transactions on Graphics 39_, 4 (2020). "
        "[doi:10.1145/3386569.3392472](https://doi.org/10.1145/3386569.3392472)",
    "https://www.cs.ubc.ca/labs/imager/tr/2013/polycut/":
        "LIVESU M., VINING N., SHEFFER A., GREGSON J., SCATENI R.: PolyCut: monotone graph-cuts for polycube "
        "base-complex construction. _ACM Transactions on Graphics 32_, 6 (2013). "
        "[doi:10.1145/2508363.2508388](https://doi.org/10.1145/2508363.2508388)",
    "https://github.com/cgg-bern/hex-me-if-you-can":
        "BEAUFORT P.-A., REBEROL M., KALMYKOV D., LIU H., LEDOUX F., BOMMES D.: Hex me if you can. "
        "_Computer Graphics Forum (SGP) 41_, 5 (2022). [doi:10.1111/cgf.14608](https://doi.org/10.1111/cgf.14608)",
    "https://www.quadmesh.cloud/":
        "PIETRONI N., NUVOLI S., ALDERIGHI T., CIGNONI P., TARINI M., PANOZZO D.: Reliable feature-line driven "
        "quad-remeshing. _ACM Transactions on Graphics 40_, 4 (2021). "
        "[doi:10.1145/3450626.3459941](https://doi.org/10.1145/3450626.3459941)",
    "https://gitlab.com/franck.ledoux/mambo":
        "LEDOUX F.: MAMBO: Model dAtabase Mesh BlOcking. "
        "[gitlab.com/franck.ledoux/mambo](https://gitlab.com/franck.ledoux/mambo)",
    "https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes":
        "MESTRALLET S., BOURCIER C., LEDOUX F.: Nightmare of polycubes, version 2.0.0 (dataset). "
        "[github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes](https://github.com/LIHPC-Computational-Geometry/nightmare_of_polycubes)",
    "https://github.com/cnr-isti-vclab/HexaLab/tree/master/datasets/2016%20-%20Skeleton-driven%20Adaptive%20Hexahedral%20Meshing%20of%20Tubular%20Shapes":
        "LIVESU M., MUNTONI A., PUPPO E., SCATENI R.: Skeleton-driven adaptive hexahedral meshing of tubular shapes. "
        "_Computer Graphics Forum 35_, 7 (2016). [doi:10.1111/cgf.13021](https://doi.org/10.1111/cgf.13021). Input meshes via "
        "[HexaLab](https://github.com/cnr-isti-vclab/HexaLab)",
    "https://github.com/cnr-isti-vclab/HexaLab/tree/master/datasets/2016%20-%20Structured%20Volume%20Decomposition%20via%20Generalized%20Sweeping":
        "GAO X., MARTIN T., DENG S., COHEN E., DENG Z., CHEN G.: Structured volume decomposition via generalized sweeping. "
        "_IEEE Transactions on Visualization and Computer Graphics 22_, 7 (2016). "
        "[doi:10.1109/TVCG.2015.2473835](https://doi.org/10.1109/TVCG.2015.2473835). Input meshes via "
        "[HexaLab](https://github.com/cnr-isti-vclab/HexaLab)",
    # --- shape benchmarks
    "https://ten-thousand-models.appspot.com":
        "ZHOU Q., JACOBSON A.: Thingi10K: a dataset of 10,000 3D-printing models. arXiv:1605.04797 (2016). "
        "[doi:10.48550/arXiv.1605.04797](https://doi.org/10.48550/arXiv.1605.04797)",
    "https://data.nist.gov/od/id/mds2-2215":
        "LIAN Z., GODIL A., BUSTOS B., DAOUDI M., HERMANS J., KAWAMURA S., KURITA Y., LAVOUÉ G., ET AL.: "
        "SHREC'11 track: shape retrieval on non-rigid 3D watertight meshes. In _Eurographics Workshop on 3D Object "
        "Retrieval_ (2011). [doi:10.2312/3DOR/3DOR11/079-088](https://doi.org/10.2312/3DOR/3DOR11/079-088)",
    "https://cvg.cit.tum.de/data/datasets/topkids":
        "LÄHNER Z., RODOLÀ E., BRONSTEIN M. M., CREMERS D., ET AL.: SHREC'16: matching of deformable shapes with "
        "topological noise. In _Eurographics Workshop on 3D Object Retrieval_ (2016). "
        "[cvg.cit.tum.de/data/datasets/topkids](https://cvg.cit.tum.de/data/datasets/topkids)",
    "https://engineering.purdue.edu/cdesign/wp/?p=1386":
        "JAYANTI S., KALYANARAMAN Y., IYER N., RAMANI K.: Developing an engineering shape benchmark for CAD models. "
        "_Computer-Aided Design 38_, 9 (2006). [doi:10.1016/j.cad.2006.06.007](https://doi.org/10.1016/j.cad.2006.06.007)",
    "https://webspace.science.uu.nl/~telea001/Shapes/SkelBenchmark":
        "TELEA A.: Skeletonization benchmark: 3D mesh shapes. "
        "[webspace.science.uu.nl/~telea001/Shapes/SkelBenchmark](https://webspace.science.uu.nl/~telea001/Shapes/SkelBenchmark)",
    "https://research.google/pubs/pub51437":
        "DOWNS L., FRANCIS A., KOENIG N., KINMAN B., HICKMAN R., REYMANN K., MCHUGH T. B., VANHOUCKE V.: "
        "Google Scanned Objects: a high-quality dataset of 3D scanned household items. In _IEEE International "
        "Conference on Robotics and Automation (ICRA)_ (2022). "
        "[doi:10.1109/ICRA46639.2022.9811809](https://doi.org/10.1109/ICRA46639.2022.9811809)",
    "https://graphics.stanford.edu/data/3Dscanrep/#vrip":
        "CURLESS B., LEVOY M.: A volumetric method for building complex models from range images. In _SIGGRAPH_ "
        "(1996). [doi:10.1145/237170.237269](https://doi.org/10.1145/237170.237269). Via the "
        "[Stanford 3D scanning repository](https://graphics.stanford.edu/data/3Dscanrep/)",
    "https://graphics.stanford.edu/data/3Dscanrep/#bunny":
        "TURK G., LEVOY M.: Zippered polygon meshes from range images. In _SIGGRAPH_ (1994). "
        "[doi:10.1145/192161.192241](https://doi.org/10.1145/192161.192241). Via the "
        "[Stanford 3D scanning repository](https://graphics.stanford.edu/data/3Dscanrep/)",
    "https://graphics.stanford.edu/data/3Dscanrep/#armadillo":
        "KRISHNAMURTHY V., LEVOY M.: Fitting smooth surfaces to dense polygon meshes. In _SIGGRAPH_ (1996). "
        "[doi:10.1145/237170.237270](https://doi.org/10.1145/237170.237270). Via the "
        "[Stanford 3D scanning repository](https://graphics.stanford.edu/data/3Dscanrep/)",
    # --- CAD / engineering
    "https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0":
        "LIPMAN R., LUBELL J.: Conformance checking of PMI representation in CAD model STEP data exchange files. "
        "_Computer-Aided Design 66_ (2015). [doi:10.1016/j.cad.2015.04.002](https://doi.org/10.1016/j.cad.2015.04.002). "
        "Models from the [NIST MBE PMI test system](https://www.nist.gov/ctl/smart-connected-systems-division/smart-connected-manufacturing-systems-group/mbe-pmi-0)",
    "https://aiaa-dpw.larc.nasa.gov/":
        "VASSBERG J. C., DEHAAN M. A., RIVERS S. M., WAHLS R. A.: Development of a common research model for applied "
        "CFD validation studies. In _26th AIAA Applied Aerodynamics Conference_ (2008). "
        "[doi:10.2514/6.2008-6919](https://doi.org/10.2514/6.2008-6919). Geometry from the "
        "[AIAA CFD Drag Prediction Workshop](https://aiaa-dpw.larc.nasa.gov/)",
    "https://www.nasa.gov/reference/aiaa-cfd-high-lift-prediction-workshop/":
        "LACY D. S., SCLAFANI A. J.: Development of the High Lift Common Research Model (HL-CRM): a representative "
        "high lift configuration for transonic transports. In _54th AIAA Aerospace Sciences Meeting_ (2016). "
        "[doi:10.2514/6.2016-0308](https://doi.org/10.2514/6.2016-0308). Geometry from the "
        "[AIAA CFD High Lift Prediction Workshop](https://www.nasa.gov/reference/aiaa-cfd-high-lift-prediction-workshop/)",
    "https://lbpw.larc.nasa.gov/":
        "PARK M. A., MORGENSTERN J. M.: Summary and statistical analysis of the first AIAA sonic boom prediction "
        "workshop. _Journal of Aircraft 53_, 2 (2016). [doi:10.2514/1.C033449](https://doi.org/10.2514/1.C033449). "
        "Geometry from the [AIAA Sonic Boom Prediction Workshop](https://lbpw.larc.nasa.gov/)",
    "https://gfx.cs.princeton.edu/proj/sugcon/models/":
        "DECARLO D., FINKELSTEIN A., RUSINKIEWICZ S., SANTELLA A.: Suggestive contours for conveying shape. "
        "_ACM Transactions on Graphics (SIGGRAPH) 22_, 3 (2003). "
        "[doi:10.1145/882262.882354](https://doi.org/10.1145/882262.882354). "
        "Models from [gfx.cs.princeton.edu/proj/sugcon/models](https://gfx.cs.princeton.edu/proj/sugcon/models/)",
    "https://github.com/nasa/NASA-3D-Resources":
        "NASA: NASA 3D Resources. [github.com/nasa/NASA-3D-Resources](https://github.com/nasa/NASA-3D-Resources)",
    # --- model collections without a dataset paper
    "https://github.com/odedstein/meshes":
        "STEIN O.: meshes. [github.com/odedstein/meshes](https://github.com/odedstein/meshes)",
    "https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/":
        "CRANE K.: Keenan's 3D model repository. "
        "[cs.cmu.edu/~kmcrane/Projects/ModelRepository](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/)",
    "https://github.com/alecjacobson/common-3d-test-models":
        "JACOBSON A.: Common 3D test models. "
        "[github.com/alecjacobson/common-3d-test-models](https://github.com/alecjacobson/common-3d-test-models)",
    "https://github.com/libigl/libigl-tutorial-data":
        "JACOBSON A., PANOZZO D.: libigl: prototyping geometry processing research in C++. In _SIGGRAPH Asia "
        "Courses_ (2017). [doi:10.1145/3134472.3134497](https://doi.org/10.1145/3134472.3134497). Data from "
        "[github.com/libigl/libigl-tutorial-data](https://github.com/libigl/libigl-tutorial-data)",
    "https://huggingface.co/datasets/alecjacobson/threedscans":
        "LARIC O.: Three D Scans. [threedscans.com](https://threedscans.com), via "
        "[huggingface.co/datasets/alecjacobson/threedscans](https://huggingface.co/datasets/alecjacobson/threedscans)",
    "https://github.com/CGAL/cgal/tree/main/Data/data/meshes":
        "THE CGAL PROJECT: _CGAL User and Reference Manual_. CGAL Editorial Board. Test meshes from "
        "[github.com/CGAL/cgal/tree/main/Data/data/meshes](https://github.com/CGAL/cgal/tree/main/Data/data/meshes)",
    "https://knotplot.com/":
        "SCHAREIN R., BOOTH K. S.: Interactive knot theory with KnotPlot. In _Multimedia Tools for Communicating "
        "Mathematics_, Mathematics and Visualization (2002). "
        "[doi:10.1007/978-3-642-56240-2_17](https://doi.org/10.1007/978-3-642-56240-2_17)",
    "https://sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0":
        "FACUNLA J.: Among Us crewmate. Sketchfab. "
        "[sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0](https://sketchfab.com/3d-models/among-us-crewmate-021671fa658d4d0dbb7bd5102b59c1d0)",
    "Bas Paardekooper":
        "PAARDEKOOPER B.: threecees. Personal communication.",
}
