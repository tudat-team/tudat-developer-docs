
Package Management
==================


.. admonition:: :fa:`graduation-cap` Learning Objectives

    .. include:: objectives/package_manager.rst

Conda
-----

Conda is in open source package manager that runs on Windows, macOS and Linux.
It is popular in the Python community, as it was originally intended to handle
Python programs primarily but due to its ability to package and distribute
software for any language, its use has grown significantly.

.. admonition:: Nomenclature

      **Environment**
       A directory that contains a specific collection of
       **conda** packages that you have installed.

      **Anaconda**
       A distribution of the Python and R programming languages
       for specific computing (data science, machine learning applications,
       large-scale data processing, predictive analytics, etc.)
       :cite:p:`anaconda`

      **Bootstrap**
       A bootstrap is the program that initializes the operating
       system (OS) during startup (Only relevant for next nomenclature item).

      **Miniconda**
       Miniconda is a free minimal installer for conda. It is a
       small, bootstrap version of Anaconda that includes only conda, Python,
       the packages they depend on, and a small number of other useful packages,
       including `pip`_, `zlib`_ and a few others. :cite:p:`miniconda`

      **Recipe**
       A `Conda-build recipe`_ is a flat directory that contains
       a specific collection of files which defines a package's dependencies,
       description (branding), build procedure (when applicable) and test
       procedure.

      **Pinning**
       Pinning dependencies refers to explicitly defining the
       versions of software that your application depends on. The high-level
       is to "freeze" dependencies so that subsequent builds/deployments are
       repeatable.

.. _`pip`: https://pypi.org/project/pip/
.. _`zlib`: https://zlib.net/
.. _`Conda-build recipe`: https://docs.conda.io/projects/conda-build/en/latest/concepts/recipe.html#conda-build-recipes

Conda-build
-----------

Conda-build is a package that contains commands and tools to use conda to
build your own conda packages. It also provides helpful tools to constrain or
pin versions in recipes. At the heart of Conda-build is the concept of a
Conda-build recipe:

.. code-block::

    recipe
    ├── bld.bat
    ├── build.sh
    ├── meta.yaml
    └── run_test.py

Each file in the Conda-build recipe has a specific responsibility in creating
a conda package. The responsibilities are as follow:

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| File                     | Description                                                                                                                                           |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``meta.yaml``            | A file that contains all the metadata in the recipe. Only ``package/name`` and ``package/version`` are required.                                      |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``build.sh``             | The script that installs the files for the package on macOS and Linux. It is executed using the ``bash`` command.                                     |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``bld.bat``              | The build script that installs the files for the package on Windows. It is executed using ``cmd``.                                                    |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``run_test.[py,sh,bat]`` | An **optional** Python test file, a test script that runs automatically if it is part of the recipe. Optional patches that are applied to the source. |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
