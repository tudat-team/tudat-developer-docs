
Code Collaboration
==================

This section describes the use of Git and Github in relation to standard
Tudat developer use cases. This chapter does not serve as a complete tutorial
on Git, but rather as an extension to the workflow used by Tudat Space.

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`users` Mission Brief

    ^^^
    .. table::
        :widths: 20 60 10

        +--------------+------------------------------------------+--------------+
        | **Audience** | **Prerequisite(s)**                      | **Time**     |
        +--------------+------------------------------------------+--------------+
        | Git Beginner | .. link-button:: http://bit.ly/git-begin | ~ 10 minutes |
        |              |     :classes: btn-success btn-block      |              |
        |              |     :text: git - the simple guide        |              |
        +--------------+------------------------------------------+--------------+

    .. note:: **Using Conda?** Git comes with the Anaconda and Miniconda
            distributions by default. If you are using Conda, the setup step
            can be skipped in the guide.

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`graduation-cap` Learning Objective(s)

    ^^^

    1. Understand the differences between Git and Github.
    2. Installing and configuring Git for use.
    3. Create, clone and manage repositories from Github.
    4. Understand the Tudat Git workflow.


.. note:: **Tired of retyping your Git credentials in the Command-line?**

    .. attention:: This method saves the credentials in plaintext on your PC's
            disk. Everyone on your computer can access it, e.g. malicious NPM
            modules.

    Run

    .. code-block:: bash

        git config --global credential.helper store

    then

    .. code-block:: bash

        git pull

    provide a username and password and those details will then be remembered
    later. The credentials are stored in a file on the disk, with the disk
    permissions of "just user readable/writable" but still in plaintext.

Develop and Master Branches
---------------------------

Instead of a single master branch, this workflow uses two branches to record
the history of the project. The master branch stores the official release
history, and the develop branch serves as an integration branch for features.
It's also convenient to tag all commits in the master branch with a version
number. :cite:p:`atlassian-gitflow`

.. raw:: html
    :file: graphics/gitflow1.svg

Feature Branches
----------------

Each new feature should reside in its own branch, which can be pushed to the
central repository for backup/collaboration. But, instead of branching off of
master, feature branches use develop as their parent branch. When a feature is
complete, it gets merged back into develop. Features should never interact
directly with master. :cite:p:`atlassian-gitflow`

.. raw:: html
    :file: graphics/gitflow2.svg

