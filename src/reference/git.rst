Git Commands
============

.. note:: This reference guide is meant to provide quick insights into commonly used Git commands. For a more detailed explanation, consider referring to the official `Git documentation <https://git-scm.com/doc>`_.

Basic Commands
--------------
.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Description
     - Command
   * - Initialize a Repository
     - .. code-block:: bash

           git init
   * - Clone a Repository
     - .. code-block:: bash

           git clone <repository_url>
   * - Check Status
     - .. code-block:: bash

           git status

.. tip:: Use ``git status`` often to see the state of your local repository.

Branching and Merging
---------------------
.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Description
     - Command
   * - Create a New Branch
     - .. code-block:: bash

           git checkout -b <branch_name>
   * - Switch to an Existing Branch
     - .. code-block:: bash

           git checkout <branch_name>
   * - Merge Branch
     - .. code-block:: bash

           git merge <branch_name>
   * - Delete a Local Branch
     - .. code-block:: bash

           git branch -d <branch_name>
   * - Delete a Remote Branch
     - .. code-block:: bash

           git push --delete <remote_name> <branch_name>

.. warning:: Deleting a branch removes all of its associated commits that are **not** merged into another branch. Always double-check before deleting a branch.

Staging and Committing
----------------------
.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Description
     - Command
   * - Stage Files
     - .. code-block:: bash

           git add <file_name>
           git add .
   * - Commit Changes
     - .. code-block:: bash

           git commit -m "<commit_message>"
   * - Amend Previous Commit
     - .. code-block:: bash

           git commit --amend

.. note:: Using ``git commit --amend`` replaces the last commit with a new one. This can be dangerous if you've already pushed commits to a shared repository.

Remote Repositories
-------------------
.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Description
     - Command
   * - Add Remote
     - .. code-block:: bash

           git remote add <remote_name> <remote_url>
   * - Fetch Changes
     - .. code-block:: bash

           git fetch <remote_name>
   * - Pull Changes
     - .. code-block:: bash

           git pull <remote_name> <branch_name>
   * - Push Changes
     - .. code-block:: bash

           git push <remote_name> <branch_name>

.. tip:: ``git pull`` is essentially a ``git fetch`` followed by a ``git merge``. If you want to review changes before merging, use ``git fetch`` and then ``git merge``.

History and Logs
----------------
.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Description
     - Command
   * - View Log
     - .. code-block:: bash

           git log
   * - View Specific File History
     - .. code-block:: bash

           git log -p <file_name>
   * - Undo Last Commit
     - .. code-block:: bash

           git revert HEAD

.. note:: ``git revert`` creates a new commit that undoes the changes from a previous commit. This is different from ``git reset``, which discards commits.

Utility Commands
----------------
.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Description
     - Command
   * - Stash Changes
     - .. code-block:: bash

           git stash
   * - Apply Stashed Changes
     - .. code-block:: bash

           git stash apply
   * - Clean Untracked Files
     - .. code-block:: bash

           git clean -fd
   * - Reset to a Specific Commit
     - .. code-block:: bash

           git reset <commit_hash>

.. warning:: Be cautious when using ``git clean`` and ``git reset`` as these commands permanently delete your work.

