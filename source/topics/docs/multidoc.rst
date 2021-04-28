Multidoc
========

Multidoc is a tool for facilitating improved maintainability and consistency
of docstrings in software that is available across multiple programming
languages.

Nomenclature
------------

    - **Application Programming Interface (API)**: An interface that defines
      interactions between multiple software applications or mixed
      hardware-software intermediaries.

    - **YAML**: (recursive acronym for "YAML Ain't Markup Language") A
      human-readable data-serialization language.

    - **Jinja2**: Jinja is a modern and designer-friendly templating language for
      Python. It is fast, widely used and secure.

API Structure Definition
------------------------

::

    docstrings/
    ├── __api__.yaml
    ├── conversion.yaml
    ├── interface
    │         ├── __module__.yaml
    │         └── spice.yaml
    └── simulation
        ├── __module__.yaml
        └── environment_setup.yaml