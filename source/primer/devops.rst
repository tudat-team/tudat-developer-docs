Development Operations
======================

DevOps is a set of practices that combines software development (Dev) and
IT operations (Ops) :cite:p:`wiki:DevOps`. Tudat relies on open
source solutions for development: GitHub for its hosted version control
system (VCS), :ref:`Conda` for its package manager, and :ref:`Azure` for its
continuous integration (CI) service.

This section explains how you can make a successful contribution to tudat. It will also point you to the right guides
and resources to learn in more detail about the different steps.

.. admonition:: :fa:`graduation-cap` Learning Objectives

       .. include:: devops/objectives/devops.rst


DevOps checklist
---------------------------

This is a step-by-step guide for Tudat developers. Since Tudat is an open-source project, a developer is someone who
wants to add or improve something within the Tudat ecosystem. This includes, but it is not limited to, software
development, documentation, etc... In this guide, we make no difference between a developer who is part of the core
tudat team and a developer outside of it. In addition, in this guide we assume that a developer is extending
functionalities directly from the tudat's `source code <https://github.com/tudat-team/tudat>`_ in C++, which then
requires to expose code to `tudatpy <https://github.com/tudat-team/tudatpy>`_ and write
associated `documentation <https://github.com/tudat-team/tudat-multidoc>`_. If a developer is not following exactly
these steps, they may skip some of the steps.

.. note:: The useful resources for each step are linked to below the checklists.


Checklist for developer
***********************


1. Preliminary operations:

   a. Fork original `tudat <https://github.com/tudat-team/tudat>`_ repo and set original repo as upstream
   b. Branch out from the ``develop`` branch and open a ``feature/FEATURE_NAME`` branch tudat-multidoc for
      documentation, etc…)

2. Develop:

   a. write code for new functionalities
   b. write new unit tests
   c. run tests and test build locally

3. Expose and document:

   a. expose C++ code in `tudatpy <https://github.com/tudat-team/tudatpy>`_ (to do so, follow the same steps in 1
      and 2)
   b. write docstrings for the associated API reference in `tudat-multidoc <https://github.com/tudat-team/tudat-multidoc>`_ (to do so, follow the same steps in 1
      and 2)
   c. [optional] add further documentation on `tudat-space <https://github.com/tudat-team/tudat-space>`_ and
      examples of new functionality in `tudatpy-examples <https://github.com/tudat-team/tudatpy-examples>`_

4. Final operations:

   a. open a Pull Request (PR) into the `develop` branch of each of the relevant repositories (both for code and
      documentation)
   b. interact with a reviewer and, if necessary, implement the requested modifications

Checklist for reviewer
***********************

Once the PR has been approved, the reviewer (or a member of the core tudat team) will:

1. build and test new conda packages on all operating systems
2. if a release is needed:

   a. open release branch
   b. release new version with `bumpversion`
   c. release new version on Github
   d. trigger build of new conda packages
   e. trigger new build of documentation and release new version

.. tip::

    For documentation, it is possible to merge the `feature` branch directly into `master` to speed up the process.

.. note::

    The steps for the reviewer will be soon automated. A beta version of such system is already in place, the current
    status and guide can be retrieved `here <https://hackmd.io/@mJnsnK9eTqSUJ_WudSrPEQ/S1u1_2Vbc>`_.


DevOps resources
****************

Below, you can find specific guides for DevOps in tudat.

.. seealso:: There are also detailed guides about :ref:`Software Development` and :ref:`Software Documentation` in the
   respective sections.

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`github` :ref:`Code Collaboration`

    ^^^

    .. include:: devops/objectives/code_collaboration.rst

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`bullhorn` :ref:`Release versioning`

    ^^^

    .. include:: devops/objectives/versioning.rst


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`cubes` :ref:`Package Management`

    ^^^

    .. include:: devops/objectives/package_manager.rst


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`cloud-upload` :ref:`Continuous Deployment`

    ^^^

    .. include:: devops/objectives/continuous_deployment.rst


.. toctree::
   :maxdepth: 2
   :caption: Topics
   :hidden:

   devops/code_collaboration
   devops/versioning
   devops/package_manager
   devops/continuous_deployment

.. _test: https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment
