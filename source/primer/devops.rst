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

    .. include:: devops/objectives/code_collaboration.rst

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`bullhorn` :ref:`Release Versioning`

    ^^^

    .. include:: devops/objectives/release_versioning.rst


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


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`cloud-upload` :ref:`Continuous Integration`

    ^^^

    .. include:: devops/objectives/continuous_integration.rst


.. toctree::
   :maxdepth: 2
   :caption: Topics
   :hidden:

   devops/code_collaboration
   devops/release_versioning
   devops/package_manager
   devops/continuous_deployment
   devops/continuous_integration

.. _test: https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment
