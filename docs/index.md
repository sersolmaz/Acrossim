<!-- #Acrossim -->

```markdown
Lastest update: 28.07.2023
```

## Introduction

Acrossim is a modular component-based toolkit to process and integrate computational fluid dynamics (CFD) simulation data into game engines. The toolkit integrates data from the most commonly applied CFD solvers in engineering science; OpenFOAM, COMSOL and Ansys Fluent. It utilizes an extract-based data processing approach to integrate CFD data into cross-platform environments. The provided toolkit helps developers effortlessly bring any simulation content into end-user devices. The toolkit is freely available on [**GitHub**](https://github.com/sersolmaz/Acrossim).

This webpage is the documentation for developers to implement the toolkit in their workflows. The toolkit mainly runs through an Anaconda environment with ParaView v5.8 and Blender v2.79 packages. The environment can be effortlessly compiled by running the “Acrossim.yml” file in Anaconda. Details about installation and implementation are given in the following sections.

## Methodology

Acrossim offers developers a rapid and cost-effective way to integrate CFD simulation results into cross-platform environments, eliminating concerns about powerful end-user hardware, data preparation time, and ensuring optimal performance and data quality. The toolkit's fundamental structure emphasizes lightweight, end-to-end automation, and free-to-use utilities.

The modular component-based approach in Acrossim optimizes and automates data processing for integrating CFD simulation data into game engines. It adopts an extract-based data processing technique, which reduces the data size of CFD post-processing. This approach is drawn from recently published research [1]. Acrossim's integration of CFD data utilizes extract-based pipelines, transforming data into suitable formats, processing them through validated workflows, sorting them for easy access, summarizing to exclude unnecessary details, bundling different data, and storing, assessing, reporting, and classifying the data. Python, Anaconda, ParaView, and Blender libraries form the foundation of its development, while standard Python libraries control input and output (I/O) operations.

Acrossim caters to three major data formats: tessellated (visual representations & volumetric data), image (graphs & charts), and text (numerical & text). The data processing pipelines are highly customizable, allowing easy editing and implementation to meet specific user demands. The data produced by Acrossim can be directly utilized in Unity and Unreal game engines, facilitating the creation of various cross-platform applications, including mobile games and immersive VR experiences.

CFD simulations typically require remote or cloud-based solutions due to their computational complexity. Post-processing simulation data can also be computationally intensive, posing challenges for end-user devices. Acrossim serves as a solution by integrating lightweight CFD data into game engines, making the process more manageable. Moreover, a fully automated routine in Acrossim could enable a content delivery network, linking the CFD solver with end-user applications remotely. This connection opens possibilities for two-way coupled interactive systems with content delivery networks (CDN), allowing remote streaming of CFD content to end-user devices and digital twins.

## Installation

An Anaconda environment should be configurated with **acrossim.yml** file to run Acrossim with required packages. Use the terminal or an Anaconda Prompt in Anaconda Navigator for the following steps:

1. Create an environment from the **acrossim.yml** file. Make sure that the cmd.exe terminal and **acrossim.yml** are in the same working directory.
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

Once the installation is completed, an Acrossim application should be listed under environments in Anaconda. Should you encounter any issues, do check [Conda user guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment).

## Modules and processors

The toolkit comprises three unique modules based on CFD solvers OpenFOAM, COMSOL, and Fluent. Each module is of three processors to integrate CFD data in various formats. These processors are TESSELLATE, IMAGE, and TEXT. OpenFOAM module encompasses baseline processors of Acrossim. COMSOL and Fluent modules basically inherit these processors with minor inclusions by only means of data preparation and recuperation. 

Acrossim is a highly customizable toolkit that can serve any user-defined demands. Either a ParaView state file or relevant processor can be modified to obtain specific processing workflows. For instance, in order to change the color legend without creating a new state file, the user can go into the existing state file and manipulate relevant objects by changing color codes. This requires an understanding of the ParaView Python API. The trace option in ParaView dynamically illustrates each action taken by the user with GUI in ParaView. Hence users can intuitively decode ParaView API by keeping track of traces. Similarly, available documentation of ParaView API can aid in finding the target object to process user-defined needs. This may enable remote data processing through connected and coupled systems.

**1. OpenFOAM**

This module includes three processors as a baseline for other modules.  Tessellated, image and text data are directly processed from native CFD data produced by OpenFOAM. It merely requires a reference ParaView state file to perform the data processing.

**2. COMSOL**

Data from COMSOL is exported to VTU format in order to import CFD data with ParaView and implement it in Acrossim. COMSOL module utilizes the same processors as OpenFOAM within one exception in the tessellate one. Having been previously mentioned, VTU encodes only simulation data rather than geometric features. Hence, the format does exclude all geometric features while extracting data from COMSOL, for instance, extrusion of streamline tubes from splines and curves. To cope with this complication, tessellate processor in COMSOL module is extended using a bevel modifier in Blender to reconstruct 3D data from splines and curves. This extension loops with an “if conditioner” in the tessellate processor. It merely applies to streamlines, glyphs, and similar visual data.

**3. FLUENT**

Fluent saves CFD data with a single CAS file where simulation settings are stored, and also DAT files for each written timestep. ParaView cannot inherit the same system to manage transient Fluent data. Each DAT file should be accompanied by a CAS file to be properly imported into ParaView. In order to automatically handle this, we wrote “fluenttoparaview.py” script through which CAS files are created and subsequently named for each DAT file. It automatically detects and converts Fluent native CFD data into formats that can be read by ParaView. No input timesteps are necessary for processors. All native data collected under the toolkit directory are directly processed.

## Tutorials

A guiding tutorial is available at [YouTube - Acrossim tutorial]([https://github.com/sersolmaz/Acrossim](https://www.youtube.com/watch?v=WA_9-2JYKdM)). It demonstrates how to set up an Anaconda environment with relevant packages, as well as to develop a user app with processed CFD data in Unity. 

A technical report - explaining the core functions of the toolkit - is available at [Technical Report - Accrossim](https://github.com/sersolmaz/Acrossim/blob/main/Technical_report_Acrossim.docx.pdf). The report can help you understand how to further build Acrossim on top of specific use cases while addressing other features and functionalities not mentioned on this page.

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

** --->ParaView state files**

ParaView state files read CFD data from user-defined directories. If the directory of CFD data is changed, the line "Reader" in the state files should be manually updated as for the following examples. Any change in the directory should be processed in the state file.

An example of OpenFOAM:
```markdown
OpenFOAMReader(FileName='D:/simulations/acrossim/module_OpenFOAM/pitzDaily_LES/pitzDaily_LES.foam') 
```
An example of COMSOL:
```markdown
PVDReader(FileName='D:/simulations/acrossim/module_COMSOL/velocity_isothermal/merged.pvd')
```

Besides, developers can create a new state file reading the CFD data from the new directory.

** --->OpenFOAM with ParaView on Microsoft Windows**

In order to post-process OpenFOAM data with ParaView on MS Windows, an empty “.foam” file should be created and stored under the simulation file to import simulation data, for example, “pitzDaily_LES.foam”.

** --->Other versions of ParaView and Blender in Anaconda**

If other versions of ParaView and Blender are utilized in the Anaconda environment, some parts of modules should be updated based on changes in ParaView and Blender APIs. Please follow the given error and go line-by-line to identify what to change and rectify such as class names, objects, etc.

** --->Processing multiple cutplanes in ParaView**

Even though only one cutplane is processed in the tutorial, the toolkit is capable of processing multiple cutplanes simultaneously from a native CFD file in ParaView. No changes in the code are required.

** --->Adding other data formats such as USD**

You can include other data formats to import and export data for specific use cases such as USD which is becoming a popular data format in computer graphics. To do this, first check data import and export pipelines available in ParaView and Blender. Then you should replace the data format with the one available in the TESSSELATE processors, for example changing FBX to USD: "exportBlender = 'fbx'" >> "exportBlender = 'usd'".

** --->Using Blender as an intermediate processor**

COMSOL module already uses Blender to construct geometries, for instance, solidifying or changing the thickness of streamlines. The same operation with some minor additions can serve an intermediate data processor to process geometry-related features for some reason - such as the construction of iso-surfaces.

## Articles and contributions

* [1] Solmaz, S. and Van Gerven, T., 2021. Automated integration of extract-based CFD results with AR/VR in engineering education for practitioners. Multimedia Tools and Applications, pp.1-23, DOI: https://doi.org/10.1007/s11042-021-10621-9.
* [2] Solmaz, S. and Van Gerven, T., 2023. Acrossim: A toolkit for cross-platform integration of CFD simulation data in computer graphics, SoftwareX, in revision (as of 28.07.2023)

## Contact

* Developer: Serkan Solmaz (serknslmz@gmail.com)
* [Personal page](https://www.kuleuven.be/wieiswie/en/person/00127798)
* [LinkedIn](https://www.linkedin.com/in/serkan-solmaz/)
* Address: Department of Chemical Engineering, KU Leuven, Celestijnenlaan 200F, B-3001 Leuven, Belgium

### Acknowledgements

This project has received funding from the European Union’s EU Framework Programme for Research and Innovation Horizon 2020 under Grant Agreement 812716. This publication reflects only the author’s view exempting the community from any liability. Project website: [https://charming-etn.eu/](https://charming-etn.eu/)

![alt text](https://charming-etn.eu/wp-content/uploads/2018/12/flag_yellow_low.jpg)
![alt text](https://user-images.githubusercontent.com/34717545/126303026-b204a42a-ca52-4cec-ab44-b78e1c32909a.png)

© 2023
