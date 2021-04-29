Development Operations
======================

DevOps is a set of practices that combines software development (Dev) and
IT operations (Ops) :cite:p:`wiki:DevOps`. Tudat relies on open
source solutions for development; GitHub for its hosted version control
system (VCS), :ref:`Conda` for it's package manager, and :ref:`Azure` for it's
continuous integration (CI) service.

.. toctree::
   :maxdepth: 2
   :caption: Topics
   :hidden:

   devops/code_collaboration
   devops/release_versioning
   devops/package_manager
   devops/continuous_deployment

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`github` :ref:`Code Collaboration`

    ^^^

    This section describes the processes and tools that go into building,
    testing and deploying packages hosted in the cloud, enabling the
    following badges:

    .. code-block:: bash

        git clone <repo>
        git commit -m "Message"
        git push

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`bullhorn` :ref:`Release Versioning`

    ^^^

    This section describes the use of the following command:

    .. code-block:: bash

        rever <new_version_number>

    which takes complete care of releasing new versions to be merged onto the
    main git branch.


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

    This section describes the processes and tools that go into building,
    testing and deploying packages hosted in the cloud, enabling the
    following badges:

    .. image:: https://anaconda.org/tudat-team/tudatpy/badges/version.svg
        :target: https://anaconda.org/tudat-team/tudatpy

    .. image:: https://anaconda.org/tudat-team/tudatpy/badges/platforms.svg
        :target: https://anaconda.org/tudat-team/tudatpy


.. _test: https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment
