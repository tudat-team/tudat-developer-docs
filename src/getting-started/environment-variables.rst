.. _Getting Started with Environment Variables:

Environment Variables
=====================

Environment variables are essential in managing software configuration,
enhancing security and flexibility. This guide covers the basics for developers
of all levels.

Understanding Environment Variables
------------------------------------

:term:`Environment Variables` are dynamic values influencing running processes.
They include :term:`Persistent Environment Variables` and
:term:`Temporary Environment Variables`, used for managing system settings and
user preferences.

Why Use Environment Variables?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Security:** Safeguard sensitive data.
- **Portability:** Facilitate configuration changes.
- **Separation of Concerns:** Detach code from configuration.

Examples of Environment Variables
---------------------------------

.. tab-set::

    .. tab-item:: Python
        :sync: python

        **Setting Environment Variables in a Python Script:**

        Directly setting a variable:

        .. code-block:: python

           import os
           os.environ["MY_VARIABLE"] = "value"
           print(f'MY_VARIABLE: {os.environ["MY_VARIABLE"]}')

        Using ``python-dotenv`` for enhanced security:

        .. code-block:: python

           # .env file should contain: MY_VARIABLE="value"
           from dotenv import load_dotenv
           load_dotenv()
           print(f'MY_VARIABLE: {os.getenv("MY_VARIABLE")}')

    .. tab-item:: Unix
        :sync: unix

        **Persistent Environment Variables in Unix (`.bashrc` or `.zshrc`):**

        Add the following line to the respective shell profile:

        .. code-block:: bash

           echo 'export MY_VARIABLE="value"' >> ~/.bashrc  # For Bash
           echo 'export MY_VARIABLE="value"' >> ~/.zshrc   # For Zsh

    .. tab-item:: Windows
        :sync: windows

        **Setting Environment Variables in a Windows Batch File:**

        Create a batch file with:

        .. code-block:: batch

           @echo off
           set MY_VARIABLE=value
           echo %MY_VARIABLE%

        **Setting Persistent Environment Variables in Windows:**

        1. Open "Environment Variables" from the Start menu.
        2. Choose "Edit the system environment variables".
        3. Click on "Environment Variables".
        4. Under "User variables", click "New" or select an existing variable to edit.

    .. tab-item:: Azure Pipelines
        :sync: azure

        **Setting Environment Variables in Azure Pipelines:**

        To set an environment variable in Azure Pipelines:

        1. Navigate to your pipeline in Azure DevOps.
        2. Click "Edit" on your selected pipeline.
        3. Go to "Variables" and either update an existing variable or add a new one.
        4. Save the changes to apply the environment variable.

        .. image:: /assets/screenshots/azure_pipeline_7.png


Conclusion
----------

Environment variables play a crucial role in modern software development,
offering security and adaptability. This guide provides a foundational overview
for various platforms.

For more advanced topics, see the respective sections on Python, Unix, Windows,
and Azure documentation.


