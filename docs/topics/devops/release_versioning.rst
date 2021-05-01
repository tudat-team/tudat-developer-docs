
Release Versioning
==================

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`graduation-cap` Learning Objective(s)

    ^^^

    1. Understand what "dependency hell" is and how to avoid it.
    2. Understand ``MAJOR.MINOR.PATCH`` and when each of them are bumped.
    3. Understand what happens when ``rever <new_version_number>`` is executed.
    4. Understand how to maintain the automated changelog.

This section describes the bookkeeping required in maintaining a changelog
with a Tudat repository. The system is simple, and only requires a consistent
approach and a decent understanding of ``Rever``. The result is a well kept
changelog, providing traceability in development.


Semantic Versioning
-------------------

    In the world of software management there exists a dreaded place called
    “dependency hell.” The bigger your system grows and the more packages you
    integrate into your software, the more likely you are to find yourself, one
    day, in this pit of despair. :cite:p:`preston-werner`

Given a version number ``MAJOR.MINOR.PATCH``, increment the:

- ``MAJOR`` version when you make incompatible API changes,
- ``MINOR`` version when you add functionality in a backwards compatible manner, and
- ``PATCH`` version when you make backwards compatible bug fixes.
Additional labels for pre-release and build metadata are available as extensions to the ``MAJOR.MINOR.PATCH`` format.

``rever.xsh``
-------------

.. code-block:: bash

    $PROJECT = 'rever'
    $ACTIVITIES = [
                  'version_bump',  # Changes the version number in various source files (setup.py, __init__.py, etc)
                  'changelog',  # Uses files in the news folder to create a changelog for release
                  'tag',  # Creates a tag for the new version number
                  'push_tag',  # Pushes the tag up to the $TAG_REMOTE
                  'pypi',  # Sends the package to pypi
                  'conda_forge',  # Creates a PR into your package's feedstock
                  'ghrelease'  # Creates a Github release entry for the new tag
                   ]
    $VERSION_BUMP_PATTERNS = [  # These note where/how to find the version numbers
                             ('rever/__init__.py', r'__version__\s*=.*', "__version__ = '$VERSION'"),
                             ('setup.py', r'version\s*=.*,', "version='$VERSION',")
                             ]
    $CHANGELOG_FILENAME = 'CHANGELOG.rst'  # Filename for the changelog
    $CHANGELOG_TEMPLATE = 'TEMPLATE.rst'  # Filename for the news template
    $PUSH_TAG_REMOTE = 'git@github.com:regro/rever.git'  # Repo to push tags to

    $GITHUB_ORG = 'regro'  # Github org for Github releases and conda-forge
    $GITHUB_REPO = 'rever'  # Github repo for Github releases  and conda-forge