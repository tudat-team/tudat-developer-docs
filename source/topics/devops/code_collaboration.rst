
Code Collaboration
==================

This section describes the use of Git and Github in relation to standard
Tudat developer use cases. This chapter does not serve as a complete tutorial
on Git, but rather as common practices with fundamentals of the Git
workflow (or Gitflow) used by the Tudat Team.

.. note::
        Git comes with the Anaconda and Miniconda
        distributions by default. If you are using Conda, then Git is already
        available in your Conda command-line interface (specific to your OS).

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
    3. Understand the Tudat Git workflow.
    4. Make your first contribution to Tudat.


Develop and Master Branches
---------------------------

Instead of a single ``master`` branch, this workflow uses two branches to record
the history of the project. The ``master`` branch stores the official release
history, and the ``develop`` branch serves as an integration branch for features.
It's also convenient to tag all commits in the ``master`` branch with a version
number. :cite:p:`atlassian-gitflow`

.. raw:: html
    :file: graphics/gitflow1.svg

The first step is to complement the default ``master`` with a ``develop`` branch. A
simple way to do this is for one developer to create an empty ``develop`` branch
locally and push it to the server (remote):

.. code-block:: bash

    git branch develop
    git push -u origin develop

Existing ``develop`` on remote
******************************

It may be the case that a ``develop`` branch already exists on the remote. To
see all remote branches:

.. code-block:: bash

    git branch -r

If the newly created local ``develop`` branch (copied from ``master``) is
even with the remote ``develop``, then pushing the local ``develop`` branch
will result in no hitch. However, if there are differences, it may be that
development is already ongoing, and ``develop`` is ahead of ``master``. In this
case, it would be preferable to switch to the remote ``develop``:

.. code-block:: bash

    git branch origin develop


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`terminal` **Try it yourself!**

    ^^^

    .. code-block:: console

        $ git branch -r
        origin/HEAD -> origin/main
        origin/main

    You can think of the ``HEAD`` as the "current branch". The output above shows
    that there aren't any ``develop`` branches available on the remote. Let's
    create one:



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

Note that feature branches combined with the develop branch is, for all intents
and purposes, the Feature Branch Workflow. But, the Gitflow Workflow doesn’t
stop there. Feature branches are generally created off to the latest develop
branch.

Creating a feature branch
*************************

.. tabbed:: Standard ``git``

    .. code-block:: console

        $ git checkout develop
        $ git checkout -b feature_branch

.. tabbed:: With ``git-flow`` extension

    .. code-block:: console

        $ git flow feature start feature_branch

Release Branches
----------------


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`list` **Chapter Summary**

    ^^^

    1. Understand the differences between Git and Github.
    2. Clone and manage repositories from Github.
    3. Understand the Tudat Git workflow.
    4. Make your first contribution to Tudat.