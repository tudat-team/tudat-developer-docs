Continuous Integration
=====================

.. admonition:: :fa:`graduation-cap` Learning Objectives

    .. include:: objectives/continuous_integration.rst

In the context of Tudat, Continuous Integration is used to streamline the development process.
Thanks to it, developers need not worry about every step required to build and release the conda packages and documentation.
Instead, they can either wait for nightly releases that are made automatically, or add specific tags in a commit message and let everything else run hidden trough :ref:`GitHub<GitHub actions>`, :ref:`Azure<Azure>`, :ref:`Anaconda<Anaconda>`, and :ref:`Readthedocs<Readthedocs>`.

GitHub actions
--------------
.. image:: https://github.com/tudat-team/.github/actions/workflows/webservices.yml/badge.svg
    :target: https://github.com/tudat-team/.github/actions/workflows/webservices.yml

GitHub actions are integrated in Tudat development process to ease and automate the build and release of conda packages.

Most importantly, the `webservices-dispatch-action repository <https://github.com/tudat-team/webservices-dispatch-action>`_ contains code that is used to trigger a build of a conda package.
More information on how this action works is given in that repo's `README <https://github.com/tudat-team/webservices-dispatch-action/blob/main/README.md>`_.

In essence, once triggered, this action can do two distinct things:

* Bump the version of the project and project feedstock repositories.
* Re-render the feedstock repository, then bump the version as above.

It is worth noting that this action makes the distinction between ``main``/``master`` repositories, and ``dev``/``develop`` repositories, so that the proper versions are bumped, and the correct build triggered.

In both cases, if changes are caused by the action, they are automatically pushed first to the project repository, then to the feedstock repository.
As a reminder, pushing to the feedstock repository will then trigger a build of the conda package trough Azure (as discussed :ref:`below<Azure>`).

Last but not least, this action is triggered automatically either every 24 hours (nightly), or by adding a ``[CI]`` or ``[rerender]`` tag in a commit to a project repository.
Do note that the emplacement of this tag in the commit message, as well as the capitalisation, do not matter.
In case the ``[rerender]`` tag is used, the feedstock repository will be rerendered, but the version number will not be bumped.
If the ``[CI]`` tag is used or it is a nightly release, the version will be bumped, then the feedstock will be rerendered.

Looking at the webservices-dispatch-action `main.py <https://github.com/tudat-team/webservices-dispatch-action/blob/main/main.py>`_ script, it is important to understand that, even though this script is in Python and run on a GitHub server, any classic Linux command can in principle be run.
For instance, the following line in Python is used to trigger rerendering of the clone feedstock (where the ``cwd`` argument specifies in which directory to run the command, and the ``stdout``/``stderr`` arguments specify where to redirect the command output):

.. code-block:: Python

    subprocess.Popen(["conda", "smithy", "rerender"], cwd=FEEDSTOCK_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

Whereas, in Linux, the command would directly be run in a terminal as:

.. code-block:: bash

    conda smithy rerender

Similarly, the `main.py <https://github.com/tudat-team/webservices-dispatch-action/blob/main/main.py>`_ script clones the project and feedstock repositories locally on the GitHub action server.
Then, the files that are locally cloned can be read, edited, and pushed to the repositories as one would usually do on a local machine.

The main issue with running code on the GitHub action server is that the code is trickier to debug, since it runs in the cloud. However, the following can be used for testing:

* The script can be run locally by cloning the `webservices-dispatch-action repository <https://github.com/tudat-team/webservices-dispatch-action>`_ and editing the ``test_env`` variable at the bottom from ``False`` to ``True``. This will then fake the action trigger locally, so that the code can be stopped at any point, and variables/files inspected.
* Logs of the script running in the cloud can be inspected at the following page: https://github.com/tudat-team/.github/actions/workflows/webservices.yml.

Azure
-----
.. image:: https://dev.azure.com/tudat-team/feedstock-builds/_apis/build/status/tudat-feedstock
    :target: https://dev.azure.com/tudat-team/feedstock-builds/_build?definitionId=2
.. image:: https://dev.azure.com/tudat-team/feedstock-builds/_apis/build/status/tudatpy-feedstock
    :target: https://dev.azure.com/tudat-team/feedstock-builds/_build?definitionId=3

Azure pipelines are used to build the conda packages and release them, for all supported platforms (Linux, Windows, OSx, and OSx arm64).

Once triggered, a Azure pipeline will clone the project and feedstock repositories of the given tudat-related project (tudat, tudatpy, tudat-resources, ...), and for the correct branch (``main`` or ``dev``).

First of all, a distinction is made if the build is for tudatpy on the Linux platform. This is because, afterwards, the tudatpy documentation is generated by Readthedocs using the tudatpy conda package for Linux (as discussed :ref:`below<Readthedocs>`).
In this case, the docstrings of tudatpy are parsed, generating the documentation in the ``docstrings.h`` header file.
This is done by calling `build_docstrings.py <https://github.com/tudat-team/tudatpy/blob/01c5335728c52fe776cbc01c016d613b564e3ee0/docs/source/build_docstrings.py>`_ in the `recipe/build.sh <https://github.com/tudat-team/tudatpy-feedstock/blob/77507bc6587ef752ffd01f17b466b6b1d7e1eea5/recipe/build.sh>`_ bash script.

Afterwards, whether the docstrings are generated or not, the conda package is built. This is done by running the sequence of commands from the `recipe/build.sh <https://github.com/tudat-team/tudatpy-feedstock/blob/77507bc6587ef752ffd01f17b466b6b1d7e1eea5/recipe/build.sh>`_ bash script: ``cmake``, ``make``, and ``make install``.
This is a somewhat similar process as described for users compiling tudatpy locally from the `tudat-bundle repository <https://github.com/tudat-team/tudat-bundle>`_.

Once a build is made, it is then packaged using conda. Among other things, all the required dependencies to install the package are specified, as well as the package metadata. 

Then, as soon as an Azure build and conda package is successfully completed for any platform, the generated conda package is uploaded to Anaconda (as discussed :ref:`below<Anaconda>`).

Finally, logs of the Azure pipeline can be inspected at the following pages: `tudat Azure logs <https://dev.azure.com/tudat-team/feedstock-builds/_build?definitionId=2>`_ / `tudatpy Azure logs <https://dev.azure.com/tudat-team/feedstock-builds/_build?definitionId=3>`_.

Anaconda
---------
.. image:: https://anaconda.org/tudat-team/tudat/badges/version.svg
    :target: https://anaconda.org/tudat-team/tudat
.. image:: https://anaconda.org/tudat-team/tudatpy/badges/version.svg
    :target: https://anaconda.org/tudat-team/tudatpy

Anaconda is used to store packages that have been build by Azure. Then, any user can automatically install the packages for its given platform (Linux, Windows, OSx, or OSx arm64), using the ``conda install`` command.
This will also take care of letting user update packages to the latest version, or to rollback to a specific version.

Readthedocs
-----------
.. image:: https://readthedocs.org/projects/tudatpy/badge/?version=latest
    :target: https://readthedocs.org/projects/tudatpy/builds/

After a full pipeline is successfully completed for all platforms for tudatpy, a trigger is made so the documentation is generated by Readthedocs.
This is done trough setting a new Azure pipeline that executes after a tudatpy pipeline is fully completed, using a `Build completion trigger`, as described in the `Azure documentation <https://docs.microsoft.com/en-us/azure/devops/pipelines/process/pipeline-triggers-classic?view=azure-devops#add-a-build-completion-trigger>`_.
For a developer with access to the tudat-team Azure space, these settings can be found at `this page <https://dev.azure.com/tudat-team/feedstock-builds/_apps/hub/ms.vss-ciworkflow.build-ci-hub?_a=edit-build-definition&id=8&view=Tab_Triggers>`_.
This new pipeline has the sole objective of running the following command:

.. code-block:: bash

    curl -X POST -d "token=<SECRET-READTHEDOCS-TOKEN>" https://readthedocs.org/api/v2/webhook/tudatpy/200830/

This ``curl`` command sends a POST request to the Readthedocs webhook API, with the secret token as the payload, which triggers the API documentations build.
This ensure that:

* The documentation is always generated for the latest version of the package.
* The documentation is only generated after the package is successfully built for all platforms.

To save time and resources on Readthedocs, the `source/conf.py <https://github.com/tudat-team/tudatpy/blob/01c5335728c52fe776cbc01c016d613b564e3ee0/docs/source/conf.py>`_ automatically detects if the build is running on Readthedocs.
If so, the ``tudatpy`` conda package is installed from Anaconda, using the ``conda install`` command.
If the latest package hosted on Anaconda is a ``dev`` version, the documentation needs to be generated from the ``tudat-team/label/dev tudatpy`` conda package.
This is done by comparing the JSON information of the `stable <https://conda.anaconda.org/tudat-team/label/main/linux-64/repodata.json>`_ and `dev <https://conda.anaconda.org/tudat-team/label/dev/linux-64/repodata.json>`_ Anaconda repositories.

Then, once the appropriate conda package is installed, the documentation is generated by extracting the docstrings from each of the methods in the ``tudatpy`` package, as done by the `document.py <https://github.com/tudat-team/tudatpy/blob/develop/docs/source/document.py>`_ script.

Once done, the new version of the API docs is uploaded to Readthedocs and accessible to users.