# Acrossim

## Introduction

Acrossim is a modular component-based toolkit to process and integrate computational fluid dynamics (CFD) simulation data into game engines. The toolkit integrates data from most commonly applied CFD solvers in engineering science; OpenFOAM, COMSOL and Ansys Fluent. The provided toolkit helps developers to effortlessly bring any simulation content to user devices. You can use the [editor on GitHub](https://github.com/sersolmaz/Acrossim/edit/main/docs/index.md) to maintain and preview the content of the toolkit.

## Methodology

The toolkit provides a modular component-based approach to integrate CFD simulation data in game engines within an optimized and automated data processing approach. 

In this study, we develop a toolkit, called Acrossim, to realize the data processing pipeline recently proposed in the literature [1].

Recently, a data processing methodology was proposed as a solution to the above-mentioned problems targeting lightweight, interoperable, end-to-end and free-to-use utilities [15]. The study highlighted an inclusive guidance on the integration of CFD data with game engines through a modular component-oriented data processing pipeline. A thorough investigation was carried out to examine optimized and automated data processing options between CFD solvers and game engines. A qualitative assessment was performed to scrutinize data format, size, processing time, quality, automation and management. The study introduced an extract-based approach to adapt big CFD data into cross-platform user applications through manageable data bundles.

The toolkit processes CFD data from multiple CFD software to integrate simulation results with various formats into game engines. A modular component-based software structure is acquired blending already available resources. It is developed with Python in an Anaconda environment and compiled with ParaView and Blender libraries. Standard Python libraries are also utilized to embed file handling operations to control input and output (I/O) functionalities. 

The toolkit comprises the following components: input, modules, processors, output and storage. A detailed description of its schematic architecture is illustrated in Figure 1. It is noteworthy that CFD solvers give input files in various formats, thereby requiring solver-specific data handling features. To tackle these hindrances, the toolkit proposes distinguished modules for each CFD software within supplementary additions in the processors. Each module can serve as a standalone provider for a specific CFD solver. 

Besides, each module has three main processors based on data formats; tessellate, image and text. Processors utilize state files to automatically integrate native CFD data into target output files.

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


1. **OpenFOAM**
THIS MODULE

2. **COMSOL**
THIS MODULE

3. **FLUENT**
THIS MODULE

## Tutorials

1. **OpenFOAM**
THIS MODULE

2. **COMSOL**
THIS MODULE

3. **FLUENT**
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

