API Documentation
=================

Multidoc
---------

**Multidoc** is a tool for purposed towards improving maintainability and
consistency of docstrings in software that is available across multiple
programming languages, with fixed language equivalent APIs.

.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`list` **Nomenclature**

    ^^^

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


.. _numpydoc: https://numpydoc.readthedocs.io/en/latest/format.html

.. code-block:: jinja

    {%- if short_summary -%}
        {{ short_summary }}
    {%- endif -%}


.. code-block:: yaml
   :caption: ``__api__.yaml``
   :name: api-def

    package:
    # name: tudat    # [cpp]
      name: tudatpy  # [py]

    modules:
      - interface
      - simulation
      - conversion

.. warning:: The ``# [py/cpp]`` tag is currently for future use. Documentation
        is currently only generated for ``py``. As a result, leave all ``# [cpp]``
        present where needed, but comment them out, as done above.

.. code-block:: yaml
   :caption: ``module.yaml``
   :name: module-def

    description: |
      Provides interfaces for external API.

    modules:
      - spice

.. code-block:: yaml
   :caption: ``spice.yaml``
   :name: submodule-def

    description: "This module provides an interface to the Spice package."
    notes: "None"

    functions:
      - name: clear_kernels
        short_summary: "Clear all loaded spice kernels."
        extended_summary: |
          This function removes all Spice kernels from the kernel pool.
          Wrapper for the `kclear_c` function.
        returns:
          - type: None   # [py]
        # - type: void   # [cpp]

Functions
---------

https://numpydoc.readthedocs.io/en/latest/format.html#sections


Classes
-------

Use the same sections as outlined above (all except **Returns** are applicable).
The constructor (**__init__**) should also be documented here, the Parameters
section of the docstring details the constructor’s parameters.

Constants
---------

::

    1. summary
    2. extended summary (optional)
    3. see also (optional)
    4. references (optional)
    5. examples (optional)

Modules
-------

::

    1. summary
    2. extended summary
    3. routine listings
    4. see also
    5. notes
    6. references
    7. examples