
Contribution Checklist
---------------------------

This is a step-by-step guide for Tudat developers. Since Tudat is an open-source project, a developer is someone who
wants to add or improve something within the Tudat ecosystem. This includes for instance software
development and documentation. In this guide, we make no difference between a developer who is part of the core
tudat team and a developer outside of it. In addition, in this guide we assume that a developer is extending
functionalities directly from tudat `source code <https://github.com/tudat-team/tudat>`_ (in C++), which then
requires to expose code to `tudatpy <https://github.com/tudat-team/tudatpy>`_ (in Python) and write
associated `documentation <https://github.com/tudat-team/tudat-multidoc>`_. If a developer is not following exactly
these steps, they may skip some of the elements in the checklist.

The DevOps checklist is separated in two. One checklist is made for the developer that will for instance add features
or documentation. The second checklist is made for the reviewer to approve and distribute the changes made by te developed.

Checklist for developer
***********************


1. Preliminary operations:

   a. Fork original `tudat <https://github.com/tudat-team/tudat>`_ repo and set original repo as upstream.
   b. Branch out from the ``develop`` branch and open a ``feature/FEATURE_NAME`` branch (in tudat-multidoc for
      documentation, tudatpy for code exposition to Python, etc…).

2. Develop:

   a. Write code for new functionalities.
   b. Write new unit tests (in C++ and/or Python depending on the nature of the functionalities).
   c. Run tests and experiment with the local build.

3. Expose and document:

   a. Expose the new C++ code in `tudatpy <https://github.com/tudat-team/tudatpy>`_ (to do so, follow the same steps in 1
      and 2).
   b. Write docstrings for the associated API reference in `tudat-multidoc <https://github.com/tudat-team/tudat-multidoc>`_ (to do so, follow the same steps in 1
      and 2).
   c. [Optional] Add further documentation on `tudat-space <https://github.com/tudat-team/tudat-space>`_ and
      examples of new functionality in `tudatpy-examples <https://github.com/tudat-team/tudatpy-examples>`_.

4. Final operations:

   a. Open a Pull Request (PR) into the `develop` branch of each of the relevant repositories (for code,
      documentation, examples, etc...).
   b. Interact with a reviewer and, if necessary, implement the requested modifications.

Checklist for reviewer
***********************

Once the PR has been approved, the reviewer (or a member of the core tudat team) will:

1. Build and test new conda packages on all operating systems.
2. If a release is needed:

   a. Open release branch.
   b. Release new version with `bumpversion`.
   c. Release new version on Github.
   d. Trigger build of new conda packages.
   e. Trigger new build of documentation and release new version.

.. tip::

    For documentation, it is possible to merge the `feature` branch directly into `master` to speed up the process.

.. note::

    The steps for the reviewer will be soon automated. A beta version of such system is already in place, the current
    status and guide can be retrieved `here <https://hackmd.io/@mJnsnK9eTqSUJ_WudSrPEQ/S1u1_2Vbc>`_.

DevOps resources
****************

Below, you can find specific guides for DevOps in tudat.

.. seealso:: There are also detailed guides about :ref:`Software Development` and :ref:`Software Documentation`.

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
