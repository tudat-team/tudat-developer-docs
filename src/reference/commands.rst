
Commands
========

+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``conda smithy rerender --feedstock_directory ./foo-feedstock`` | Rerendering is conda-forge’s way to update the files common to all feedstocks (e.g. README, CI configuration, pinned dependencies). |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
|                                                                 |                                                                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

:download:`Git Cheat Sheet </assets/files/git-cheatsheet.pdf>`

:download:`Conda Cheat Sheet </assets/files/git-cheatsheet.pdf>`

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

.. note::

    You can now check the state of the working tree and the staging area on
    on your local branch. The working tree, or working directory, consists of
    files that you are currently working on. You can think of a working tree
    as a file system where you can view and modify files. The index, or staging
    area, is where commits are prepared.


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

.. attention:: INCREDIBLE Bash scripting cheatsheet

    https://devhints.io/bash

- Visual Git: https://marklodato.github.io/visual-git-guide/index-en.html