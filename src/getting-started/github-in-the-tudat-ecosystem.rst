.. _GitHub in the Tudat Ecosystem:

=============================
GitHub in the Tudat Ecosystem
=============================

.. _GitHub Actions: https://docs.github.com/en/actions

Introduction
------------

Welcome to the `Tudat Team on GitHub`_, the heartbeat of the Tudat ecosystem.
This organization is the central repository for all the development and
maintenance activities related to Tudat—an advanced computational framework
designed to facilitate research in astrodynamics and space sciences.

.. image:: /assets/screenshots/github_homepage.png
   :alt: GitHub Homepage of Tudat-Team
   :target: https://github.com/tudat-team
   :align: center

This organization leverages GitHub for :term:`Version Control` System (VCS),
comprehensive project management, and community engagement through discussions.
Additionally, we employ `GitHub Actions`_ for a streamlined :term:`DevOps`
pipeline. Further details can be found in specific sections of this
documentation.

GitHub Repositories
-------------------

.. mermaid:: /assets/mermaid/github/github.mmd
   :light-theme: light
   :dark-theme: dark

Core Repositories
^^^^^^^^^^^^^^^^^

- `tudat-bundle`_: This is the primary repository for setting up a Tudat
  development environment. It includes all essential dependencies, making the
  initial setup process more straightforward and efficient.

- `tudat`_: The fundamental library of the Tudat ecosystem, written in C++. It
  offers a comprehensive suite of tools and features specifically designed for
  astrodynamics and space science research.

- `tudatpy`_: Acts as a bridge between the robust capabilities of Tudat's C++
  core and the simplicity of Python. `tudatpy` extends Tudat's high-performance
  space research functionalities to the versatile environment of Python.

Dependencies
^^^^^^^^^^^^

- `tudat-resources`_: Functions as a dedicated resource manager. It separates
  non-code assets from the main `tudat` repository, ensuring more efficient
  resource management and accessibility for the community.

- `webservices-dispatch-action`_: A crucial GitHub action in the Tudat
  ecosystem, aimed at enhancing development workflows. It simplifies complex
  development aspects for the tudat-team by automating various tasks related to
  the Tudat and `tudatpy` repositories.

- `sofa-cmake`_: Contains the SOFA ANSI C source code, supplemented with cmake
  files to integrate it seamlessly into Tudat. SOFA is vital for the
  implementation of standard astronomical models.

- `cspice-cmake`_: Hosts NASA’s SPICE toolkit for C programming, along with
  cmake files to facilitate integration with Tudat. SPICE is a key tool used in
  planetary science and remote sensing missions.

- `nrlmsise-00-cmake`_: Integrates the NRLMSISE-00 Atmospheric Model in C with
  additional cmake enhancements for compatibility with Tudat. This model is
  crucial for simulating Earth's atmospheric conditions.

GitHub Actions
--------------

GitHub Actions is a powerful tool for automating software development workflows
within GitHub repositories. These actions are stored within the directory
``.github/workflows`` of each repository. The following table summarizes the
actions currently implemented in the Tudat ecosystem.

- `automerge.yml`_: Comes standard in all feedstock repositories. This action
  automatically merges pull requests that pass all checks, ensuring a
  streamlined and efficient development process. This is maintained by
  ``conda-forge``. For more details on the automerge action, refer to the
  `conda-forge/automerge-action`_ repository.

  .. mermaid::
     :light-theme: light
     :dark-theme: dark

        flowchart LR
            subgraph Feedstock Repository
                direction LR
                A[Pull Request] --> B{Checks Passed?}
                B --> |Yes| C[Automerge]
                B --> |No| D[End workflow]
            end

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Workflow
     - Description
   * - `tudat-team/.github/webservice.yml`_
     - Adds in-house custom controls to the Tudat GitHub ecosystem by calling the `webservices-dispatch-action`_.
   * - `tudat-team/.github/nightly.yml <https://github.com/tudat-team/.github/blob/main/.github/workflows/nightly.yml>`_
     - Builds all `dev` packages, automatically incrementing versions, if **any changes** are detected in the `develop` branch of the `tudat` or `tudatpy` repositories.

.. _tudat-team/.github/webservice.yml: https://github.com/tudat-team/.github/blob/main/.github/workflows/webservices.yml

.. _automerge.yml: https://github.com/tudat-team/tudat-feedstock/blob/master/.github/workflows/automerge.yml

.. _conda-forge/automerge-action: https://github.com/conda-forge/automerge-action


`tudat-team/.github/nightly.yml`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. mermaid:: /assets/mermaid/github/github-nightly.mmd
   :light-theme: light
   :dark-theme: dark

.. comment::


    .. mermaid::
       :light-theme: light
       :dark-theme: dark

        flowchart LR
            A[Triggered by cron] --> B{Changes in develop branch?}
            B --> |Yes| C[Build dev packages]
            B --> |No| D[End workflow]



.. note::

    The time at which the nightly workflow is triggered is set in the
    `following lines
    <https://github.com/tudat-team/.github/blob/dd9b2e327fbc8a46fd2646d349b957fd88466ad5/.github/workflows/nightly.yml#L7-L8>`_

    At the time of writing, the workflow is triggered at 03:00 UTC, seen in the
    following configuration:

    .. code-block:: yaml

        on:
          schedule:
            - cron: '0 3 * * *' everyday at 3:00 a.m. https://crontab.guru/#0_3_*_*_* ,,,,,,



.. seealso::

    `GitHub Actions Documentation <https://docs.github.com/en/actions>`_


.. _Tudat Team on GitHub: https://github.com/tudat-team
.. _tudat-bundle: https://github.com/tudat-team/tudat-bundle
.. _tudat: https://github.com/tudat-team/tudat
.. _tudatpy: https://github.com/tudat-team/tudatpy
.. _tudat-resources: https://github.com/tudat-team/tudat-resources
.. _sofa-cmake: https://github.com/tudat-team/sofa-cmake
.. _cspice-cmake: https://github.com/tudat-team/cspice-cmake
.. _nrlmsise-00-cmake: https://github.com/tudat-team/nrlmsise-00-cmake
.. _webservices-dispatch-action: https://github.com/tudat-team/webservices-dispatch-action
