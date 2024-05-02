
Developer Environment
=====================

.. _`tudat-bundle`: http://bit.ly/tudat-bundle

The `tudat-bundle`_ build configuration allows developers to simultaneously
work on `tudat` and `tudatpy` for a better flow in your end to end development.

.. note:: This topic is relevant for:


    - developers who want to expose their updated tudat code to the upcoming ``tudatpy`` package release.
    - users who like to extend ``tudatpy`` functionality locally via modification of the C++-based ``tudat`` source code.
    - anybody interested in seeing a concurrent C++ / Python development workflow.


.. admonition:: :fa:`graduation-cap` Learning Objectives
    :class: learning-objectives

    .. include:: objectives/environment.rst


Cloning ``tudat-bundle``
##########################

The ``tudat-bundle`` environment is available on the `tudat-team  <https://github.com/tudat-team/tudat-bundle/tree/minimal>`_ GitHub repository.

.. note:: Detailed instructions for the download, setup and verification of your own ``tudat-bundle`` can be found in the repository's `README  <https://github.com/tudat-team/tudat-bundle/tree/minimal#readme>`_ (steps 1-4).

.. warning:: If your machine is running on an Apple M1 processor, you may have to follow a slightly different procedure. Please refer to this `discussion <https://github.com/tudat-team/tudat-bundle/issues/1>`_.



Introduction to ``tudat-bundle``
#############################

The ``tudat-bundle`` consists of three subdirectories:

- ``tudat``, containing the tudat ``C++`` source code.
- ``tudatpy``, containing the ``tudatpy/kernel`` directory in which the exposure of ``C++`` source code to the tudatpy package is facilitated.
- ``<build>``, the build directory containing the compiled ``C++`` tudat code (``<build>/tudat``), as well as the compiled tudatpy package at ``<build>/tudatpy/tudatpy/kernel.so``.


The entirety of exposed C++ functionality in ``tudatpy`` is contained within the ``tudatpy/kernel`` source directory.

For reference during this guide, the architecture of this directory is as follows:

.. note:: This module / submodule tree structure always aspires to mimic the structure of the ``tudat/src`` directory.


.. _dir-structure:
.. code-block:: base
    :caption: ``schematic tudatpy/kernel directory``

    *  kernel
       *  ├── expose_<module_A>.cpp
       *  ├── expose_<module_A>.h
       *  ├── expose_<module_A>

            *  ├── expose_<submodule_A1>.cpp
            *  ├── expose_<submodule_A1>.h
            *  ├── expose_<submodule_A2>.cpp
            *  ├── expose_<submodule_A2>.h
            *  ├──          ...

       *  ├── expose_<module_B>.cpp
       *  ├── expose_<module_B>.h
       *  ├──          ...

       *  └── kernel.cpp



.. note:: The terms Package/Module/Submodule are intended to be hierarchical descriptions,
          used mostly in the context of directory structure. In the Python interpreter,
          everything is treated as a `module` object.


The ``tudatpy`` Package
########################

The ``tudatpy`` package is a collection of modules, in which the C++-based ``tudat`` source code is exposed into Python bindings.

.. note::  The interfaces of C++-based ``tudat`` source code and the Python-based ``tudatpy`` modules are managed by the `Pybind11 library  <https://pybind11.readthedocs.io/en/stable/>`_. The rules for defining C++ to Python interfaces using Pybind11 will be presented in detail under :ref:`Exposing C++ in Python`.


In ``kernel.cpp`` (see ``schematic tudatpy/kernel directory``) ``tudatpy`` modules are bundled into the ``tudatpy`` package.
The following folded code shows the core elements of ``kernel.cpp``.
It would serve the reader to have a glance through before we walk through the elements in detail.


.. literalinclude:: /primer/software/snips_environment/kernel.cpp
        :caption: ``tudatpy/kernel/kernel.cpp``
        :language: cpp


Starting with the end in mind, compiling the previous will create a shared library named ``kernel.so``, making available all modules included in ``kernel.cpp``.
With the ``kernel.so`` library added to the Python path variable, users can then import ``tudatpy`` modules such as the ``astro`` module, by executing ``from kernel import astro``.


.. warning::

    The Python interpreter searches the ``sys.path`` in its order. Inspect
    the ``sys.path`` list to verify that the desired variant of a module is imported.



All ``tudatpy`` modules included in the ``kernel`` namespace have previously defined in their respective ``expose_<module_A>.cpp`` (and ``expose_<module_A>.h``) files.


Module Definition
###################

.. note:: A ``tudatpy`` module can be thought of as collection of ``tudat`` source code, which has been exposed to ``python``.

Modules are defined by their respective exposition functions ``expose_<module_X>( )``.
These exposition functions fulfill one of two (or sometimes both) tasks:

1. directly expose ``tudat`` source code in the module namespace (see ``<module_B>`` in :ref:`dir-structure`)
2. include selected submodules, where ``tudat`` source code has been exposed in nested namespaces (see ``<module_A>`` in :ref:`dir-structure`)



1. Source Code Exposition in Module Namespace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exposition functions may directly expose ``tudat`` source code content (module classes, functions and attributes) from the respective ``tudat`` namespace to the ``tudatpy`` module namespace.
In this case, the ``C++`` to ``python`` interfaces are defined directly in the ``tudatpy`` module namespace.
One example of this usage is the ``tudatpy`` ``constants`` module.
Consider below the definition of the module ``constants``:

.. literalinclude:: /primer/software/snips_environment/module_definition.cpp
        :caption: ``tudatpy/kernel/expose_constants.cpp``
        :language: cpp

The procedure can be summarized in three easy steps

1. make available ``tudat`` source code and ``pybind11`` functionality
2. define module definition function ``expose_constants( )`` in module namespace
3. define ``C++`` to ``python`` interfaces using the ``pybind`` syntax


.. note:: In the case of the ``constants`` module, the exposed source code content is limited to attributes.



2. Source Code Exposition in Nested Namespace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For large ``tudatpy`` modules, the exposition of the ``tudat`` source code is divided over submodules.
In this case, the ``C++`` to ``python`` interfaces are defined in the submodule namespace or even lower-level nested namespaces.
One example of this usage is the ``tudatpy`` ``astro`` module, which includes exposed ``tudat`` source code from submodules such as ``fundamentals``, ``ephemerides`` and more.
Consider below the definition of the module ``astro``:

.. literalinclude:: /primer/software/snips_environment/module_definition_nested.cpp
        :caption: ``tudatpy/kernel/expose_astro.cpp``
        :language: cpp


The procedure is largely analogous to the that of :ref:`Source Code exposition in module namespace`:

1. make available ``tudat`` source code and ``pybind11`` functionality
2. define module definition function ``expose_astro( )`` in module namespace
3. include selected submodules ``fundamentals`` & ``ephemerides`` via pybind's ``module.add_submodule( )`` function


Since the ``tudatpy`` submodules ``fundamentals`` & ``ephemerides`` define the ``C++`` to ``python`` interfaces, the definition of these submodules follows the exact same structure as in case 1 (Source Code Exposition in Module Namespace).
For the sake of completeness the definition of the ``ephemerides`` submodule is presented below:

.. literalinclude:: /primer/software/snips_environment/submodule_definition.cpp
        :caption: ``tudatpy/kernel/expose_astro.cpp``
        :language: cpp


In principle, it is possible for the ``ephemerides`` submodule to delegate the ``C++`` to ``python`` interfaces to even lower-level namespaces.
In this case, the ``ephemerides`` submodule definition (and any lower levels that delegate the interfaces) would follow the logic of case 2 (Source Code Exposition in Nested Namespace), while at the lowest level of this module / submodule tree the definition would again follow the logic of case 1 (Source Code Exposition in Module Namespace).



The ``tudat(py)`` API in ``tudat-bundle``
------------------------------------------
.. warning:: WIP - show how to use docstrings in ``tudat-bundle`` to contribute to ``tudat(py)``-api


Build Configurations
----------------------
The ``tudat`` source code can be build using various build configurations.
These configurations are listed in ``tudat-bundle/CMakeLists.txt`` (l. 43 ff.).
The user can select the build options by use of the 'ON'/'OFF' keywords.
See below a section of the ``CMakeLists`` file, which gives an example for an enabled test-suite build option and a disabled boost build option:

.. literalinclude:: /primer/software/snips_environment/CMakeListsFolded.txt
        :caption: ``tudat-bundle/CMakeLists.txt``
        :language: cpp


.. warning:: Options that toggle the use of ``SOFA`` amd ``SPICE`` can break the build of ``tudatpy``.

.. note:: For more information on the workings of ``CMake`` as a build system, please refer to :ref:`Build System`.





Building the Project and Known Issues
--------------------------------------

For most users the project build is very easy and described in the `README  <https://github.com/tudat-team/tudat-bundle/tree/minimal#readme>`_ (steps 5 ff.)

.. warning:: If your machine is running on an Apple M1 processor, you may have to follow a slightly different. Please refer to this `discussion <https://github.com/tudat-team/tudat-bundle/issues/1>`_. You may also encounter issues with tudat-test, which can be resolved as described `here <https://github.com/tudat-team/tudat-bundle/issues/2>`_.
