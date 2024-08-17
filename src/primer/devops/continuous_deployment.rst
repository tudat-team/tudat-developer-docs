
Continuous Deployment
=====================

.. admonition:: :fa:`graduation-cap` Learning Objectives

    .. include:: objectives/continuous_deployment.rst

The previous section described the concepts that found the creation of a Conda
package. This section will describe how packages are built, tested and
deployed using an open source continuous deployment (CD) system built by
the ``conda-forge`` community: ``conda-smithy``.

.. note:: ``conda-smithy`` can also be used as a continuous integration (CI)
        and continuous delivery system.

.. attention::

    Please ensure to use the recommended following command to install
    `conda-smithy`. If not installed in the base environment, you may need to
    reinstall Miniconda/Anaconda from scratch.

.. todo::

    Elaborate on ``osx_arm64`` cross-compiled build variants. (This may only
    apply to the private ``tudat-team`` channel?)

Azure
-----

Microsoft Azure, commonly referred to as Azure, is a cloud computing service
created by Microsoft for building, testing, deploying, and managing
applications and services through Microsoft-managed data centers.

