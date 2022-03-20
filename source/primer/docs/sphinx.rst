====================
Sphinx Documentation
====================

.. code-block::

    sudo apt-get install  texmaker gummi texlive texlive-full texlive-latex-recommended latexdraw intltool-debian lacheck libgtksourceview2.0-0 libgtksourceview2.0-common lmodern luatex po-debconf tex-common texlive-binaries texlive-extra-utils texlive-latex-base texlive-latex-base-doc texlive-luatex texlive-xetex texlive-lang-cyrillic texlive-fonts-extra texlive-science texlive-latex-extra texlive-pstricks


.. todo::

    - Link checking is facilitated by sphinx using ``make linkcheck`` (on windows)
    - Add section on FontAwesome inline icons from ``sphinx-panels``
    - https://fontawesome.com/
    - Add tutorial/ section on maintaining a bibliography in Sphinx.


**********************************
Compile documentation with Sphinx
**********************************


This example is a step-by-step guide on how to compile the tudat documentation
locally on your system using ``sphinx``. This procedure works to compile documentation for both the `tudat-space
<https://docs.tudat.space/en/latest/>`_ and the documentation you are currently reading.

.. note::

    This procedure requires that Anaconda or Miniconda is installed. For
    information regarding the use of the conda ecosystem, please see :ref:`Getting Started with Conda`.

1. Create an environment that will be satisfy all dependencies required for building documentation, then activate it.
   This can be done by downloading this ``environment.yaml`` (:download:`yaml <_static/environment.yaml>`), which
   will install the ``tudat-docs`` conda environment.

.. code:: bash

    conda env create -f environment.yaml & conda activate tudat-docs

2. Enter the root directory of a repository containing a ``docs`` directory, which contains a ``source`` subdirectory.
   The following command is specific to cloning and entering the ``tudat-space`` repository.

.. code:: bash

    git clone https://github.com/tudat-team/tudat-space.git & cd tudat-space

3. Build the documentation using the ``sphinx-build`` command, specifying that html is to be built with the supplied
   source and output build directory.

.. code:: bash

    sphinx-build -b html docs/source docs/build

4. View the local build of the documentation by opening the ``docs/build/index.html`` with your preferred browser.

.. tip:: **[PyCharm/CLion]** You can do this in by right clicking ``index.html`` in the Project tree and selecting ``Open with Browser``.

Compiling Documentation in PyCharm
************************************

If you are using PyCharm, the compilation of the documentation after each edit can be simplified by setting up a
run configuration tailored for sphinx. The procedure is described below.

1. From the main toolbar, click on ``Run > Edit Configurations``;
2. In the window that has just opened, click on the ``+`` button (upper-left) to add a new configuration;
3. From the drop-down menu, select ``Python docs > Sphinx task``;

.. figure:: _static/sphinx_config_pycharm_step1.png
    :width: 200px
    :align: center

4. Give a name to the new run configuration;
5. Make sure that the field ``Command`` is set on ``html``;
6. For the ``input`` and ``output`` fields, select the ``source`` and ``build`` folders respectively.

.. figure:: _static/sphinx_config_pycharm_step2.png

Make sure that the correct run configuration is selected. If so, pressing *Run* will be equivalent to executing the
following command from the command line:

.. code:: bash

    sphinx-build -b html docs/source docs/build

**********************************
Release new versions of the docs
**********************************

Every time you make a modification to the documentation, you are required to:

1. update the ``CHANGELOG.md``
2. release a new version of the documentation

While updating the changelog is quite straightforward, the process needed to release a new version deserves some
explanation.

Versioning with readthedocs
**********************************

Releasing a new version of the documentation is simple. To do this, we rely on `bumpversion <https://github
.com/c4urself/bump2version>`_ which in turns uses semantic versioning (or `SemVer <https://semver.org>`_). Semantic
versioning relies the following structure for stable releases: ``MAJOR.MINOR.PATCH`` (e.g., 1.3.1). For unstable
releases, the same
syntax is used with the addition of an additional tag, such as ``MAJOR.MINOR.PATCH.devBUILD`` (e.g., 1.3.1.dev2).

.. seealso::
    Read more on how readthedocs deals with `versions <https://docs.readthedocs.io/en/stable/versions.html#>`_.

Once you have committed your changes, you can release a new version by typing in the terminal one of the following
commands:

- ``bumpversion patch``: this increases the patch number (the same can be done with ``bumpversion major`` or ``bumpversion minor``)
    - 1.1.1 -> 1.1.2.dev0
    - 1.1.2.dev0 -> 1.1.3.dev0
    - 1.1.2.dev1 -> 1.1.3.dev0

- ``bumpversion dev``: this increases the build number
    - 1.1.2.dev0` -> 1.1.2.dev1
    - 1.1.2` -> ❌ This will break. Patch must be bumped to start ``dev`` suffix.

- ``bumpversion release``: this releases a stable version
    - 1.1.2.dev0` -> 1.1.2
    - 1.2.0.dev0` -> 1.2.0

``bumpversion`` creates a dedicated commit every time it is executed and tags such commit with the version number.

Once the commits are pushed to the ``main`` branch on ``origin``, the documentation is built by `readthedocs
<readthedocs.org>`_.
Readthedocs uses the tags to build different versions of the documentation, with two additional versions:

- ``latest`` (corresponding to the latest commit on ``main``)
- ``stable`` (corresponding to the most recent version released)

Depending whether the release is stable or unstable, different things happen:

- if the release is *stable*, the resulting documentation is published on the website and a new version will be visible
  in the readthedocs menu)
- if the release is *unstable*, the resulting documentation will not be built nor published on the website

.. _readthedocs_menu:

.. note::

    The readthedocs menu is located in the bottom left corner of the documentation page (see below).

    .. figure:: _static/readthedocs_menu.png
        :width: 200px
        :align: center

Unpublished (or "hidden") versions can still be activated (by authorized users) to be viewed online (and shared with
others through a link) by clicking on the readthedocs menu and selecting "Builds", then "Versions" and activate build.

.. figure:: _static/builds.png
    :width: 200px
    :align: center

Clicking on the right build allows to see it in the browser and copy
the related link to share it with collaborators. This is particularly useful to share drafts of the output
documentation without modifying stable versions.

.. warning::
    If the changes are pushed to other branches, no documentation is built.

****************
Troubleshooting
****************

In this section, we collect the most recurring bugs that can happen while using sphinx, hoping that it will save
precious time to future Tudat contributors.

No changes shown in browser
***************************

It happens often that the browser shows cached data instead of the updated html files. As a result, if you don't
see your changes, try to empty/delete the cache of your browser (see, e.g., this
`guide <https://its.uiowa.edu/support/article/719>`_).

No changes shown in online docs
**********************************

It can happen that, after pushing your changes to the ``origin`` repository, no changes are shown on the actual
website (e.g., on tudat-space or on this website). Some suggestions to identify the problem will follow:

1. Check that you pushed to the ``main`` branch. The documentation is built by readthedocs only if changes are pushed
   to that branch.
2. Check that the build was successful. This can be monitored via the "Builds" link in the readthedocs_menu_ (see
   screenshot above). If the build was not successful, you can click on it and see the output of the build. This can
   be helpful to identify where things are going wrong.

.. figure:: _static/build_output.png
    :width: 600px
    :align: center


Sphinx commands not working
********************************

If a sphinx command does not work, for instance the following:

.. code-block::

    .. toctree::
       intro
       guide

it can be due to many things, but before going crazy into debugging mode, check that the amount of spaces before
``intro`` and ``guide`` correspond to three empty spaces. Sphinx requires *three* empty spaces, but
the tab key corresponds to *four* empty spaces: if you use it in sphinx commands, it can generate a lot of confusion
because the extra white space will break the sphinx command and it is *very* difficult to notice as well.
To be clear, this will likely **not** work:

.. code-block::

    .. toctree::
        intro
        guide
