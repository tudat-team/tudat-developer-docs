How to contribute to Tudat
===========================

.. _`Developer Primer`: https://github.com/tudat-team/developer-primer.git

The release versioning section describes the workflow and tools used in release
versioning used as a Tudat Developer.

.. admonition:: :fa:`graduation-cap` Learning Objectives

       .. include:: objectives/release_versioning.rst


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

.. seealso::

    This guide is partly based on the Gitflow concepts. Therefore, before continuing the reader should be familiar
    with the content of :ref:`Code Collaboration`.

Checklist for developer
***********************


1. Preliminary operations:

   a. Fork original `tudat <https://github.com/tudat-team/tudat>`_ repo and set original repo as upstream
   b. Branch out from the `develop` branch and open a `feature/FEATURE_NAME` branch tudat-multidoc for
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


Semantic Versioning
-------------------

Tom Preston-Werner originally proposed a simple set of rules and requirements
that provide a convention for modifying the versioning of software packages
:cite:p:`preston-werner`. The opening paragraph introduces the concept of
*dependency hell*:

    In the world of software management there exists a dreaded place called
    “dependency hell.” The bigger your system grows and the more packages you
    integrate into your software, the more likely you are to find yourself, one
    day, in this pit of despair.

This chapter relays the Semantic Versioning (SemVer) 2.0.0 convention in an
effort to avoid any developer needed "dependency hell" to be defined. It is
further mentioned that the proposed system will only work with an API
declaration:

    For this system to work, you first need to declare a public API. This may
    consist of documentation or be enforced by the code itself. Regardless, it
    is important that this API be clear and precise. Once you identify your
    public API, you communicate changes to it with specific increments to your
    version number.

The SemVer 2.0.0 can be summarised by the following set of rules: Given a
version number ``MAJOR.MINOR.PATCH``, increment the:

- ``MAJOR`` version when you make incompatible API changes,
- ``MINOR`` version when you add functionality in a backwards compatible
  manner, and
- ``PATCH`` version when you make backwards compatible bug fixes.

Additional labels for pre-release and build metadata are available as
extensions to the ``MAJOR.MINOR.PATCH`` format. SemVer only focuses on API
compatibility, however there are common labels appended to the semantic
version, for example ``1.0.0-alpha``. The list of requirements for the label
formatting are detailed in SemVer. The important takeaway is that precedence is
alphanumeric:

.. code-block::

    Precedence: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta
              < 1.0.0-beta  < 1.0.0-beta.2  < 1.0.0-beta.11
              < 1.0.0-rc.1  < 1.0.0.

.. admonition:: Example

       A proposed guided example flow is as follows:

       - ``alpha`` = in development without caring about (old) unit-tests
       - ``beta`` = in development and the old (unit) tests are valid
       - ``rc.1`` = tests for new features are written and valid
       - ``rc.2`` = additional tests had to be written and those were made valid
       - ``rc.3`` = more additional tests that were made valid

       However this is just an example flow, not a further set of rules.
       Depart from it whenever it improves your content.

              Break any of these rules sooner than say anything outright barbarous.

              — George Orwell, "`Politics and the English Language`_"

       .. _`Politics and the English Language`: https://www.orwell.ru/library/essays/politics/english/e_polit/



