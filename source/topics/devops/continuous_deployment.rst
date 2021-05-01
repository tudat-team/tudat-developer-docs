
Continuous Deployment
=====================

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`graduation-cap` Learning Objectives

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

The previous section described the concepts that found the creation of a Conda
package. This section will describe how packages are built, tested and
deployed using an open source continuous deployment (CD) system built by
the ``conda-forge`` community: ``conda-smithy``.

.. note:: ``conda-smithy`` can also be used as a continuous integration (CI)
        and continuous delivery system.

Azure
-----

Microsoft Azure, commonly referred to as Azure, is a cloud computing service
created by Microsoft for building, testing, deploying, and managing
applications and services through Microsoft-managed data centers.

