.. _define-program-environment-variables:

Define Program Environment Variables
====================================

This section guides software developers on how to securely store sensitive information, like access tokens, in environment variables. These practices are crucial for security and are explained for various operating systems, shells, and cloud services, suitable for developers of all skill levels.

Defining Environment Variables in Python
----------------------------------------

In Python, environment variables can be defined using the ``os.environ`` dictionary. To set an environment variable named ``MY_VARIABLE``, use the following code:

.. code-block:: python

   import os
   os.environ["MY_VARIABLE"] = "value"

Alternatively, use the `python-dotenv`_ library for a more secure approach. This library enables you to define environment variables in a ``.env`` file, which can then be loaded into your Python script:

.. code-block:: bash

   # Add this line to your .env file located in ~/
   MY_VARIABLE="value"

Load the environment variables using the ``dotenv`` module:

.. code-block:: python

   from dotenv import load_dotenv
   load_dotenv()

.. _python-dotenv: https://pypi.org/project/python-dotenv/

To access environment variables in Python:

.. code-block:: python

   import os
   my_variable = os.environ.get("MY_VARIABLE")
   if my_variable:
       print("MY_VARIABLE is set to:", my_variable)
   else:
       print("MY_VARIABLE is not set.")

.. admonition:: Note
   The `python-dotenv` library should be used for handling environment variables in production code to prevent sensitive data exposure.

Defining Persistent Environment Variables in Unix
-------------------------------------------------

For Unix systems, define persistent environment variables in your shell profile file. The file's location and name depend on your shell. For example, use ``.bashrc`` for bash or ``.zshrc`` for zsh, both located in your home directory (``~/``).

Example for bash:

.. code-block:: bash

   # Add this to your .bashrc file
   export MY_VARIABLE="value"

.. admonition:: Note
   For zsh, add the `export` statement to ``.zshrc`` instead of ``.bashrc``.

Defining Temporary Environment Variables in Bash Script
-------------------------------------------------------

To define environment variables in a Bash script, use the ``export`` keyword:

.. code-block:: bash

   export MY_VARIABLE="value"
   my_variable=$MY_VARIABLE
   if [ -n "$my_variable" ]; then
       echo "MY_VARIABLE is set to: $my_variable"
   else
       echo "MY_VARIABLE is not set."

Defining Environment Variables in Windows
-----------------------------------------

Use a batch file (``.bat``) to define environment variables in Windows. The `set` command sets the variable:

.. code-block:: batch

   @echo off
   set MY_VARIABLE=value
   if errorlevel 1 (
      echo MY_VARIABLE could not be set
   ) else (
      echo MY_VARIABLE was set successfully
   )

.. admonition:: Warning
   To ensure the variable is available in all sessions, add the batch file to your startup folder (``C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup``).

For persistent variables:

1. Open "Environment Variables" from the Start menu.
2. Click "Edit the system environment variables" > "Environment Variables".
3. Choose "User variables" or "System variables" to add or edit a variable.
4. Enter the variable's name and value, then click "OK".

.. note::
   Restart command prompt windows to apply new environment variables.
