Multidoc
========

Multidoc is a tool for purposed towards improving maintainability and
consistency of docstrings in software that is available across multiple
programming languages, with fixed language equivalent APIs.

Nomenclature
------------

    - **Application Programming Interface (API)**: An interface that defines
      interactions between multiple software applications or mixed
      hardware-software intermediaries.

    - **YAML**: (recursive acronym for "YAML Ain't Markup Language") A
      human-readable data-serialization language.

    - **Jinja2**: Jinja is a modern and designer-friendly templating language
      for Python. It is fast, widely used and secure.

API Structure Definition
------------------------

At the core of Multidoc is the API Structure Definition. This directory
contains all the information required to constrain the structure across all
Multidoc supported languages (C++, pybind and Python as of now).

::

    definition/
    ├── __api__.yaml
    ├── module1.yaml
    ├── module2
    │         ├── __module__.yaml
    │         └── submodule1.yaml
    └── module3
        ├── __module__.yaml
        └── submodule2
               └── subsubmodule.yaml

The concepts can be broken down into the following elements:

+--------------------------+-----------------------------------------------------------------------------------------+
| Element                  | Description                                                                             |
+--------------------------+-----------------------------------------------------------------------------------------+
| ``__api__.[yml/yaml]``   | API configuration file. **Must exist** in the API structure prefix.                     |
+--------------------------+-----------------------------------------------------------------------------------------+
| ``module.[yml/yaml]``    | Module configuration file. Module definition as a file implicitly infers no submodules. |
+--------------------------+-----------------------------------------------------------------------------------------+
| ``/module``              | Module configuration directory. **Must contain** ``__module__.[yml/yaml]``              |
+--------------------------+-----------------------------------------------------------------------------------------+
| ``submodule.[yml/yaml]`` | Submodule configuration file. Equivalent to a module configuration file.                |
+--------------------------+-----------------------------------------------------------------------------------------+
