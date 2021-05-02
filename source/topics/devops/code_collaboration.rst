
Code Collaboration
==================

This section describes the use of Git and Github in relation to standard
Tudat developer use cases.

.. note::
        Git comes with the Anaconda and Miniconda
        distributions by default. If you are using Conda, then git is already
        available in your Conda command-line interface (specific to your OS).

.. important::
        This chapter does not serve as a complete tutorial
        on Git, but rather as the fundamentals to the workflow used by Tudat
        Space.

        +--------------+------------------------------------------+--------------+
        | **Audience** | **Prerequisite(s)**                      | **Time**     |
        +--------------+------------------------------------------+--------------+
        | Git Beginner | .. link-button:: http://bit.ly/git-begin | ~ 10 minutes |
        |              |     :classes: btn-success btn-block      |              |
        |              |     :text: git - the simple guide        |              |
        +--------------+------------------------------------------+--------------+

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`graduation-cap` Learning Objective(s)

    ^^^

    1. Understand the differences between Git and Github.

    2. Clone and manage repositories from Github.

    4. Understand the Tudat Git workflow.

    5. Make your first contribution to Tudat.


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`users` Mission Brief

    ^^^
    If you choose to follow along with the primer, you will complete
    the following:

    - Clone the `Developer Primer`_ repository.
    - Collaborate with others by sharing an interest of yours on a feature
      branch.
    - Hotfix a fellow collaborators typo in their contributed interest.

Clone A Repository
------------------

Cloning a repository is simple. Each repository on GitHub has a dropdown
under a ``Code`` button. After entering your desired directory, the
`Developer Primer`_ repository can be cloned by:

.. _`Developer Primer`: https://github.com/tudat-team/developer-primer.git

.. code-block:: bash

    git clone https://github.com/tudat-team/developer-primer.git

You now have a local repository set to the ``master`` branch of the ``remote``
`Developer Primer`_ repository. 🎉

.. code-block::

    developer-primer
    ├── AUTHORS
    ├── CHANGELOG.rst
    ├── docs
    │   ├── build
    │   ├── make.bat
    │   ├── Makefile
    │   └── source
    ├── environment.yaml
    ├── LICENSE
    ├── news
    │   └── TEMPLATE.rst
    │  
    ├── README.md
    │  
    └── rever.xsh

There's a lot going on in the Repository structure, don't be overwhelmed. By
the end of the Primer, you will have all the knowledge required to navigate it
like a pro Tudat Developer.

Develop and Master Branches
---------------------------

Instead of a single master branch, this workflow uses two branches to record
the history of the project. The master branch stores the official release
history, and the develop branch serves as an integration branch for features.
It's also convenient to tag all commits in the master branch with a version
number. :cite:p:`atlassian-gitflow`

.. raw:: html
    :file: graphics/gitflow1.svg

The first step before making any modifications to the current
repository is to check if the ``develop`` branch exists.

.. code-block:: console

    $ git branch -r
    origin/HEAD -> origin/main
    origin/main

You can think of the ``HEAD`` as the "current branch". The output above shows
that there aren't any ``develop`` branches available on the ``remote``. Let's
create one:

.. code-block:: console

    $git branch develop
    $git push -u origin develop

.. note::

        Command variants for checking available branches and their
        descriptions:

        +-------------------+--------------------------------------+
        | **Variant**       | **Description**                      |
        +-------------------+--------------------------------------+
        | ``git branch``    | To see local branches                |
        +-------------------+--------------------------------------+
        | ``git branch -r`` | To see remote branches               |
        +-------------------+--------------------------------------+
        | ``git branch -a`` | To see all local and remote branches |
        +-------------------+--------------------------------------+




Feature Branches
----------------

Each new feature should reside in its own branch, which can be pushed to the
central repository for backup/collaboration. But, instead of branching off of
master, feature branches use develop as their parent branch. When a feature is
complete, it gets merged back into develop. Features should never interact
directly with master. :cite:p:`atlassian-gitflow`

.. raw:: html
    :file: graphics/gitflow2.svg

