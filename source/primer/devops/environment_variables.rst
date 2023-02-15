Environment Variables
=====================

Definition and Importance
--------------------------

Environment variables are values that can be passed to the operating system or an application, which can then be used as configuration information. They are commonly used to store sensitive information, such as access tokens, so that they can be easily retrieved and used within code. By using environment variables, you can keep sensitive information separate from your code and store it securely.

Setting Environment Variables Locally in Different Operating Systems
---------------------------------------------------------------

Setting environment variables locally in Unix-based systems:

In Unix-based systems, you can set environment variables for the current session in your terminal by using the following syntax:

::

    export VAR_NAME=value

For example, to set an environment variable for your access token, you can run the following command:

::

    export ACCESS_TOKEN=your_access_token_value

Setting environment variables locally in Windows:

In Windows, you can set environment variables for the current session in the command prompt by using the following syntax:

::

    set VAR_NAME=value

For example, to set an environment variable for your access token, you can run the following command:

::

    set ACCESS_TOKEN=your_access_token_value

Setting Environment Variables Persistently in Different Operating Systems
---------------------------------------------------------------

Setting environment variables persistently in Unix-based systems:

To set environment variables persistently in Unix-based systems, you need to add the environment variable definitions to your shell profile file, such as .bashrc or .bash_profile.

For example, to set an environment variable for your access token persistently, you can add the following line to your shell profile file:

::

    export ACCESS_TOKEN=your_access_token_value

Setting environment variables persistently in Windows:

To set environment variables persistently in Windows, you can use the `setx` command in the command prompt. The `setx` command allows you to set environment variables that will persist even after you restart your computer.

For example, to set an environment variable for your access token persistently, you can run the following command:

::

    setx ACCESS_TOKEN your_access_token_value

Code Snippet for Defining Environment Variables in Python
---------------------------------------------------------------

In Python, you can access environment variables using the `os` module. You can retrieve the value of an environment variable using the `getenv` method.

For example, to retrieve the value of an environment variable for your access token, you can use the following code:

::

    import os
    access_token = os.getenv("ACCESS_TOKEN")

FAQ's
-----

Q: How do I view my environment variables?
A: To view your environment variables, you can use the `echo` command in your terminal or run the `set` command in a command prompt (Windows) or `env` command in a terminal (Unix-based systems).

Q: How do I delete an environment variable?
A: To delete an environment variable, you can use the `unset` command in a terminal (Unix-based systems) or `setx` command in a command prompt (Windows) followed by the name of the variable.

For more information and a more in-depth guide on defining environment variables, please see the :ref:`Defining Environment Variables` guide.
