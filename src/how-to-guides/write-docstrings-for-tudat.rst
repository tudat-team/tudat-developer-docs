************************************************
Write docstrings for ``tudat`` and ``tudatpy``
************************************************

In this guide, we will explain how to write docstrings for tudat and tudatpy.
We will also include a template for documenting enums, classes and (factory) functions.

.. note:: Before diving into this guide, the user should be familiar with the page about :ref:`Exposing C++ to Python`.

YAML files
*************

The source of docstrings are located in yaml files in the `docstring <https://github
.com/tudat-team/tudat-multidoc/tree/main/docstrings>`_ directory on Github.
The content is divided over a file tree structure that mimics the structure of the tudatpy exposure (see this
`directory <https://github.com/tudat-team/tudatpy/tree/master/tudatpy/kernel>`_ on Github),
which is the same structure of the tudatpy modules.
Each file bundles the content of a module exposure function (i.e. Ephemeris, Gravity Field, Rotation, etc). Within each
yaml file, all module classes are listed under a single "classes" key, while functions are listed under a single "functions" key.

.. note:: For tudatpy-native classes and functions (i.e., not exposed from C++ code but directly coded in Python), the docstrings can be
   written directly in the Python source files. Only the name of the class and method needs to be included in the yaml file. An example of this can be found
   `here <https://github.com/tudat-team/tudatpy/blob/9a341fcb4202b2c5be2e5abe7e2119fae99da79a/tudatpy/plotting
   /_ground_track.py#L14-L42>`_ for the docstring and `here <https://github.com/tudat-team/tudat-multidoc/blob/0f6e77e5469ea4556a65d98796e1d28f143998d8/docstrings/plotting.yaml#L8>`_ for the mention in the yaml file.


API Structure Definition
------------------------

The generic structure definition of a Python API reference system is provided below:

.. code-block::

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

The building blocks can be broken down into the following elements:

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

``yaml`` files
---------------

`YAML <https://yaml.org>`_ files contain the sources of the docstrings and are organized as key-value pairs.
An example of a typical YAML file is provided below.

.. warning:: The example taken from this docstring `file <https://github.com/tudat-team/tudat-multidoc/blob/main/docstrings/numerical_simulation/propagation_setup/integrator.yaml>`_
   but it was heavily adapted to make it shorter, so it does not contain meaningful information.

.. toggle-header::
    :header: **Show/Hide example**

    .. code-block:: yaml

       extended_summary: |
          This module provides the functionality for creating integrator settings.

       enums:
          - name: AvailableIntegrators
            short_summary: "Enumeration of available integrators."
            extended_summary: |
              Enumeration of integrators supported by tudat.
            members:
              - name: euler # [cpp]
              - name: rungeKutta4 # [cpp]
              - name: euler_type # [py]
              - name: runge_kutta_4_type # [py]

        classes:
          - name: IntegratorSettings
            short_summary: "Functional base class to define settings for integrators."
            extended_summary: |
              Class to define settings for numerical integrators, for instance for use in numerical integration of equations of motion/
              variational equations. This class can be used for simple integrators such as fixed step RK and Euler. Integrators that
              require more settings to define have their own derived class.
            methods:
              - name: ctor # [cpp]
                short_summary: "Constructor." # [cpp]
                extended_summary: "Instances of this class are typically not generated by the user because this is a base class." # [cpp]

            attributes:
              - name: initial_time # [py]
                type: float # [py]
                description: Initial time of the integration. # [py]

        functions:
          # Euler
          - name: eulerSettings # [cpp]
          - name: euler # [py]
            short_summary: "Creates the settings for the Euler integrator."
            extended_summary: |
              Factory function to create settings for the Euler integrator. For this integrator, the step size is kept
              constant.
            parameters:
              - name: initialTime # [cpp]
                type: double # [cpp]
              - name: initial_time # [py]
                type: float # [py]
                description: Start time (independent variable) of numerical integration.

              - name: initialTimeStep # [cpp]
                type: double # [cpp]
              - name: initial_time_step # [py]
                type: float # [py]
                description: Initial and constant value for the time step.

            returns:
                type: IntegratorSettings
                description: Integrator settings object.


As the example shows, the following keys are accepted:

- ``extended_summary`` (for the module)
- ``enums``
- ``classes``
- ``functions``

Each of those sections (except for ``extended_summary``) accepts a number of items. Each item should start with:

.. code-block:: python

    - name: "..."

where the dots are replaced by the name of the enum, class, or function.

.. note::
   - Keys and values entries in YAML files require a leading dash *only if* they are part of a list.
   - A string can be provided in YAML files through quotation marks or with the ``|`` linebreak symbol.

Each item also has different fields. We adopted the `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`_
documentation style. As a result, in our API reference each function or class can accept all the fields specified by
numpydoc (see `here <https://numpydoc.readthedocs.io/en/latest/format.html#sections>`_ for an extensive list).

.. warning:: For enums, as they are not Python native objects, an additional ``members`` field is made available.

tudat vs. tudatpy
------------------------------------------

Tudat and tudatpy API documentations are generated from the same yaml files.

Tudat-exclusive content is marked by the ``# [cpp]`` tag, while tudatpy-exclusive content is marked by ``# [py]``.

.. note:: Untagged content will be included in both API documentations.

Typically, the two APIs convey the same content. That means that the same functions, parameters and returns (etc) are
listed in both APIs, where names and types are adopted to the respective API (`[cpp]` or `[py]`).
Most class or function summaries are the same (word-by-word) for the two APIs.

Documentation style
***********************

The text in the docstring will be parsed and rendered by Sphinx. Therefore, any sphinx command can be used in the
yaml files.

.. warning:: There should be a balance between the readability of the raw docstrings and the intended aesthetical
    effects provided by Sphinx. Even if most of the users will consult the online API reference, the same docstrings
    will be also shipped with the ``tudatpy`` conda package, so the docstrings can be consulted locally. Docstrings
    with many Sphinx commands will be difficult to read and interpret.

Below, a few important aspects of the documentation style are outlined.

Factory functions
------------------------------------------

.. seealso:: All examples from this subsection have been inspired from (but do not correspond exactly to) `this file
   <https://github.com/tudat-team/tudat-multidoc/blob/main/docstrings/numerical_simulation/environment_setup/gravity_field.yaml>`_.

Factory functions (FFs) are functions creating instances of objects via the class constructors ) and they are intended
to be the user's interface with the actual class constructors, such that the users typically do not interact with the
classes as such. FFs will be used throughout all user guides, examples and tutorials. They will be the user`s
landing pad in the API. It is therefore the intention to supply all functionality-related information in the
docstrings of the FF. This may include (but is not limited to) complete explanations for function parameters,
information about the models (that will be created by the classes), model implementation and links to external
resources.

.. toggle-header::
    :header: **Example**

    .. code-block:: yaml

        functions:
            # Factory function instantiating an object of type CentralGravityFieldSettings (see next example)
          - name: central # [py]
          - name: centralGravitySettings # [cpp]
            short_summary: "Factory function for central gravity field settings object."
            extended_summary: |
              Factory function for settings object, defining a point-mass gravity field model with user-defined gravitational parameter.
            parameters:
              - name: gravitational_parameter # [py]
                type: float # [py]
              - name: gravitationalParameter # [cpp]
                type: double # [cpp]
                description: Gravitational parameter defining the point-mass gravity field.
            returns:
                type: CentralGravityFieldSettings
                description: Instance of the :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.GravityFieldSettings` derived :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.CentralGravityFieldSettings` class


(derived) classes
------------------------------------------

Classes, on the other hand, are documented in a more minimalistic manner, focused more on code design and hierarchy
and less on the functional aspects. Constructors of classes that have FFs implemented will not be documented with
``parameters`` and ``returns`` keys, since users are discouraged from directly using the constructor method.
``short_description`` of the constructor method will be given by the string ``"Constructor"``.
``extended_description`` of the constructor method will refer the user to use the respective FF for creating
instances of the given class.


.. toggle-header::
    :header: **Example**

    .. code-block:: yaml

        classes:
          # Derived class from GravityFieldSettings (see next example)
          - name: CentralGravityFieldSettings
            short_summary: "`GravityFieldSettings` derived class defining settings of point mass gravity field."
            extended_summary: |
              Derived class of `GravityFieldSettings` for central gravity fields, which are defined by a single gravitational parameter.

            methods: # [cpp]
                # Class constructor
              - name: ctor # [cpp]
                short_summary: "Constructor." # [cpp]
                extended_summary: "Instances of the `CentralGravityFieldSettings` class should be created through the `centralGravitySettings` factory function." # [cpp]
                # Class constructor's parameter
              - name: getGravitationalParameter # [cpp]
                short_summary: "Retrieve gravitational parameter." # [cpp]
                extended_summary: "Function to retrieve gravitational parameter of the settings object." # [cpp]
                parameters: # [cpp]
                  - name: None # [cpp]
                returns: # [cpp]
                    type: double # [cpp]
                    description: Gravitational parameter of central gravity field. # [cpp]


Base classes
------------------------------------------

Base classes are to be identified as such (in ``short_description``). Typically, users do not create instances of the
base classes (but of the derived classes through the dedicated FFs) and this shall also be mentioned in the
in the ``extended_description``.

.. toggle-header::
    :header: **Example**

    .. code-block:: yaml

        classes:
            # Base class
          - name: GravityFieldSettings
            short_summary: "Base class for providing settings for automatic gravity field model creation."
            extended_summary: |
              This class is a functional base class for settings of gravity field models that require no information in addition to their type.
              Gravity field model classes requiring additional information must be created using an object derived from this class.

            properties: # [py]
              - name: gravity_field_type # [py]
                type: GravityFieldType # [py]
                description: Type of gravity field model that is to be created. # [py]
                readonly: True # [py]

            methods:
              - name: __init__ # [py]
              - name: ctor # [cpp]
                short_summary: "Constructor." # [cpp]
                extended_summary: "Instances of this class are typically not generated by the user. Settings objects for gravity field models should be instantiated through the factory functions of a derived class." # [cpp]


Python properties vs. C++ getters/setters
------------------------------------------

An exception to the analogous structure of the two APIs is the treatment of class attributes.

The original get/set methods of the tudat classes are exposed as "properties" in
tudatpy classes (see our guide about :ref:`Class attributes in C++ vs. in Python`).

As a result, class attributes are only documented as such for the tudatpy API, while the get/set
methods of the classes are documented in the tudat API instead.

.. toggle-header::
    :header: **Example**

    .. code-block:: yaml

        classes:
            # Derived class
          - name: CentralGravityFieldSettings
            short_summary: "`GravityFieldSettings` derived class defining settings of point mass gravity field."
            extended_summary: |
              Derived class of `GravityFieldSettings` for central gravity fields, which are defined by a single gravitational parameter.

            # Properties (only for Python)
            properties: # [py]
              - name: gravitational_parameter # [py]
                type: float # [py]
                description: Gravitational parameter of central gravity field. # [py]

            methods: # [cpp]
              - name: ctor # [cpp]
                short_summary: "Constructor." # [cpp]
                extended_summary: "Instances of the `CentralGravityFieldSettings` class should be created through the `centralGravitySettings` factory function." # [cpp]

                # Getter (only for C++)
              - name: getGravitationalParameter # [cpp]
                short_summary: "Retrieve gravitational parameter." # [cpp]
                extended_summary: "Function to retrieve gravitational parameter of the settings object." # [cpp]
                parameters: # [cpp]
                  - name: None # [cpp]
                returns: # [cpp]
                    type: double # [cpp]
                    description: Gravitational parameter of central gravity field. # [cpp]

                # Setter (only for C++)
              - name: resetGravitationalParameter # [cpp]
                short_summary: "Reset gravitational parameter." # [cpp]
                extended_summary: "Function to reset gravitational parameter of the settings object." # [cpp]
                parameters: # [cpp]
                  - name: gravitationalParameter # [cpp]
                    type: double # [cpp]
                    description: Gravitational parameter of central gravity field that is to be defined by the settings object. # [cpp]

Links within API elements
----------------------------

It is possible to include in a docstring a link to another API element via `intersphinx <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`_.

This can be done with the following syntax:

.. code-block::

    :ObjectName:`~path.to.object`

where ``ObjectName`` can be one of the following:

- ``class``
- ``func``

.. toggle-header::
    :header: **Class example**

    .. code-block::

        :class:`~tudatpy.numerical_simulation.environment_setup.gravity_field.GravityFieldSettings`

.. toggle-header::
    :header: **Function example**

    .. code-block::

        :func:`~tudatpy.numerical_simulation.environment_setup.get_default_body_settings`

.. note:: While this is demonstrated here for links to tudatpy methods, a link to any of python, sphinx, pagmo, numpy, scipy, or matplotlib methods is (in theory) also feasible.

.. todo:: Unfortunately, although other object types (such as properties or modules) should work with the same syntax
    (e.g., see sphinx `resource <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#cross-referencing-python-objects>`_),
    it is currently not working on our API system (see this `open issue <https://github.com/tudat-team/tudat-space/issues/27#>`_).


Link docstrings to source code
***********************************

The docstrings need to be linked in the code such that, during the API build, a connection from docstrings to the code can be made.
This is different between tudat and tudatpy.

tudat
------

This is done by placing tags right above the class/function declaration in the header files of the cpp source code
(`here <https://github.com/tudat-team/tudat/tree/master/include/tudat>`_  on Github) as follows:

Classes
.......

.. code-block:: cpp

   //! @get_docstring(<ClassName>.__docstring__)

.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

         //! @get_docstring(ThrustAccelerationSettings.__docstring__)
         class ThrustAccelerationSettings: public AccelerationSettings{
         ...
         }

Functions
.........

.. code-block:: cpp

   //! @get_docstring(<function_name>)

.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

         //! @get_docstring(customAccelerationSettings)
         inline std::shared_ptr< AccelerationSettings > customAccelerationSettings(
                 const std::function< Eigen::Vector3d( const double ) > accelerationFunction,
                 const std::function< double( const double ) > scalingFunction = nullptr ){
         ...
         }

Overloads
..........

For overload nr. X (X=0,1,...) of a function:

.. code-block:: cpp

  //! @get_docstring(<function_name>, X)

.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

         //! @get_docstring(thrustAcceleration, 0)
         inline std::shared_ptr< AccelerationSettings > thrustAcceleration( const std::shared_ptr< ThrustDirectionSettings >
                 thrustDirectionGuidanceSettings,
                const std::shared_ptr< ThrustMagnitudeSettings > thrustMagnitudeSettings ){
         ...
         }

.. note:: All other tags present in .cpp/.h files, used to connect the source code to the Doxygen documentation engine,
   should be removed, otherwise they will be automatically included in the API.

tudatpy
--------

In order to make the link to the exposed tudatpy classes and functions, the docstrings need to be exposed as well. This
can be done as follows.

Classes
.......

.. code-block:: cpp

   get_docstring("<ClassName>").c_str()

as last argument of ``py:class_<>()``, as in

.. code-block:: cpp

   py:class_<CppClass, CppPointerToClass, CppParentClass>(module, "ClassName", get_docstring("<ClassName>").c_str())


.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

        py::class_<tss::ThrustAccelerationSettings,
                std::shared_ptr<tss::ThrustAccelerationSettings>,
                tss::AccelerationSettings>(m, "ThrustAccelerationSettings",
                                           get_docstring("ThrustAccelerationSettings").c_str())

Class methods
...............

.. code-block:: cpp

   get_docstring("<ClassName.MethodName>").c_str()

as last argument of ``.def()``, as in

.. code-block:: cpp

    .def("MethodName", CppClassName::CppMethodName, py::arg("ParameterName"), ..., get_docstring("<ClassName.MethodName>").c_str())

.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

          .def("integrate_equations_of_motion",
               &tp::SingleArcDynamicsSimulator<double, double>::integrateEquationsOfMotion,
               py::arg("initial_states"),
               get_docstring("SingleArcSimulator.integrate_equations_of_motion").c_str())

Class properties
.................

.. code-block:: cpp

   get_docstring("<ClassName.MethodName>").c_str()

as last argument of `.def_property()` (or `.def_property_readonly()` for properties with a getter only), as in

.. code-block:: cpp

    .def_property("PropertyName", CppClassName::CppGetterMethodName, CppClassName::CppSetterMethodName, get_docstring("<ClassName.PropertyName>").c_str())

or

.. code-block:: cpp

    .def_property_readonly("PropertyName", CppClassName::CppGetterMethodName, get_docstring("<ClassName.PropertyName>").c_str())

.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

           .def_property_readonly("state_history",
                                 &tp::SingleArcDynamicsSimulator<double, double>::getEquationsOfMotionNumericalSolution,
                                 get_docstring("SingleArcSimulator.state_history").c_str())


Functions
.................

.. code-block:: cpp

   get_docstring("<function_name>").c_str()

as last argument of ``m.def("<function_name>", ... )`` exposure function.

.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

        m.def("aerodynamic", &tss::aerodynamicAcceleration,
              get_docstring("aerodynamic").c_str());


Overloads
....................

For overload nr X (X=0,1,...) of an overloaded function:

.. code-block:: cpp

   get_docstring("<function_name>", X).c_str()

as last argument of ``m.def("<function_name>", ... )`` exposure function.

.. toggle-header::
    :header: **Example**

    .. code-block:: cpp

        m.def("thrust_acceleration", py::overload_cast<const std::shared_ptr<tss::ThrustDirectionSettings>,
                      const std::shared_ptr<tss::ThrustMagnitudeSettings>>(&tss::thrustAcceleration),
              py::arg("thrust_direction_settings"),
              py::arg("thrust_magnitude_settings"),
              get_docstring("thrust_acceleration", 0).c_str());


.. note:: Class attributes do not need the ``get_docstring`` tag because their docstring is automatically retrieved
   from the class exposure.


Docstring template
*******************

As an additional resource, we have assembled a template to kickstart the writing process of docstrings. It can be found
in :ref:`YAML templates`.
