
Developer Environment
=====================

``tudat-bundle``
----------------

.. link-button:: http://bit.ly/tudat-bundle
    :classes: btn-outline-primary btn-block
    :text: Tudat Developer Environment



``tudat-bundle`` is the tudat development environment for ``C++``- and ``python``-based code development.

.. note:: This topic is relevant for:


    - developers who want to expose their updated tudat code to the upcoming ``tudatpy`` package release
    - users who like to extend ``tudatpy`` functionality locally via modification of the ``C++``-based tudat code
    - anybody interested in seeing a concurrent ``C++`` / ``python`` development workflow


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`graduation-cap` Learning Objective(s)

    ^^^

    1. Get your own ``tudat-bundle`` environment from the tudat-team.
    2. Understand the structure of the ``tudat-bundle`` and the purpose of its components.
    3. Familiarize with the mapping between ``tudat`` and ``tudatpy`` source code.
    4. (%!) Understand the higher level functions of the ``tudat-api``.
    5. (%!) Familiarize with the available build configurations for ``tudat`` and ``tudatpy``.
    6. (%!) Know how to build the ``tudat-bundle`` and recognize some common problems that can be encountered.


Getting your tudat-bundle
##########################

The ``tudat-bundle`` environment is available on the `tudat-team  <https://github.com/tudat-team/tudat-bundle/tree/minimal>`_ github repository.
Detailed instructions for the download, setup and verification of your own `tudat-bundle`` can be found in the repository's README.


Introduction to tudat-bundle
#############################

The tudat-bundle consists of three subdirectories:

- ``tudat``, containing the tudat ``C++`` source code
- ``tudatpy``, containing the ``tudatpy/kernel`` directory in which the ``pybind`` exposure of ``C++`` source code to the tudatpy module is facilitated
- ``build``, the build directory containing the compiled ``C++`` tudat code (``builg/tudat``), as well as the compiled tudatpy kernels at ``build/tudatpy/tudatpy/kernel.so``


The entirety of exposed C++ functionality in ``tudatpy`` is contained within the ``tudatpy/kernel`` source directory. For reference during this guide, the architecture of this directory is as follows:

.. code-block:: base

    *  kernel
       *  ├── expose_<module_A>.cpp
       *  ├── expose_<module_A>.h
       *  ├── expose_<module_A>

            *  ├── expose_<submodule_A1>.cpp
            *  ├── expose_<submodule_A1>.h
            *  ├── expose_<submodule_A2>.cpp
            *  ├── expose_<submodule_A2>.cpp
            *  ├──          ...

       *  ├── expose_<module_B>.cpp
       *  ├── expose_<module_B>.h
       *  ├── expose_<module_B>

            *  ├── expose_<submodule_B1>.cpp
            *  ├── expose_<submodule_B1>.h
            *  ├── expose_<submodule_B2>.cpp
            *  ├── expose_<submodule_B2>.cpp
            *  ├──          ...

       *  ├── expose_<module_C>.cpp
       *  ├── expose_<module_C>.h
       *  ├── expose_<module_D>.cpp
       *  ├── expose_<module_D>.h
       *  ├──          ...

       *  └── kernel.cpp


.. note:: The terms Package/Module/Submodule are intended to be hierarchical descriptions,
          used mostly in the context of directory structure. In the Python interpreter,
          everything is treated as a `module` object.




Defining the tudatpy package (via the kernel namespace)
#########################################################

The following folded code shows the core elements of the ``tudatpy`` package via the ``kernel`` namespace.
It would serve the reader to have a glance through before we walk through the elements in detail.


.. literalinclude:: /topics/software/snips_environment/kernel.cpp
        :caption: ``tudatpy/kernel/kernel.cpp``
        :language: cpp


Starting with the end in mind, compiling the previous will create a shared library named ``kernel.so``, making available all modules included in ``kernel.cpp``.
With the ``kernel.so`` library added to the Python path variable, users can then import ``tudatpy` modules by executing for example ``from kernel import simulation``.


.. warning::

    The Python interpreter searches the ``sys.path`` in its order. Inspect
    the ``sys.path`` list to verify that the desired variant of a module is imported.


(%!) includes, module settings, versioning...

All ``tudatpy`` modules included in the ``kernel`` namespace are defined in their respective ``expose_<module_A>.cpp`` (and ``expose_<module_A>.h``) files.
For some modules (e.g. module ``constants``) the ``C++`` / ``python`` class and function interfaces are exposed directly in the module definition.
More extensive modules (e.g. module ``simulation``) are first compiled as modules from their own respective submodules.



Module Definition from Submodules
##################################

The following code shows the complete module definition ``simulation`` from its respective submodules ``environment_setup``, ``estimation_setup``, ``propagation_setup`` and ``shape_based_thrust``.
Note that in this case the ``C++`` / ``python`` class and function interfaces are defined on the respective submodule level.

.. literalinclude:: /topics/software/snips_environment/expose_simulation.cpp
        :caption: ``tudatpy/kernel/expose_simulation.cpp``
        :language: cpp



Class and Function Interfaces in (Sub)Module Definitions
##########################################################

Depending on the extend of the module, the ``C++`` / ``python`` class and function interfaces are managed on the module or submodule level (via the ``expose_<module_A>`` or ``expose_<submodule_Ax>`` functions, respectively).
The rules for the ``pybind`` interface management are the same for both cases and will be explained in more detail under :ref:`Exposing C++ in Python`.


The ``constants`` module definition serves as an example for straightforward exposure on module level. Consider the folded code below:

.. literalinclude:: /topics/software/snips_environment/expose_constants.cpp
        :caption: ``tudatpy/kernel/expose_constants.cpp``
        :language: cpp

By including tudat source code headers, several tudat namespaces related ``constants`` are made available, such that their content can be exposed.
In the case of the ``constants`` module, this content is limited to attributes.
Using the ``pybind`` syntax for attributes, the content is exposed within the ``expose_constants( )`` function.


The class and function interfaces of the ``simulation`` module are managed on the submodule level, for example in the definition of its ``environment_setup`` submodule.
The content which is exposed here is much more extensive and diverse (including classes, functions, etc).
In such cases, it may be convenient to lower-level exposition functions to pre-group the content by its origin header file or tudat namespace.
The folded code below gives as an example the structure of the submodule definition ``environment_setup``.
It shows this pre-grouping for the ``aerodynamic_coefficient_setup`` and ``atmosphere_setup``.
The respective exposition functions ``expose_aerodynamic_coefficient_setup( )`` and ``expose_atmosphere_setup( )`` are then called later from within the submodule exposition function.
The example also shows that some content (i.e. from ``body.h``) may still be exposed directly in the submodule exposition function.


(%!) somehow condense this code by a lot:

.. literalinclude:: /topics/software/snips_environment/expose_environment_setup.cpp
        :caption: ``tudatpy/kernel/expose_environment_setup.cpp``
        :language: cpp






``tudat-api``
----------------
4. (%!) Understand the higher level functions of the ``tudat-api``.


Building ``tudat`` and/or ``tudatpy``
------------------------------------------------
5. (%!) Familiarize with the available build configurations for ``tudat`` and ``tudatpy``.
6. (%!) Know how to build the ``tudat-bundle`` and recognize some common problems that can be encountered.
