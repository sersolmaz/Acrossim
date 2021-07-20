#Acrossim
## Introduction

Acrossim is a modular component-based toolkit to process and integrate computational fluid dynamics (CFD) simulation data into game engines. The toolkit integrates data from most commonly applied CFD solvers in engineering science; OpenFOAM, COMSOL and Ansys Fluent. The provided toolkit helps developers to effortlessly bring any simulation content to user devices. You can use the [editor on GitHub](https://github.com/sersolmaz/Acrossim/edit/main/docs/index.md) to maintain and preview the content of the toolkit.

This section details the implementation of Acrossim. An Anaconda environment with ParaView v5.8 and Blender v2.79 packages should be created to run processors. The environment can be effortlessly compiled by running “Acrossim.yml” file in Anaconda. 

## Methodology

The toolkit provides a modular component-based approach to integrate CFD simulation data in game engines within an optimized and automated data processing approach. 

Acrossim proposes optimal and automated data processing pipelines considering three major data formats; tessellate, image and text. Modules highly customizable mediums to edit and implement and user specific demands.
Data produced by Acrossim can be directly utilized in Unity and Unreal game engines, through which miscellaneous cross-platform application such as mobile games and immersive VR experiences can be readily built.
Acrossim integrated CFD data through data processing pipelines in which data is conversed to suitable formats, processed based on validated workflows, specifically sorted to maintain easy access, summarized by excluding the unnecessary details, aggregated to bundle different data, assessed and reported, classified and stored.

In this study, we develop a toolkit, called Acrossim, to realize the data processing pipeline recently proposed in the literature [1].

The processed CFD data can be usually categorized as follows: visual representations  as volumetric data, graphs & charts, and analytical & text data. An extract-based data processing approach can diminish data size of CFD post-processing. Integration of extract-based CFD data with cross-platform development tools has been studied by scholars based on two fundamental approaches.

On one hand, native CFD data is processed via post-processing software and subsequently exported to text files. Following, the intended CFD data is reproduced in cross-platform environments using dedicated post-processing algorithms implemented by developers [5]–[7]. This approach came forward with technical drawbacks in the design and operation of user applications. First of all, CFD post-processing algorithms should be implemented in the game engines to reproduce CFD data from text files. 

On the other hand, native CFD data is processed via post-processing software and exported to suitable file formats such as 3D, image and text. The exported data are then exchanged to the formats that are readable by game engines. This methodology points out a lightweight approach to employ any end user device. 

Recently, a data processing methodology was proposed as a solution to the above-mentioned problems targeting lightweight, interoperable, end-to-end and free-to-use utilities [15]. The study highlighted an inclusive guidance on the integration of CFD data with game engines through a modular component-oriented data processing pipeline. A thorough investigation was carried out to examine optimized and automated data processing options between CFD solvers and game engines. A qualitative assessment was performed to scrutinize data format, size, processing time, quality, automation and management. The study introduced an extract-based approach to adapt big CFD data into cross-platform user applications through manageable data bundles.

The toolkit processes CFD data from multiple CFD software to integrate simulation results with various formats into game engines. A modular component-based software structure is acquired blending already available resources. It is developed with Python in an Anaconda environment and compiled with ParaView and Blender libraries. Standard Python libraries are also utilized to embed file handling operations to control input and output (I/O) functionalities. 

The toolkit comprises the following components: input, modules, processors, output and storage. A detailed description of its schematic architecture is illustrated in Figure 1. It is noteworthy that CFD solvers give input files in various formats, thereby requiring solver-specific data handling features. To tackle these hindrances, the toolkit proposes distinguished modules for each CFD software within supplementary additions in the processors. Each module can serve as a standalone provider for a specific CFD solver. Native CFD datasets and ParaView states are two input files to appropriately run the toolkit. The prior can be in any format as long as it is imported in ParaView. The latter is only one time and manually created to provide a baseline of CFD post-processing data. Besides, each module has three main processors based on data formats; tessellate, image and text. Processors utilize state files to automatically integrate native CFD data into target output files.

It is noteworthy that CFD solvers give input files in various formats, thereby requiring solver-specific data handling features. To tackle these hindrances, the toolkit proposes distinguished modules for each CFD software within supplementary additions in the data processing pipeline. These are presented in the section Software Functionalities.

Besides, each module has three main processors based on data formats; tessellate, image and text. Processors utilize state files to automatically integrate native CFD data into target output files.

Data produced by Acrossim can be directly utilized in Unity and Unreal game engines, through which miscellaneous cross-platform application such as mobile games and AR/VR experiences can be readily built. 

CFD simulations are generally performed with either remote or cloud-based solutions due to the heavy calculations. Post-processing of simulation data can also result in computationally intensive workflows that can be demanding for end user devices. Acrossim serves as a mean for developers to integrate lightweight CFD data into games engines. Above all, a fully automated routine of Acrossim may facilitate a content delivery network by remotely linking CFD solver with end user applications. This connection can open gates for two-way coupled interactive systems with content delivery networks (CDN), thereby remotely streaming any CFD content to end user devices and digital twins.

In this study, we develop a set of codes, called A toolkit for cross-platform integration of CFD simulation data in computer graphics (Acrossim), to realize the data processing pipeline recently proposed in the literature [14]. This will help developers to rapidly integrate their CFD simulation results in cross-platform environments in a time cost effective way without concerning over powerful end user hardware, hours of data preparation, and more significantly performance and data quality.

## Installation

An Anaconda environment should be configurated to run Acrossim with **acrossim.yml** file. Use the terminal or an Anaconda Prompt in Anaconda Navigator for the following steps:

1. Creat an environment from the **acrossim.yml** file. Make sure that the terminal and **acrossim.yml** are in the same working directory.
```markdown
conda env create -f acrossim.yml
```
2. Activate environment.
```markdown
conda activate acrossim
```
3. Verify the installed environment
```markdown
conda env list
```

Should you encounter any issues, do check [Conda user guide](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment).

## Modules and processors
The toolkit comprises three unique modules based on CFD solvers OpenFOAM, COMSOL and Fluent. Each module is of three processors to integrate 3D data in various formats. These processors are TESSELLATE, IMAGE and TEXT. OpenFOAM module encompasses baseline processors of Acrossim. COMSOL and Fluent modules basically inherit these processors with minor inclusions by only means of data preparation and recuperation. 

Acrossim is a highly customizable toolkit that can serve for any user-defined demands. Either ParaView state file or relevant processor can be modified to obtain specific processing workflows. For instance, in order to change color legend without creating a new state file, the user can go in the existing state file and manipulate relevant object by changing color codes. This requires an understanding of the ParaView Python API. Trace option in ParaView dynamically illustrates each action taken by user with GUI in ParaView. Hence users can intuitively decode ParaView API by keeping track of traces. Similarly, available documentation of ParaView API can aid finding the target object to process user-defined needs. This may enable remote data processing through connected and coupled system. 

**1. OpenFOAM**

This module includes three processors as a baseline to other modules.  Tessellate, image and text data are directly processed from native CFD data produced by OpenFOAM. It merely requires a reference ParaView state file to perform the data processing.

**2. COMSOL**

Data from COMSOL is exported to VTU format in order to import CFD data with ParaView and implement it in Acrossim. COMSOL module utilizes the same processors as OpenFOAM within one exception in the tessellate one. Having been previously mentioned, VTU encodes only simulation data rather than geometric features. Hence, the format does exclude all geometric features while extracting data from COMSOL, for instance, extrusion of streamline tubes from splines and curves. To cope with this complication, tessellate processor in COMSOL module is extended using a bevel modifier in Blender to reconstruct 3D data from splines and curves. This extension loops with an “if conditioner” in the tessellate processor. It merely applies to streamlines, glyphs, and similar visual data.

**3. FLUENT**

Fluent saves CFD data with a single CAS file where simulation settings are stored, and also DAT files for each written timestep. ParaView cannot inherit the same system to manage transient Fluent data. Each DAT file should be accompanied by a CAS file to be properly imported in ParaView. In order to automatically handle this, we wrote “fluenttoparaview.py” script through which CAS files are created and subsequently named for each DAT file. It automatically detects and converts Fluent native CFD data into formats that can be read by ParaView. No input timesteps are necessity in processors. All native data collected under the toolkit directory are directly processed.

## Tutorials

**1. OpenFOAM**

THIS MODULE

**2. COMSOL**

THIS MODULE

**3. FLUENT**

THIS MODULE

## Articles and contributions

* [1] Solmaz, S. and Van Gerven, T., 2021. Automated integration of extract-based CFD results with AR/VR in engineering education for practitioners. Multimedia Tools and Applications, pp.1-23, DOI: https://doi.org/10.1007/s11042-021-10621-9.
* [2] ...
* [3] ...

## Contact

* Developer: Serkan Solmaz (serkan.solmaz@kuleuven.be)
* [Personal page](https://www.kuleuven.be/wieiswie/en/person/00127798)
* Address: Department of Chemical Engineering, KU Leuven, Celestijnenlaan 200F, B-3001 Leuven, Belgium

### Acknowledgements

_This project has received funding from the European Union’s EU Framework Programme for Research and Innovation Horizon 2020 under Grant Agreement 812716. This publication reflects only the author’s view exempting the community from any liability. Project website: https://charming-etn.eu/._

