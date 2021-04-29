
Continuous Deployment (CD)
==========================

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`arrows-alt,mr-1` Learning Objective

    ^^^

    This section describes the processes and tools that go into building,
    testing and deploying packages hosted in the cloud, enabling the
    following badges:

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

