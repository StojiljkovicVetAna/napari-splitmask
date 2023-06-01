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

Here we have wrapped the splitmask functions into a napari plugin, which enables to interactively setup points of interest, that are used to generate masks of different geometries. These specific masks are then used to compute intensity measurements on different channels of the time-lapse images. The intensity data can be viewed in napari or saved along with the masks.

----------------------------------
## Installation

Install napari-splitmask in a conda environment where you have pre-installed napari!

If you don't have an environment, follow this example using [conda] as environment manager. Or follow the instructions on the [napari] repository.

    conda create -y -n napari-env -c conda-forge python=3.9
    conda activate napari-env
    python -m pip install "napari[all]"

In this example, you create a new environment called 'napari-env' (you can pick the name you prefer), then you activate it and finally you install napari.

The environment should also contain the package 'splitmask', which can be installed as follow:

    pip install git+https://github.com/guiwitz/splitmask.git@master#egg=splitmask -U

Finally install napari-splitmask from Github using this command:

    pip install git+https://github.com/StojiljkovicVetAna/napari-splitmask.git


## Authors

Splitmask has been created by Guillaume Witz, Microscopy Imaging Center and Data Science Lab, University of Bern in collaboration with Jakobus van Unen, Pertz lab, Institute of Cell Biology, University of Bern.

Ana Stojiljkovic & Guillaume Witz, Data Science Lab (DSL), University of Bern have developed the napari-splitmask plugin.

## License

Distributed under the terms of the [BSD-3] license,
"napari-splitmask" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
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

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/

[splitmask]: https://github.com/guiwitz/splitmask
[conda]: https://docs.conda.io/en/latest/miniconda.html