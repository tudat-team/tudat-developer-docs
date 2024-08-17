Version Package Releases
===========================

.. _`Developer Primer`: https://github.com/tudat-team/developer-primer.git

This section explains how releases are dealt with in the tudat ecosystem.

.. admonition:: :fa:`graduation-cap` Learning Objectives

       .. include:: objectives/versioning.rst

.. _sem_ver:

Semantic versioning
--------------------

Tom Preston-Werner originally proposed a simple set of rules and requirements
that provide a convention for modifying the versioning of software packages
:cite:p:`preston-werner`. The opening paragraph introduces the concept of
*dependency hell*:

    In the world of software management there exists a dreaded place called
    “dependency hell.” The bigger your system grows and the more packages you
    integrate into your software, the more likely you are to find yourself, one
    day, in this pit of despair.

This chapter relays the Semantic Versioning (`SemVer <https://semver.org>`_) 2.0.0 convention in an
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


.. _bump_version:

Releasing a new version with bumpversion
-----------------------------------------

.. warning:: This section is currently only used for releasing new versions of the docs, not of the software. More
    information about how to release a new version of the software will be provided soon in this page.


Releasing a new version of the documentation is simple. To do this, we rely on `bumpversion <https://github
.com/c4urself/bump2version>`_ which in turns uses semantic versioning (see :ref:`sem_ver`). Semantic
versioning relies the following structure for stable releases: ``MAJOR.MINOR.PATCH`` (e.g., 1.3.1). For unstable
releases, the same
syntax is used with the addition of an additional tag, such as ``MAJOR.MINOR.PATCH.devBUILD`` (e.g., 1.3.1.dev2).

Once you have committed your changes, you can release a new version by typing in the terminal one of the following
commands:

- ``bumpversion patch``: this increases the patch number (the same can be done with ``bumpversion major`` or ``bumpversion minor``)
    - 1.1.1 -> 1.1.2.dev0
    - 1.1.2.dev0 -> 1.1.3.dev0
    - 1.1.2.dev1 -> 1.1.3.dev0

- ``bumpversion dev``: this increases the build number
    - 1.1.2.dev0` -> 1.1.2.dev1
    - 1.1.2` -> ❌ This will break. Patch must be bumped to start ``dev`` suffix.

- ``bumpversion release``: this releases a stable version
    - 1.1.2.dev0` -> 1.1.2
    - 1.2.0.dev0` -> 1.2.0

``bumpversion`` creates a dedicated commit every time it is executed and tags such commit with the version number.



