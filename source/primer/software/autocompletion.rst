
Autocompletion in Python
========================

This document describes how autocompletion works for Python modules, and explains
the solution implemented in tudat to provide autocompletions for all Python *and*
C++ modules (exposed through `pybind11`) in `tudatpy`.

Introduction
------------

Autocompletion in Python is performed by a Python Language Server (VSCode uses such
a server, and other IDEs as well), which works by scanning the current scope and
using the active Python interpreter to gather information about installed packages
and modules.

For this to work for a given module it must be inspectable. The `tudat`
kernel, exposed to Python using `pybind11` (`kernel.so`), is not.

.. note::

    This is likely related to an issue with the `def_submodule` function of `pybind11`, 
    due to which exposed modules are not fully inspectable by the Python interpreter (see [1]_).

The solution that hs been implemented in `tudatpy` is to create a Python module 
that wraps each `tudat` kernel module, and explicitly imports all members of the
kernel module. This way, the Python Language Server can inspect the module, and
autocompletion works.

Goal of this guide
------------------

The goal of this guide is to give you immediate insight into how:

1. We implement autocompletion for kernel modules in `tudatpy`
2. How we use the `expose_kernel_module.py`[2]_ script to automate this process
3. How you can use `build_and_expose_kernel,sh`[3]_ to simultaneously build `tudatpy` and expose all kernel modules (to automatically add autocompletion for any new kernel members you may have exposed)

Implementation in tudatpy
-------------------------

Autocompletion in `tudatpy` was implemented in pull request 128[4]_.

To explain how this works, consider a `tudat` kernel module which is exposed through a 
Python module which wraps it. The Python module 

- lives inside `tudatpy`
- has the same name as the kernel module
- and has inside an `__init__.py` with the following statement: `from tudatpy.kernel.<kernel_module_name>import *` -this allows us to import all members of the kernel module from its Python wrapper-.

For each such exposed kernel module, this pull request does the following:

1. Next to the Python module's `__init__.py`, if and only if the module has **non-module** members (so classes, functions and other objects), a new file is created: `_import_all_kernel_members.py`
2. `_import_all_kernel_members.py` explicitly imports all members (classes, functions and other objects) of the kernel module as follows: `from tudatpy.kernel.<module_name> import <member 1>, <member 2>, ...` (see [5]_)
3. In the module's `__init__.py`, we import everything from `_import_all_kernel_members.py` (see [6]_)

This way, all the _explicitly imported_  kernel members are accessible from the Python module 
wrapping it: autocompletion engines will scan this, and detect all module members for autocompletion.

The reason we do this with two files (`__init__.py` and `_import_all_kernel_members.py`) is that this 
way users **can change the** `__init__.py` (which they may well want to do, as it is the `__init__.py` 
of a _hybrid_ C++/_Python_ module), and we can **freely automatically generate** the `_import_all_kernel_members.py` 
**overwriting the existing ones**, as these files will **never be manually changed**.

Basically, this way we allow users to change `__init__.py`, and keep the liberty to blast away old versions 
of all `_import_all_kernel_members.py`s when the kernel changes.

How the process is automated
----------------------------

`expose_kernel_module.py`[2]_ automates this process. We will consider the `numerical_simulation` kernel module to
explain how the script works. Given the name of the kernel module (`numerical_simulation`), `expose_kernel_module.py`[2]_ will:

1. Expose (wrap) every submodule of `numerical_simulation` (create submodule directory and `__init__.py` file)
2. For each submodule, create a `_import_all_kernel_members.py` file, which explicitly imports all **non-module** members of the submodule

Simultaneously compiling `tudatpy`, exposing all kernel modules and enabling autocompletions
--------------------------------------------------------------------------------------------

The `build_and_expose_kernel.sh`[3]_ script automates the process of compiling `tudatpy` and exposing all kernel modules. It does the following:

1. Builds `tudatpy` (by calling the `build.sh`[7]_, providing it with the number of cores to be used for compilation)
2. Defines a list of kernel modules to be exposed (this is necessary as some kernel modules such as `io` and `util` are superseeded/wrapped by the `tudatpy` python modules `io` and `utils`)
3. For each kernel module in the list, it calls `expose_kernel_module.py`[2]_ to expose the kernel module

References
----------

.. [1] `https://github.com/pybind/pybind11/issues/2639`_
.. [2] `https://github.com/tudat-team/tudatpy/blob/master/expose_kernel_module.py`_
.. [3] `https://github.com/tudat-team/tudat-bundle/blob/main/build_and_expose_kernel.sh`_
.. [4] `https://github.com/tudat-team/tudatpy/pull/128`_
.. [5] `https://github.com/tudat-team/tudatpy/blob/master/tudatpy/math/interpolators/_import_all_kernel_members.py`_
.. [6] `https://github.com/tudat-team/tudatpy/blob/master/tudatpy/math/interpolators/__init__.py`_
.. [7] `https://github.com/tudat-team/tudat-bundle/blob/main/build.sh`_