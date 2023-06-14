# napari-splitmask

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

[![License BSD-3](https://img.shields.io/pypi/l/napari-splitmask.svg?color=green)](https://github.com/StojiljkovicVetAna/napari-splitmask/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-splitmask.svg?color=green)](https://pypi.org/project/napari-splitmask)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-splitmask.svg?color=green)](https://python.org)
[![tests](https://github.com/StojiljkovicVetAna/napari-splitmask/workflows/tests/badge.svg)](https://github.com/StojiljkovicVetAna/napari-splitmask/actions)
[![codecov](https://codecov.io/gh/StojiljkovicVetAna/napari-splitmask/branch/main/graph/badge.svg)](https://codecov.io/gh/StojiljkovicVetAna/napari-splitmask)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-splitmask)](https://napari-hub.org/plugins/napari-splitmask)

Plugin to use the python package 'splitmask' within napari.

The [splitmask] package provides interesting tools to analyze the dynamics of intensity in time-lapse microscopy images split into regions of specific geometries.

Here we have wrapped the splitmask functions into an easy-to-use napari plugin, which enables to interactively setup points of interest, which are used to generate masks of different geometries. In the current version you can select three different geometries:

<center><img src="/docs/images/napari-splitmask_shapes.png" width="490" height="190"/></center>

These specific masks are then used to compute intensity measurements on different channels of the time-lapse images. The intensity data can be viewed in napari or saved along with the masks.

----------------------------------
## Installation

Install napari-splitmask in a python environment where you have pre-installed the python viewer [napari]!

If you don't have a python environment yet, follow the example below, which uses [conda] as environment manager. Or explore the different options illustrated on the [napari installation] website.

### First create a python environment containing napari
After installing conda, execute these three commands in your terminal or command prompt.
```
conda create -y -n napari-env -c conda-forge python=3.9
conda activate napari-env
python -m pip install "napari[all]"
```
In this example, with the first command you create a new environment called 'napari-env' (here you can pick the name that you prefer), and you install python 3.9 in this new environment. Then you activate it and finally you install napari.

### Install napari-splitmask

In the newly created environment, now you can install napari-splitmask from Github using this command:

    pip install git+https://github.com/StojiljkovicVetAna/napari-splitmask.git

### Use napari-splitmask
If the installation was successful, you will be able to use napari-splitmask from your new environment. Make sure that the environment is active and type napari in the terminal, the napari GUI should appear. From the GUI you should navigate to Plugins/napari-splitmask to open the plugin. <br/>
Detailed instructions for the plugin are provided in the step-by-step guide.333333

## Authors

Splitmask has been created by Guillaume Witz, Microscopy Imaging Center and Data Science Lab, University of Bern in collaboration with Jakobus van Unen, Pertz lab, Institute of Cell Biology, University of Bern.

Ana Stojiljkovic & Guillaume Witz, Data Science Lab (DSL), University of Bern have developed the napari-splitmask plugin.

## License

Distributed under the terms of the [BSD-3] license,
"napari-splitmask" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://napari.org/stable/
[napari installation]: https://napari.org/stable/tutorials/fundamentals/installation.html

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/StojiljkovicVetAna/napari-splitmask/issues

[napari]: https://napari.org/stable/tutorials/fundamentals/installation.html
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

[splitmask]: https://github.com/guiwitz/splitmask
[conda]: https://docs.conda.io/en/latest/miniconda.html