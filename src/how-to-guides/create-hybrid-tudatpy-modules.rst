.. _create-hybrid-tudatpy-modules:

Create Hybrid C++/Python modules in ``tudatpy``
===============================================

This example shows how to create a hybrid C++/Python module in `tudatpy`.

.. note::

    If you're not familiar with the Python import system, it may be useful for you
    to check out the developer documentation on kernel module exposure and autocompletion
    in `tudatpy` first.

The goal of this guide is to briefly explain how to create a hybrid C++/Python module in
`tudatpy`. This is useful to combine C++ and Python functionality in a single `tudatpy`
module.

We will first consider the case in which you have implemented a new class, function or
other object in a C++ `tudat` kernel module, a Python module which uses this object to
provide some functionality, and want to expose them both.

Then, we will consider the case in which you have created an entirely new C++ `tudat` kernel
module, a Python script which makes use of its members to provide some functionality, and
want to expose them both.

Combining C++ and Python functionality in an existing ``tudatpy`` module
------------------------------------------------------------------------

The directory `tudatpy/tudatpy` contains all `tudatpy` modules, both the ones which wrap C++ `tudat` kernel
modules and those which are pure Python.

1. Find the `tudatpy` module which wraps the C++ `tudat` kernel module you want to combine with
   your Python module.
2. Place your Python module inside the `tudatpy` module wrapping the C++ `tudat` kernel module.
   This will allow you to import the Python module and use its members, as well as the members
   of the kernel module.
3. Compile `tudatpy` using `build_and_expose_kernel.sh`_.
   This will expose the C++ `tudat` kernel module by wrapping it in a Python module (as well as provide
   Python autocompletions for all its members).

You're done! You have now combined Python and C++ inside a single `tudatpy` module.

To get a feeling of how the final result should look like, you can check out the `tudatpy.trajectory_design`_
`tudatpy` module, which combines the C++ `shape_based_thrust` and `transfer_trajectory` modules and the Python
`porkchop` module.

.. note::

    You can make use of the `__init__.py`_ of the `tudatpy` module which wraps the C++ `tudat` kernel module
    to ease the import of the Python functionality you've just added to it.

    For example, you could add the following lines to the `__init__.py` of the `tudatpy.trajectory_design` module
    to make it easier to import the `trajectory_design.porkchop.porkchop` function::

        from tudatpy.trajectory_design.porkchop import porkchop

Combining C++ and Python functionality in a new `tudatpy` module
----------------------------------------------------------------

Two components are needed for this:

1. A C++ `tudat` kernel module, exposed to Python using `pybind11`
2. A Python wrapper of the module, which exposes it through `tudatpy`

Create a C++ `tudat` module and expose to Python using `pybind11`
#################################################################

Please refer to the developer docs on exposing C++ modules for a detailed explanation.

Expose the C++ `tudat` kernel module through `tudatpy`
######################################################

Once you have created your C++ kernel module, compile `tudatpy` using `build_and_expose_kernel.sh`_.
This will expose the new C++ `tudat` kernel module by wrapping it in a Python module (as well as provide
Python autocompletions for all its members).

Place your Python module inside the `tudatpy` module wrapping the C++ `tudat` kernel module
###########################################################################################

Move the Python module you want to combine with the kernel module inside the Python module
which wraps the kernel module. This will allow you to import the Python module and use its
members, as well as the members of the kernel module.

To get a feeling of how the final result should look like, you can check out the `tudatpy.trajectory_design`_
`tudatpy` module, which combines the C++ `shape_based_thrust` and `transfer_trajectory` modules and the Python
`porkchop` module.

.. note::

    You can make use of the `__init__.py`_ of the `tudatpy` module which wraps the C++ `tudat` kernel module
    to ease the import of the Python functionality you've just added to it.

    For example, you could add the following lines to the `__init__.py` of the `tudatpy.trajectory_design` module
    to make it easier to import the `trajectory_design.porkchop.porkchop` function::

        from tudatpy.trajectory_design.porkchop import porkchop

References
----------

.. _`tudatpy/tudatpy`: https://github.com/tudat-team/tudatpy/tree/master/tudatpy
.. _`build_and_expose_kernel.sh`: https://github.com/tudat-team/tudat-bundle/blob/main/build_and_expose_kernel.sh
.. _`tudatpy.trajectory_design`: https://github.com/tudat-team/tudatpy/tree/master/tudatpy/trajectory_design
.. _`__init__.py`: https://github.com/tudat-team/tudatpy/blob/master/tudatpy/trajectory_design/__init__.py
