
Code Collaboration
==================

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`graduation-cap` Learning Objective(s)

    ^^^

    1. Understand the differences between Git and Github.
    2. Installing and configuring Git for use.
    3. Create, clone and manage repositories from Github.
    4. Understand the Tudat Git workflow.


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

