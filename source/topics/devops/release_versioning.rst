
Release Versioning
==================

.. attention:: The only way for this section to be relevant, is if **all**
    developers follow the details closely. No more than what is needed in your
    workflow, and minor details for establishing a mental knowledge map will
    be provided here. Please read thoroughly!

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

Rever: Releaser of Versions!
----------------------------

``rever.xsh``
*************

.. code-block:: bash

    $PROJECT = 'tudat-developer-docs'
    $ACTIVITIES = [
                  'version_bump',  # Changes the version number in various source files (setup.py, __init__.py, etc)
                  'changelog',  # Uses files in the news folder to create a changelog for release
                  'tag',  # Creates a tag for the new version number
                  'push_tag',  # Pushes the tag up to the $TAG_REMOTE
                   # 'pypi',  # Sends the package to pypi
                   # 'conda_forge',  # Creates a PR into your package's feedstock
                   # 'ghrelease'  # Creates a Github release entry for the new tag
                   ]
    $VERSION_BUMP_PATTERNS = [  # These note where/how to find the version numbers
                             ('docs/conf.py', r'release\s*=.*', "release='$VERSION'")
                             ]

    $CHANGELOG_FILENAME = 'CHANGELOG.rst'  # Filename for the changelog
    $CHANGELOG_TEMPLATE = 'TEMPLATE.rst'  # Filename for the news template
    $PUSH_TAG_REMOTE = 'git@github.com:tudat-team/tudat-developer-docs.git'  # Repo to push tags to

    $GITHUB_ORG = 'tudat-team'  # Github org for Github releases and conda-forge
    $GITHUB_REPO = 'tudat-developer-docs'  # Github repo for Github releases  and conda-forge

Adding a new Author
*******************

``.authors.yml``

News Workflow
***************

One of the most helpful features of rever is the changelog activity.
This activity produces a changelog by colating news files. The changelog is
written into the repo and can be used in the GitHub release activity.

.. important:: Ensure that you have one commit prior to executing
        ``rever <MAJOR.MINOR.PATCH>``, otherwise you will not appear as an
        author on the Change Log.

1. Go into the ``news/`` directory

2. Copy the ``TEMPLATE.rst`` file to another file in the ``news/`` directory. We suggest using the branchname:

.. code-block:: bash

    $ cp TEMPLATE.rst branch.rst

3. The news files are customizable in the ``rever.xsh`` files. However, the default template looks like:

.. code-block:: md

    **Added:**

    * <news item>

    **Changed:**

    * <news item>

    **Deprecated:**

    * <news item>

    **Removed:**

    * <news item>

    **Fixed:**

    * <news item>

    **Security:**

    * <news item>

4. In this case you can remove the ``* <news item>`` and replace it with your own news entries, e.g.:

.. code-block:: md

    **Added:**

    * New news template tutorial

    **Changed:**

    * <news item>

    **Deprecated:**

    * <news item>

    **Removed:**

    * <news item>

    **Fixed:**

    * <news item>

    **Security:**

    * <news item>

4. Commit your ``branch.rst``.

Feel free to update this file whenever you want! Please don’t use someone
else’s file name. All of the files in this news/ directory will be merged
automatically at release time. The <news item> entries will be automatically
filtered out too!

Once the project is ready for a release when running the rever command all the
files, except the template, in the news folder will be collated and merged into
a single changelog file.