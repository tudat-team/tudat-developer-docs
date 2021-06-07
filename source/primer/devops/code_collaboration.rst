
Code Collaboration
==================

This section describes the use of Git and Github in relation to standard
Tudat developer use cases. This chapter does not serve as a complete tutorial
on Git, but rather as common practices with fundamentals of the Git
workflow (or Gitflow) used by a Tudat Developer.

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

.. admonition:: :fa:`graduation-cap` Learning Objectives
    :class: learning-objectives

    .. include:: objectives/code_collaboration.rst

Cloning a Repository
--------------------

Cloning a repository is a straightforward process. Each repository on GitHub
has a green :badge:`Code,badge-success badge-pill` button. After clicking this
button, you can then choose to "Clone with HTTPS" by clicking the clipboard
icon under the dropdown and executing:

.. code-block:: bash

    git clone <repository_url>

The primary version of the repository source code will be cloned.

.. note::
    The ``master`` branch has commonly served as this primary version of a
    repository, though Github has changed this default to ``main`` in recent
    times in an effort to align with political correctness. ``master`` and
    ``main`` will be used interchangeably in this document, where images or
    repositories have not been updated.

    .. todo::
        Update all graphics, documentation and repositories to the new default ``main``.

.. admonition:: :fa:`terminal` **Try it yourself!**

    After entering your desired directory with the ``cd`` command, clone the
    ``developer-primer`` repository :cite:p:`developer-primer0.0.1`:

    .. code-block:: bash

        $ git clone https://github.com/tudat-team/developer-primer.git

    You now have a local repository set to the ``main`` branch of the remote
    `developer-primer` repository 🎉

    .. code-block::

        developer-primer
        ├── .authors
        │   ├── AUTHORS
        │   ├── .authors.yml
        │   └── .mailmap
        ├── bibtex.bib
        ├── CHANGELOG.rst
        ├── docs
        │   ├── build
        │   ├── make.bat
        │   ├── Makefile
        │   └── source
        ├── environment.yaml
        ├── .gitignore
        ├── LICENSE
        ├── news
        │   └── TEMPLATE.rst
        ├── README.rst
        ├── rever.xsh
        └── source
            └── tree_trunk.txt

    There's a lot going on in the Repository structure, don't be overwhelmed. By
    the end of the Primer, you will have all the knowledge required to navigate it
    like a pro Tudat Developer.

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

.. note::

    The ``-u`` flag simply tells Git to track the newly created remote branch.

This branch will contain the complete history of the project, whereas ``master``
will contain an abridged version. Other developers should now clone the central
repository and create a tracking branch for ``develop``. If you form part of
this group, (i.e. a ``develop`` branch already exists on the remote) you can
create a tracking branch for ``develop`` by executing:

.. code-block:: bash

    git checkout --track origin/develop

A tracking branch simply means that you have a local version of a branch
that is connected to an existing remote version. This relationship is
invaluable as it provides two major benefits:

1. Pushing and pulling becomes a lot easier.
    - ``git push origin develop`` replaced by shorthand ``git push``
    - ``git pull origin develop`` replaced by shorthand ``git pull``
2. Git will now inform you about "unpushed" and "unpulled" commits.

.. admonition:: :fa:`terminal` **Try it yourself!**

    With the ``developer-primer`` repository :cite:p:`developer-primer0.0.1`
    cloned, check what branches exist on the remote:

    .. code-block:: console

        $ git branch -r
        origin/HEAD -> origin/main
        origin/develop
        origin/main

    You can think of the ``HEAD`` as the "current branch". The output above shows
    that there there is indeed a ``develop`` branch available on the remote.
    Let's create a local tracking branch:

    .. code-block:: console

        $ git checkout --track origin/develop
        Branch 'develop' set up to track remote branch 'develop' from 'origin'.
        Switched to a new branch 'develop'

    Congratulations, you are now on your local version of the ``develop``
    branch, which is tracking the remote version of ``develop`` 🎉

Feature Branches
----------------

Each new feature should reside in its own branch, which can be pushed to the
central repository for backup/collaboration. But, instead of branching off of
``master``, ``feature`` branches use ``develop`` as their parent branch. When a
feature is complete, it gets merged back into ``develop``. Features should
never interact directly with ``master``. :cite:p:`atlassian-gitflow`

.. raw:: html
    :file: graphics/gitflow2.svg

.. note::
    Note that ``feature`` branches combined with the ``develop`` branch is, for
    all intents and purposes, the Feature Branch Workflow. But, the Gitflow
    Workflow doesn’t stop there. ``Feature`` branches are generally created off
    to the latest ``develop`` branch.

Creating a feature branch
*************************

.. tabbed:: Standard ``git``

    .. code-block:: console

        $ git checkout develop
        $ git checkout -b feature/name

.. tabbed:: With ``git-flow`` extension

    .. code-block:: console

        $ git flow feature start feature_name

Continue your work and use Git as demonstrated beforehand.

.. admonition:: :fa:`terminal` **Try it yourself!**

    With the ``developer-primer`` repository :cite:p:`developer-primer0.0.1`,
    ensure that the ``develop`` branch is checked out, and create a new local
    feature branch with your Github username as the feature name.

    .. code-block:: console

        $ git checkout develop
        Already on 'develop'
        Your branch is up to date with 'origin/develop'.
        $ git checkout -b feature/ggarrett13_was_here
        Switched to a new branch 'feature/ggarrett13_was_here'

    After creating a feature that is appropriate for the planned work, carry
    out the work! Just for sake of example in modifying the ``source`` of a
    project, carve "<your_github_name> was here!" to the tree
    trunk contained in the source directory, using the command:

    .. note::
        This is just some arbitrary example "work" of modifying a projects
        source code for sake of example, not a convention or standard.

    .. code-block:: console

        $ echo "ggarrett13 was here!" >> source/tree_trunk.txt

    Your message will be appended to the bottom of the ``tree_trunk.txt``:

    .. code-block:: text
        :caption: ``source/tree_trunk.txt``

        ----- This is a tree trunk -----
        ggarrett13 was here!

    Stage ``source/tree_trunk.txt`` to be committed:

    .. code-block:: console

        $ git add source/tree_trunk.txt

    Finally, commit the changes made to your feature branch:

    .. code-block:: console

        $ git commit -m "ggarrett13 was here!"
        [feature/ggarrett13_was_here 6810969] ggarrett13 was here!
         1 file changed, 1 insertion(+)

    You're all set to leave your first mark on the Tudat
    Space community.

Finishing a feature branch
**************************

When you’re done with the development work on the feature, the next step is to
merge the ``feature/name`` into ``develop``.

.. code-block:: console

        $ git checkout develop
        $ git merge feature/name

.. admonition:: :fa:`terminal` **Try it yourself!**

    Continuing with the ``developer-primer`` repository :cite:p:`developer-primer0.0.1`,
    checkout the ``develop`` branch in your local repository and merge your
    feature into it.

    .. code-block:: console

        $ git checkout develop
        Switched to branch 'develop'
        Your branch is up to date with 'origin/develop'.
        $ git merge feature/ggarrett13_was_here
        Updating e2285f3..6810969
        Fast-forward
         source/tree_trunk.txt | 1 +
         1 file changed, 1 insertion(+)

    Finally, push the changes to the remote:

    .. code-block:: console

        $ git push
        Counting objects: 4, done.
        Delta compression using up to 8 threads.
        Compressing objects: 100% (3/3), done.
        Writing objects: 100% (4/4), 364 bytes | 364.00 KiB/s, done.
        Total 4 (delta 1), reused 0 (delta 0)
        remote: Resolving deltas: 100% (1/1), completed with 1 local object.
        To https://github.com/tudat-team/developer-primer.git
           e2285f3..6810969  develop -> develop

    Congratulations, you've just officially made your first mark on the
    Tudat Space community as a Tudat Developer! 🎉



Release Branches
----------------

.. todo:: Complete Release Branches section. Currently not a common part of
        the Tudat Developer workflow, but will be soon!

Hotfix Branches
---------------

.. todo:: Complete Hotfix Branches section. Currently not a common part of
        the Tudat Developer workflow, but will be soon!


.. admonition:: :fa:`list` **Chapter Summary**

    **Gitflow Workflow** :cite:p:`atlassian-gitflow`

    1. A ``develop`` branch is created from ``master``
    2. A ``release`` branch is created from ``develop``
    3. ``Feature`` branches are created from ``develop``
    4. When a ``feature`` is complete it is merged into the ``develop`` branch
    5. When the ``release`` branch is done it is merged into ``develop`` and ``master``
    6. If an issue in ``master`` is detected a ``hotfix`` branch is created from ``master``
    7. Once the ``hotfix`` is complete it is merged to both ``develop`` and ``master``
