
Exposing Kernel Modules in ``tudatpy``
================================================

The goal of this document is to concisely explain

1. Why we must come up with a solution to expose kernel modules directly through tudatpy
2. How the solution works
3. How the solution is automated with the `expose_kernel_module.py`[1]_ script
4. How you can simultaneously compile `tudatpy` and expose all kernel modules directly through `tudatpy`

.. note::

    With "kernel exposure directly through `tudatpy`" we mean making it possible
    to import kernel modules as follows::

        from tudatpy.numerical_simulation import environment

    instead of::

        from tudatpy.kernel.numerical_simulation import environment

Why we must come up with a solution to expose kernel modules directly through tudatpy
-------------------------------------------------------------------------------------

The reason a manual solution is needed is an issue with the `def_submodule` function of
`pybind11`, due to which exposed modules are not fully inspectable by the Python interpreter
(see [2]_).

Previously, the `tudat` C++ kernel was exposed in `tudatpy` in the `tudatpy/__init__.py` as follows::

    from tudatpy.kernel import *

Due to the bug with the `def_submodule` function of `pybind11`, the Python interpreter **cannot inspect**
the kernel modules imported with the start import, and thus imports such as the following **will fail**::

    from tudatpy.numerical_simulation import environment

The solution
------------

We will use the module `tudatpy.kernel.astro` to illustrate how kernel modules are exposed:

1. A top-level `tudatpy` Python module, `tudatpy.astro`, is created to wrap `tudatpy.kernel.astro`. This top-level module consists of an empty directory with a an (empty) `__init__.py` inside
2. In the `__init__.py` we **import** the kernel module `tudatpy.kernel.astro` as follows::

        `from tudatpy.kernel.astro import *`.

      This makes it possible to import the kernel module in Python like this: `import tudatpy.astro`
3. We add a [disclaimer](https://github.com/tudat-team/tudatpy/blob/60719404b37c8cfb747e9d4cd7ef6f865b148acf/tudatpy/trajectory_design/__init__.py#L1), clearly stating that the import statement has been automatically generated, and why.
4. This process repeats for all submodules of `tudatpy.kernel.astro`

Hybrid Python/C++ modules
#########################

It is possible to combine Python and C++ functionality inside the `tudatpy` modules which wrap `tudat` C++ kernel modules.
Check the developer guide on hybrid modules for more details.

The consequence is that the `__init__.py` of `tudatpy.astro` in our example may be edited later on to facilitate
the import of Python functions and classes which are not part of the `tudat` C++ kernel module `astro`.

To avoid overwriting/deleting meaningful content inside the `__init__.py` file, kernel modules are exposed as follows. We will
consider the `tudatpy.trajectory_design` module as an example, which exposes the `tudat` C++ `trajectory_design` module
as well as Python code:

1. The entire `tudatpy/trajectory_design` Python module is copied to the **compiled tudatpy directory** `tudatpy/trajectory_design`
2. After this is done, we check if `tudatpy/trajectory_design` **already contains** a top-level `__init__.py`
    - **If it does**, we check if the `__init__.py` **already contains** the kernel module import statement:
        - **If it does**, we do nothing
        - **Else**, we **append** the import statement and disclaimer to the `__init__.py`
    - Else, an `__init__.py` is created inside `tudatpy/trajectory_design` with the kernel module import statement and disclaimer

How the process is automated
----------------------------

`expose_kernel_module.py`[1]_ automates this process. We will consider the `numerical_simulation` kernel module to
explain how the script works. Given the name of the kernel module (`numerical_simulation`), `expose_kernel_module.py`[2]_ will:

1. Expose (wrap) every submodule of `numerical_simulation` (create submodule directory and `__init__.py` file)
2. For each submodule, create a `_import_all_kernel_members.py` file, which explicitly imports all **non-module** members of the submodule

.. note::

    `expose_kernel_module`[1]_ also enables autocompletions for all kernel variables (classes, functions, other objects).
    Check the developer docs on autocompletion to see how this is done.

Simultaneously compiling `tudatpy` and exposing all kernel modules (as well as enabling autocompletions)
--------------------------------------------------------------------------------------------------------

The `build_and_expose_kernel.sh`[3]_ script automates the process of compiling `tudatpy` and exposing all kernel modules. It does the following:

1. Builds `tudatpy` (by calling the `build.sh`[7]_, providing it with the number of cores to be used for compilation)
2. Defines a list of kernel modules to be exposed (this is necessary as some kernel modules such as `io` and `util` are superseeded/wrapped by the `tudatpy` python modules `io` and `utils`)
3. For each kernel module in the list, it calls `expose_kernel_module.py`[2]_ to expose the kernel module

References
----------

.. [1] `<https://github.com/tudat-team/tudatpy/blob/master/expose_kernel_module.py>`_
.. [2] `<https://github.com/pybind/pybind11/issues/2639>`_