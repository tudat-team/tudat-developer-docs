
Release Versioning
==================

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`graduation-cap` Learning Objective(s)

    ^^^

    1. Understand ``MAJOR.MINOR.PATCH`` and when each of them are bumped.

    2. Understand what happens when ``rever <new_version_number>`` is executed.

    3. Understand how to maintain the automated changelog.

This section describes the bookkeeping required in maintaining a changelog
with a Tudat repository. The system is simple, and only requires a consistent
approach and a decent understanding of ``Rever``. The result is a well kept
changelog, providing traceability in development.

Semantic Versioning
-------------------

    In the world of software management there exists a dreaded place called
    “dependency hell.” The bigger your system grows and the more packages you
    integrate into your software, the more likely you are to find yourself, one
    day, in this pit of despair.

:cite:p:`preston-werner`

Given a version number ``MAJOR.MINOR.PATCH``, increment the:

MAJOR version when you make incompatible API changes,
MINOR version when you add functionality in a backwards compatible manner, and
PATCH version when you make backwards compatible bug fixes.
Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.
