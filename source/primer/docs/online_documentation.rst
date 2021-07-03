**********************************
Getting Started with Documentation
**********************************

Compiling Documentation Locally
################################

This example is a step-by-step guide on how to compile the tudat-developer documentation
locally on your system using ``sphinx``.

.. todo::

   The following procedure only works if the ``environment.yaml`` file has the following form. Currently,
   the same file has a different form.

   .. code-block:: yaml

      dependencies:
          - python-graphviz
          - rever
          - sphinxcontrib-bibtex
          - sphinx-panels
          - graphviz
          - pip
          - furo
          - GitPython
          - pip:
            - insipid-sphinx-theme

.. note::

    This procedure requires that Anaconda or Miniconda is installed. For
    information regarding the use of the conda ecosystem, please see ADD REFERENCE.

1. Clone the Github repository and enter it:

.. code:: bash

    git clone https://github.com/tudat-team/tudat-developer-docs & cd tudat-developer-docs

2. Create a conda environment from the ``environment.yaml`` file, then activate it
   (the ``-y`` flag instructs the ``conda-install`` command to install packages without asking for confirmation):

.. code:: bash

    conda create -y --name tudat-developer-docs -f environment.yaml & conda activate tudat-developer-docs

3. Install the following dependency:

.. code-block:: bash

    pip install insipid-sphinx-theme

4. Build the documentation using the ``sphinx-build`` command, specifying that html is to be built with the supplied source and output build directory.

.. code:: bash

    sphinx-build -b html source build

.. tip:: If you are using PyCharm, this step can be simplified by setting up a run configuration tailored for sphinx.
   This is explained in `Compiling Documentation with PyCharm`_.

5. View the local build of the documentation by opening the ``docs/build/index.html`` (or any other file)
   with your preferred browser.

.. tip:: **[PyCharm/CLion]** You can do this in by right clicking ``index.html`` in the Project tree and selecting ``Open with Browser``.


Compiling Documentation with PyCharm
####################################

If you are using PyCharm, the compilation of the documentation after each edit can be simplified by setting up a
run configuration tailored for sphinx. The procedure is described below.

1. From the main toolbar, click on ``Run > Edit Configurations``;
2. In the window that has just opened, click on the ``+`` button (upper-left) to add a new configuration;
3. From the drop-down menu, select ``Python docs > Sphinx task``;

.. figure:: _static/sphinx_config_pycharm_step1.png

4. Give a name to the new run configuration;
5. Make sure that the field ``Command`` is set on ``html``;
6. For the ``input`` and ``output`` fields, select the ``source`` and ``build`` folders respectively.

.. figure:: _static/sphinx_config_pycharm_step2.png

Make sure that the correct run configuration is selected. If so, pressing *Run* will be equivalent to executing the
following command from the command line:

.. code:: bash

    sphinx-build -b html docs/source docs/build

