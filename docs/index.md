<!-- #Acrossim -->

```markdown
This webpage is under construction. Last update: 11.08.2021
```

## Introduction

Acrossim is a modular component-based toolkit to process and integrate computational fluid dynamics (CFD) simulation data into game engines. The toolkit integrates data from the most commonly applied CFD solvers in engineering science; OpenFOAM, COMSOL and Ansys Fluent. It utilizes an extract-based data processing approach to integrate CFD data into cross-platform environments. The provided toolkit helps developers to effortlessly bring any simulation content into end-user devices. The toolkit is freely available on [**GitHub**](https://github.com/sersolmaz/Acrossim).

This webpage is the documentation for developers to implement the toolkit in their workflows. The toolkit mainly runs through an Anaconda environment with ParaView v5.8 and Blender v2.79 packages. The environment can be effortlessly compiled by running the “Acrossim.yml” file in Anaconda. Details about installation and implementation are given in the following sections.

## Methodology

Acrossim helps developers to rapidly integrate their CFD simulation results in cross-platform environments in a time cost effective way without concerning over powerful end-user hardware, hours of data preparation, and more significantly, performance and data quality. It is fundamentally structured towards lightweight, end-to-end, automated, and free-to-use utilities.

The toolkit provides a modular component-based approach to integrate CFD simulation data into game engines within an optimized and automated data processing approach. It utilizes an extract-based data processing approach to diminish the data size of CFD post-processing. This approach is incorporated in the toolkit from a recently published research [1, 2]. Notably, Acrossim integrates CFD data through extract-based data processing pipelines in which data is converted to suitable formats, processed based on validated workflows, specifically sorted to maintain easy access, summarized by excluding the unnecessary details, aggregated to bundle different data, assessed and reported, classified and stored. It is developed with Python in an Anaconda environment and compiled with ParaView and Blender libraries. Standard Python libraries are also utilized to embed file handling operations to control input and output (I/O) functionalities. 

Acrossim provides data processing pipelines considering three major data formats; tessellated (visual representations & volumetric data), image (graphs & charts) and text (numerical & text). Data processing pipelines are highly customizable mediums to edit and implement and user-specific demands. Data produced by Acrossim can be directly utilized in Unity and Unreal game engines, through which miscellaneous cross-platform applications such as mobile games and immersive VR experiences can be readily built.

Moreover, CFD simulations are generally performed with either remote or cloud-based solutions due to the heavy calculations. Post-processing of simulation data can also result in computationally intensive workflows that can be demanding for end-user devices. Acrossim serves as a means for developers to integrate lightweight CFD data into games engines. Above all, a fully automated routine of Acrossim may facilitate a content delivery network by remotely linking CFD solver with end-user applications. This connection can open gates for two-way coupled interactive systems with content delivery networks (CDN), thereby remotely streaming any CFD content to end-user devices and digital twins.

## Installation

An Anaconda environment should be configurated with **acrossim.yml** file to run Acrossim with required packages. Use the terminal or an Anaconda Prompt in Anaconda Navigator for the following steps:

1. Creat an environment from the **acrossim.yml** file. Make sure that the cmd.exe terminal and **acrossim.yml** are in the same working directory.
```markdown
conda env create -f acrossim.yml
```
2. Activate environment.
```markdown
conda activate acrossim
```
3. Verify the installed environment.
```markdown
conda env list
```

After the installation completed, an Acrossim application should be listed under environments in Anaconda. Should you encounter any issues, do check [Conda user guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment).

## Modules and processors

The toolkit comprises three unique modules based on CFD solvers OpenFOAM, COMSOL, and Fluent. Each module is of three processors to integrate CFD data in various formats. These processors are TESSELLATE, IMAGE, and TEXT. OpenFOAM module encompasses baseline processors of Acrossim. COMSOL and Fluent modules basically inherit these processors with minor inclusions by only means of data preparation and recuperation. 

Acrossim is a highly customizable toolkit that can serve any user-defined demands. Either ParaView state file or relevant processor can be modified to obtain specific processing workflows. For instance, in order to change color legend without creating a new state file, the user can go into the existing state file and manipulate relevant objects by changing color codes. This requires an understanding of the ParaView Python API. The trace option in ParaView dynamically illustrates each action taken by the user with GUI in ParaView. Hence users can intuitively decode ParaView API by keeping track of traces. Similarly, available documentation of ParaView API can aid in finding the target object to process user-defined needs. This may enable remote data processing through connected and coupled systems.

**1. OpenFOAM**

This module includes three processors as a baseline to other modules.  Tessellated, image and text data are directly processed from native CFD data produced by OpenFOAM. It merely requires a reference ParaView state file to perform the data processing.

**2. COMSOL**

Data from COMSOL is exported to VTU format in order to import CFD data with ParaView and implement it in Acrossim. COMSOL module utilizes the same processors as OpenFOAM within one exception in the tessellate one. Having been previously mentioned, VTU encodes only simulation data rather than geometric features. Hence, the format does exclude all geometric features while extracting data from COMSOL, for instance, extrusion of streamline tubes from splines and curves. To cope with this complication, tessellate processor in COMSOL module is extended using a bevel modifier in Blender to reconstruct 3D data from splines and curves. This extension loops with an “if conditioner” in the tessellate processor. It merely applies to streamlines, glyphs, and similar visual data.

**3. FLUENT**

Fluent saves CFD data with a single CAS file where simulation settings are stored, and also DAT files for each written timestep. ParaView cannot inherit the same system to manage transient Fluent data. Each DAT file should be accompanied by a CAS file to be properly imported in ParaView. In order to automatically handle this, we wrote “fluenttoparaview.py” script through which CAS files are created and subsequently named for each DAT file. It automatically detects and converts Fluent native CFD data into formats that can be read by ParaView. No input timesteps are necessary for processors. All native data collected under the toolkit directory are directly processed.

## Tutorials

This section is under construction.

## Outsourcing

**Available CFD data** 

CFD simulations require a competent analyst to pre-process, calculate and post-process simulation data in a timely cost-effective way. Also, developing verified and validated CFD workflows are vital to obtaining accurate results. Various online resources are freely available for developers to ease the workflow creating verified and validated simulations workflows. Resources that can be integrated into Acrossim are listed as follows:

OpenFOAM:
* https://wiki.openfoam.com/Tutorials
* https://wiki.openfoam.com/Collection_by_authors
* https://github.com/OpenFOAM/OpenFOAM-6
* https://www.openfoam.com/documentation/tutorial-guide
* https://www.cfd.at/tutorials

COMSOL:
* https://www.comsol.com/models
* https://www.comsol.com/learning-center

Databases for CFD benchmarks:
* Ercoftac: http://cfd.mace.manchester.ac.uk/ercoftac/doku.php?id=flow_types
* Ercoftac: https://www.ercoftac.org/publications/ercoftac_best_practice_guidelines/
* Hamburg: https://mi-pub.cen.uni-hamburg.de/index.php?id=628
* NASA V&V: https://www.grc.nasa.gov/www/wind/valid/tutorial/overview.html
* NASA archive: https://www.grc.nasa.gov/www/wind/valid/archive.html
* Gallery of fluid motion: https://gfm.aps.org/

**Unity game engine**

Several free and paid packages can be acquired from Unity asset store: https://assetstore.unity.com/

## Troubleshooting

This section is being kept updated to give guidance for frequently encountered problems.

**ParaView state files**

ParaView state files read CFD data from user-defined directories. If the directory of CFD data is changed, the line "Reader" in the state files should be manually updated as for the following examples. Any change in the directory should be processed in the state file.

An example for OpenFOAM:
```markdown
OpenFOAMReader(FileName='D:/simulations/acrossim/module_OpenFOAM/pitzDaily_LES/pitzDaily_LES.foam') 
```
An example for COMSOL:
```markdown
PVDReader(FileName='D:/simulations/acrossim/module_COMSOL/velocity_isothermal/merged.pvd')
```

Besides, developers can create a new state file reading the CFD data from the new directory.

**OpenFOAM with ParaView on Microsoft Windows**

In order to post-process OpenFOAM data with ParaView on MS Windows, an empty “.foam” file should be created and stored under the simulation file to import simulation data, for example, “pitzDaily_LES.foam”.

## Articles and contributions

* [1] Solmaz, S. and Van Gerven, T., 2021. Automated integration of extract-based CFD results with AR/VR in engineering education for practitioners. Multimedia Tools and Applications, pp.1-23, DOI: https://doi.org/10.1007/s11042-021-10621-9.
* [2] Solmaz, S. and Van Gerven, T., 2021. In preparation.
* [3] ...

## Contact

* Developer: Serkan Solmaz (serkan.solmaz@kuleuven.be)
* [Personal page](https://www.kuleuven.be/wieiswie/en/person/00127798)
* Address: Department of Chemical Engineering, KU Leuven, Celestijnenlaan 200F, B-3001 Leuven, Belgium

### Acknowledgements

This project has received funding from the European Union’s EU Framework Programme for Research and Innovation Horizon 2020 under Grant Agreement 812716. This publication reflects only the author’s view exempting the community from any liability. Project website: [https://charming-etn.eu/](https://charming-etn.eu/)

![alt text](https://charming-etn.eu/wp-content/uploads/2018/12/flag_yellow_low.jpg)
![alt text](https://user-images.githubusercontent.com/34717545/126303026-b204a42a-ca52-4cec-ab44-b78e1c32909a.png)

© 2021
