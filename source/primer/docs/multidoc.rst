Multidoc
=================

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