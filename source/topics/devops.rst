Development Operations
======================

DevOps is a set of practices that combines software development (Dev) and
IT operations (Ops) :cite:p:`wiki:DevOps`. Tudat relies on open
source solutions for development; GitHub for its hosted version control
system (VCS), :ref:`Conda` for it's package manager, and :ref:`Azure` for it's
continuous integration (CI) service.

.. todo:: Discuss with team whether learning goals should be presented at this
        level or whether a clean practical use case of the section should be
        presented. (i.e. Package Management: ``conda install tudatpy``, what
        goes on behind the scenes into making this possible?)

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`github` :ref:`Code Collaboration`

    ^^^

    1. Understand the differences between Git and Github.
    2. Installing and configuring the ``git`` command for use.
    3. Create, clone and manage repositories from Github.
    4. Understand the Tudat Git workflow.

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`bullhorn` :ref:`Release Versioning`

    ^^^

    1. Understand what "dependency hell" is and how to avoid it.
    2. Understand ``MAJOR.MINOR.PATCH`` and when each of them are bumped.
    3. Understand what happens when ``rever <new_version_number>`` is executed.
    4. Understand how to maintain the automated changelog.

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`cubes` :ref:`Package Management`

    ^^^

    This section describes the processes and tools that go into the following
    executable command using Conda:

    .. code-block:: bash

        conda install tudatpy  # -c tudat-team

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`cloud-upload` :ref:`Continuous Deployment`

    ^^^

    1. Understand what ``conda-forge`` is, and what their role is with respect
       to Conda packages.
    2. Understand how ``conda-smithy`` builds, tests and packages across target OS'.
    3. Know how to inspect build status' of packages on Azure and re-trigger them.
    4. Understand common problems encountered in this workflow and how to
       resolve them.

    .. image:: https://anaconda.org/tudat-team/tudatpy/badges/version.svg
        :target: https://anaconda.org/tudat-team/tudatpy

    .. image:: https://anaconda.org/tudat-team/tudatpy/badges/platforms.svg
        :target: https://anaconda.org/tudat-team/tudatpy

.. toctree::
   :maxdepth: 2
   :caption: Topics
   :hidden:

   devops/code_collaboration
   devops/release_versioning
   devops/package_manager
   devops/continuous_deployment

.. _test: https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment
