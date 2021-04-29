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
   :name: api-def

    description: |
      Provides interfaces for external API.

    modules:
      - spice

.. code-block:: yaml
   :caption: ``spice.yaml``
   :name: api-def

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

.. note:: The following list is for overview. For a more detailed description
      of each section, with examples, please go to `numpydoc`_.

.. dropdown:: 1. Short summary: **A one-line summary that does not use variable names or
               the function name.**
    :title: text-info font-weight-bold

.. dropdown:: 2. Deprecation warning: **A section (use if applicable) to warn users that
               the object is deprecated.**
    :title: text-info font-weight-bold

.. dropdown:: 3. Extended Summary: **A few sentences giving an extended description.**
    :title: text-info font-weight-bold

    This section should be used to clarify functionality, not to discuss
    implementation detail or background theory, which should rather
    be explored in the Notes section below.

.. dropdown:: 4. Parameters: **Description of the function arguments, keywords and their respective types.**
    :title: text-info font-weight-bold

.. dropdown:: 5. **Returns**: Explanation of the returned values and their types.
    :title: text-info font-weight-bold

    Similar to the Parameters section, except the name of each return value is optional.

.. dropdown:: 6. **Yields**: Explanation of the yielded values and their types. This is relevant to generators only.
    :title: text-info font-weight-bold

    Similar to the Returns section in that the name of each value is optional,
    but the type of each value is always required.

.. dropdown:: 7. **Receives**: Explanation of parameters passed to a generator’s ``.send()`` method, formatted as for Parameters, above.
    :title: text-info font-weight-bold

.. dropdown:: 8. **Other Parameters**: An optional section used to describe infrequently used parameters.
    :title: text-info font-weight-bold

     It should only be used if a function has a large number of
     keyword parameters, to prevent cluttering the Parameters section.

8. **Other Parameters**: An optional section used to describe infrequently used
   parameters. It should only be used if a function has a large number of
   keyword parameters, to prevent cluttering the Parameters section.

9. **Raises**: An optional section detailing which errors get raised and under
   what conditions.

10. **Warns**: An optional section detailing which warnings get raised and
    under what conditions, formatted similarly to Raises.

11. **Warnings**: An optional section with cautions to the user in free
    text/reST.

12. **See Also**: An optional section used to refer to related code. This
    section can be very useful, but should be used judiciously. The goal is to
    direct users to other functions they may not be aware of, or have easy
    means of discovering (by looking at the module docstring, for example).
    Routines whose docstrings further explain parameters used by this function
    are good candidates.

13. **Notes**: An optional section that provides additional information about
    the code, possibly including a discussion of the algorithm. This section
    may include mathematical equations, written in LaTeX format.

14. **References**: References cited in the Notes section may be listed here.

15. **Examples**: An optional section for examples, using the doctest format.
    This section is meant to illustrate usage, not to provide a testing
    framework – for that, use the ``tests/`` directory. While optional, this
    section is very strongly encouraged.

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