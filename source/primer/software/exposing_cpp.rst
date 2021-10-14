
Exposing C++ to Python
======================

This section contains fundamental concepts about pybind11, a library to expose C++ to Python, and more specific
indications for users who want to expose tudat functionalities to tudatpy.

.. note:: In this context, the terms *expose* and *bind* (and derived words) will be treated as synonyms.

The reader should be familiar with the content of the :ref:`Developer Environment` page before moving on to the
remainder of this guide.

.. admonition:: :fa:`graduation-cap` Learning Objectives
    :class: learning-objectives

    .. include:: objectives/exposing_cpp.rst

The contents of this guide are shown below:

.. toctree::
   :maxdepth: 3

   exposing_cpp.rst

Pybind11
--------

`pybind11 <https://pybind11.readthedocs.io/en/stable/index.html#>`_ is an open-source library that exposes C++ types
in Python. Through this software, the user interfaces of *tudat*, written in C++, can be made available in *tudatpy*.

*pybind11* has an extensive and well-written documentation accessible through the link
reported above, which the reader can refer to at anytime. The main goal of this page is to help the reader gain familiarity
with the nomenclature and functionalities offered by *pybind11* that are specifically useful to expose tudat code to
Python. *pybind11* features that are not directly applicable to tudat will not be presented.

.. note:: The hierarchical structure of the binding code is explained in `this section`_. It is noted that the actual
   compilation of the binding code is achieved by calling the ``kernel.cpp`` file; however, all the pybind functionalities
   that will be explained above are employed in the respective submodules.

.. _`this section`: https://tudat-developer.readthedocs.io/en/latest/primer/software/environment.html#introduction-to-tudat-bundle`


Headers and preliminaries
#########################

To write a C++ exposition file, the following header is needed:

.. code-block:: c++

   #include <pybind11/pybind11.h>

However, additional headers may be needed, such as:

.. code-block:: c++

   #include <pybind11/stl.h>  // to enable conversions from/to C++ standard library types

   #include <pybind11/eigen.h>  // to enable conversions from/to Eigen library types

   #include <pybind11/numpy.h>  // to enable conversions from/to Numpy library types

In addition, it is assumed that the following piece of code is present in each code snippet shown in this page:

.. code-block:: c++

   namespace py = pybind11;



Exposing a function
-------------------

In this section, the procedure to expose a simple function through *pybind11* will be explained. We will make use of
an example taken from tudat.

Suppose that we want to expose to Python the following tudat function (taken from `this file`_):

.. _`this file`: https://github.com/tudat-team/tudat/blob/fa30c49dca7ee27630717efb8546802589a4c8b7/include/tudat/simulation/propagation_setup/propagationOutputSettings.h#L558-L564

.. code-block:: c++

   inline std::shared_ptr< SingleDependentVariableSaveSettings > machNumberDependentVariable(
        const std::string& associatedBody,
        const std::string& bodyWithAtmosphere )
   {
    return std::make_shared< SingleDependentVariableSaveSettings >(
                mach_number_dependent_variable, associatedBody, bodyWithAtmosphere );
   }

This function is used to save the Mach number dependent variable associated to a certain body.
More specifically, it returns a smart pointer to a ``SingleDependentVariableSaveSettings`` object and takes as input
two standard pointers to ``std::string`` (these refer the body whose Mach number should be saved and the body whose
atmosphere should be used to compute the Mach number respectively).
This is the code (`available here`_) needed to expose the above function to Python:

.. _`available here`: https://github.com/tudat-team/tudatpy/blob/07b37d5ca8dce1c93b749cb29286c709ee91e2af/tudatpy/kernel/expose_simulation/expose_propagation_setup.cpp#L124-L127

.. code-block:: c++

   PYBIND11_MODULE(example, m) {
       m.def("mach_number",
             &tp::machNumberDependentVariable,
             py::arg("body"),
             py::arg("central_body"));
   }

The code reported above creates a Python module, called ``example`` (the creation of a module through the
``PYBIND11_MODULE()`` function is done in tudatpy only in the ``kernel.cpp`` file; most of the binding code is organized
through submodules structured as explained in section `pybind11`_ of this page).
``def()`` is the pybind function that creates binding code for a specific C++ function [1]_.
``def()`` takes two **mandatory** arguments:

1. a string (i.e., ``"mach_number"``), representing the name of the exposed function in Python;
2. a pointer to the C++ function that should be exposed (i.e., ``&tp::machNumberDependentVariable``), where ``tp`` is an
   abbreviation for the ``tudat::propagators`` namespace.

There are also additional input arguments that can be passed to the pybind ``def()`` function. In the context of the
example above, these are the keywords for the input arguments of the exposed function in Python, denoted by the syntax
``py::arg`` , which takes a string as input (i.e., ``"body"`` and ``"central_body"``). ``py`` is a shortcut for the
``pybind11`` namespace [2]_.

.. note:: There are many other optional input arguments to the ``def()`` function. For instance, a third positional
   argument after ``&tp::machNumberDependentVariable`` can be passed (of type ``std::string``) to provide a short
   documentation to the function. However, this pybind functionality is not employed for tudat/tudatpy.

As a result, pybind11 will generate a Python function that can be used as follows:

.. tabs::

     .. tab:: tudatpy

      .. code-block:: python

         # Module import
         import example
         # Function call
         dep_var_to_save = example.mach_number("Spacecraft", "Earth")

     .. tab:: tudat

      .. code-block:: c++

         std::make_shared<SingleDependentVariableSaveSettings> DepVarToSave = machNumberDependentVariable("Spacecraft", "Earth")

It is also allowed to call the tudatpy function ``mach_number()`` through the keyword arguments as follows:

.. code-block:: python

   dep_var_to_save = example.mach_number(body="Spacecraft", central_body="Earth")

It is also possible to have default values for certain keyword arguments. Suppose, for instance, that we want to have
``"Earth"`` as default central body. This can be achieved through the following implementation [3]_:

.. code-block:: c++

   PYBIND11_MODULE(example, m) {
       m.def("mach_number",
             &tp::machNumberDependentVariable,
             py::arg("body"),
             py::arg("central_body") = "Earth");
   }


The first issue that arises in the binding process is the conversion between variable types.
C++ is a statically-typed language, while Python is dynamically-typed. However, the type conversion is still needed
and in both directions.
In other words, the user can pass a Python variable as input to an exposed function. The type of such
variable will have to be converted to a C++ type before it is passed to the actual C++ function acting "behind the
scenes". The inverse process takes place for the output of a function.
This is one of the reasons why *pybind11* is necessary. Indeed, conversions between native types are dealt with
automatically in pybind. For instance, a C++ ``std::map<>`` is converted into a Python ``dict`` and vice-versa.
In our example, this automatic type conversion takes place between the input arguments, between the ``std::string``
in C++ and ``str`` in Python. A table reporting common conversions is reported below.

+------------+---------------------------------------------------------------------+
| **Python** |                                 **C++**                             |
+------------+---------------------------------------------------------------------+
| ``list``   | ``std::vector<>``/``std::deque<>``/``std::list<>``/``std::array<>`` |
+------------+---------------------------------------------------------------------+
| ``set``    |               ``std::set<>``/``std::unordered_set<>``               |
+------------+---------------------------------------------------------------------+
| ``dict``   |               ``std::map<>``/``std::unordered_map<>``               |
+------------+---------------------------------------------------------------------+

However, non-native data types need to be known to pybind to be converted properly. This is the case of the output type
of the ``machNumberDependentVariable()`` function, returning a pointer to an instance of the
``SingleDependentVariableSaveSettings`` class. If this class is not exposed to Python, the binding process will fail.
This offers the opportunity to explain how to generate binding code for classes, which will be done in
`Exposing a class`_.

Templated functions
###################
When a function is templated (see for instance `here <https://github.com/tudat-team/tudat/blob/888bd58eadddf2c5f1a90f206dd570759f315d1a/include/tudat/simulation/propagation_setup/propagationSettings.h#L473-L480>`_)
it is mandatory to specify the template argument when exposing it. Therefore, the exposition code must be duplicated
for each variable type (shown below for ``double``, example taken `from here <https://github.com/tudat-team/tudatpy/blob/a8839bd4195a41fa6bb1a48f4a091122802069bc/tudatpy/kernel/expose_simulation/expose_propagation_setup.cpp#L1332-L1335>`_).

.. code-block:: c++
   :emphasize-lines: 2

   m.def("multi_arc",
       &tp::multiArcPropagatorSettings<double>,
       py::arg("single_arc_settings"),
       py::arg("transfer_state_to_next_arc") = false );

.. _overloading_functions:
Overloading functions
#####################

If a free function or a member function is overloaded (i.e., it bears the same name but it accepts different sets of
input argument types), it is not possible to generate binding code in the traditional way explained in
`Exposing a function`_, because pybind will not know which version should be chosen to generate Python code.
Suppose, for instance, that we want to expose the `following overloaded function`_:

.. _`following overloaded function`: https://github.com/tudat-team/tudat/blob/fa30c49dca7ee27630717efb8546802589a4c8b7/src/simulation/propagation_setup/createAccelerationModels.cpp#L1632-L1637

.. code-block:: c++

   //! Function to create a set of acceleration models from a map of bodies and acceleration model types.
   basic_astrodynamics::AccelerationMap createAccelerationModelsMap(
        const SystemOfBodies& bodies,
        const SelectedAccelerationMap& selectedAccelerationPerBody,
        const std::map< std::string, std::string >& centralBodies )

   //! Function to create acceleration models from a map of bodies and acceleration model types.
   basic_astrodynamics::AccelerationMap createAccelerationModelsMap(
        const SystemOfBodies& bodies,
        const SelectedAccelerationMap& selectedAccelerationPerBody,
        const std::vector< std::string >& propagatedBodies,
        const std::vector< std::string >& centralBodies )

Both overloads of the ``createAccelerationModelsMap()`` function accept the system of bodies and an acceleration map as
first two input arguments. In addition, the function needs to know the central body of each propagated body.
This information can be passed as a ``std::map`` (where each propagated body is associated to its own central body
key-value pairs) or through two different ``std::vector`` objects, one containing the propagated bodies and the other
containing the respective central bodies. The `code`_ to expose both overloads is reported below:

.. _`code`: https://github.com/tudat-team/tudatpy/blob/07b37d5ca8dce1c93b749cb29286c709ee91e2af/tudatpy/kernel/expose_simulation/expose_propagation_setup.cpp#L1015-L1033

.. code-block:: c++

   m.def("create_acceleration_models",// overload [1/2]
          py::overload_cast<const tss::SystemOfBodies &,
          const tss::SelectedAccelerationMap &,
          const std::vector<std::string> &,
          const std::vector<std::string> &>(
              &tss::createAccelerationModelsMap),
          py::arg("body_system"),
          py::arg("selected_acceleration_per_body"),
          py::arg("bodies_to_propagate"),
          py::arg("central_bodies"));

   m.def("create_acceleration_models",// overload [2/2]
          py::overload_cast<const tss::SystemOfBodies &,
          const tss::SelectedAccelerationMap &,
          const std::map<std::string, std::string> &>(
              &tss::createAccelerationModelsMap),
          py::arg("body_system"),
          py::arg("selected_acceleration_per_body"),
          py::arg("central_bodies"));

The ``def()`` function is still used, where the first input argument is the function name in Python.
The difference with respect to a non-overloaded function exposition (see `Exposing a function`_) lies in the second
input argument, where pybind's templated ``py::overload_cast<>`` is used [8]_.
This pybind function casts overloaded functions to function pointers and its syntax is as follows:

1. the types of input arguments of the original C++ function are passed as template arguments
   (e.g., ``const tss::SystemOfBodies &``, etc...);
2. a reference to the original C++ function are passed as regular input arguments
   (e.g., ``&tss::createAccelerationModelsMap``, where ``tss`` is a shortcut for the ``tudat::simulation_setup``
   namespace).

The optional arguments to ``def()`` do not change with respect to what was explained in `Exposing a function`_.

.. warning:: In the (rare) case where a function is overloaded based on constness only, the pybind tag ``py::const_``
   must be added as second parameter to ``py::overload_cast<>``.


Exposing a class
----------------

As explained above, the ``SingleDependentVariableSaveSettings`` class should be exposed to Python as well. This class,
available at `this link`_, is defined as follows:

.. _`this link`: https://github.com/tudat-team/tudat/blob/fa30c49dca7ee27630717efb8546802589a4c8b7/include/tudat/simulation/propagation_setup/propagationOutputSettings.h#L126-L166

.. code-block:: c++

   class SingleDependentVariableSaveSettings : public VariableSettings
   {
   public:
        SingleDependentVariableSaveSettings(
                const PropagationDependentVariables dependentVariableType,
                const std::string& associatedBody,
                const std::string& secondaryBody = "",
                const int componentIndex = -1 ):
            VariableSettings( dependentVariable ),
            dependentVariableType_( dependentVariableType ),
            associatedBody_( associatedBody ),
            secondaryBody_( secondaryBody ),
            componentIndex_( componentIndex ) { }

        // Attributes
        PropagationDependentVariables dependentVariableType_;
        std::string associatedBody_;
        std::string secondaryBody_;
        int componentIndex_;
    };

The class has a constructor and it is derived class, whose parent is the ``VariableSettings`` class. The code to
expose it to Python, available through this `link`_ is as follows, where the exposition of the constructor was omitted
for now:

.. _`link`: https://github.com/tudat-team/tudatpy/blob/07b37d5ca8dce1c93b749cb29286c709ee91e2af/tudatpy/kernel/expose_simulation/expose_propagation_setup.cpp#L87-L98

.. code-block:: c++

   py::class_<tp::SingleDependentVariableSaveSettings,
        std::shared_ptr<tp::SingleDependentVariableSaveSettings>,
        tp::VariableSettings>(m, "tp::SingleDependentVariableSaveSettings")

It makes use of pybind's ``py::class_<>`` templated function [4]_. In the template, there are three arguments, of which
only the first one is mandatory:

1. the first template argument declares the C++ class that should be exposed
   (i.e., ``tp::SingleDependentVariableSaveSettings``);
2. the second template argument declares the type of pointer that should be used by pybind to refer to instances of such
   class (i.e., ``std::shared_ptr<tp::SingleDependentVariableSaveSettings>``). The default argument is a
   ``std::unique_ptr``, but in tudat the common and consistently used pointer is a ``std::shared_ptr<>`` [5]_;
3. the third template argument informs pybind that the class to be exposed is derived by the parent class
   ``tp::VariableSettings`` [6]_.

.. todo::
   When does a parent class need to be exposed? In theory, tp::VariableSettings does *not* have to be exposed...
   According to GG, "only when the class is part of the signature of a
   different function" (see recording at 14m01s).

.. warning:: The third template argument is necessary to ensure automatic downcasting of pointers referring to
   polymorphic base classes. In other words, when a function returns a pointer to an instance of a derived class, pybind
   automatically knows to "downcast" the pointer to the type of the derived class only if the base class is
   polymorphic (a class is said *polymorphic* if it has at least one virtual function).

In addition, there are two input arguments to the ``py::class_`` function:

1. the name of the Python module to which the exposed class will belong to (i.e., ``m``);
2. the name of the exposed class in Python, provided as a ``std::string``
   (i.e., ``"tp::SingleDependentVariableSaveSettings"``).

Exposing class constructors
###########################

Once the class has been exposed, one can also expose its *member functions* (in C++) which will become *methods*
(in Python). The first member function that will be exposed is the class constructor. This can be exposed through the
following code:

.. code-block:: c++

   py::class_<tp::SingleDependentVariableSaveSettings,
        std::shared_ptr<tp::SingleDependentVariableSaveSettings>,
        tp::VariableSettings>(m, "tp::SingleDependentVariableSaveSettings")
        .def(py::init<
             const tp::PropagationDependentVariables,
             const std::string &,
             const std::string &,
             const int>(),
             py::arg("dependent_variable_type"),
             py::arg("associated_body"),
             py::arg("secondary_body") = "",
             py::arg("component_idx") = -1);

The first three lines were explained above. To expose the class constructor, it is possible to use the pybind ``def()``
function, which is common to any function (whether it is a member of a class or not). In addition, the pybind
``py::init<>`` function is used to declare the definition of the constructor. This function takes the types of the input
arguments to the constructor as template arguments (i.e., ``const tp::PropagationDependentVariable``,
``const std::string &``, etc...). The templated function ``py::init<>`` makes it easy to overload the class constructor:
it is sufficient to define multiple ``.def(py::init<>)``, with different template arguments, to expose several versions
of the constructor, whose correct version is selected according to the input arguments types passed to the constructor.
An example, taken from `this tudat class`_ exposed `through this code`_, is provided below.
Overloading simple functions will be explained in section :ref:`overloading_functions`.

.. _`this tudat class`: https://github.com/tudat-team/tudat/blob/fa30c49dca7ee27630717efb8546802589a4c8b7/include/tudat/simulation/propagation_setup/propagationSettings.h#L585-L726
.. _`through this code`: https://github.com/tudat-team/tudatpy/blob/07b37d5ca8dce1c93b749cb29286c709ee91e2af/tudatpy/kernel/expose_simulation/expose_propagation_setup.cpp#L650-L722

.. toggle-header::
   :header: *Example: overloading a class constructor* **Show/Hide**

        .. code-block:: c++

            py::class_<
                tp::TranslationalStatePropagatorSettings<double>,
                std::shared_ptr<tp::TranslationalStatePropagatorSettings<double>>,
                tp::SingleArcPropagatorSettings<double>>(m, "TranslationalStatePropagatorSettings")
                .def(// ctor 1
                     py::init<
                     const std::vector<std::string> &,
                     const tba::AccelerationMap &,
                     const std::vector<std::string> &,
                     const Eigen::Matrix<double, Eigen::Dynamic, 1> &,
                     const std::shared_ptr<tp::PropagationTerminationSettings>,
                     const tp::TranslationalPropagatorType,
                     const std::shared_ptr<tp::DependentVariableSaveSettings>,
                     const double>(),
                     py::arg("central_bodies"),
                     py::arg("acceleration_models"),
                     py::arg("bodies_to_integrate"),
                     py::arg("initial_states"),
                     py::arg("termination_settings"),
                     py::arg("propagator") = tp::TranslationalPropagatorType::cowell,
                     py::arg("output_variables") = std::shared_ptr<tp::DependentVariableSaveSettings>(),
                     py::arg("print_interval") = TUDAT_NAN)
                .def(// ctor 2
                     py::init<const std::vector<std::string> &,
                     const tss::SelectedAccelerationMap &,
                     const std::vector<std::string> &,
                     const Eigen::Matrix<double, Eigen::Dynamic, 1> &,
                     const std::shared_ptr<tp::PropagationTerminationSettings>,
                     const tp::TranslationalPropagatorType,
                     const std::shared_ptr<tp::DependentVariableSaveSettings>,
                     const double>(),
                     py::arg("central_bodies"),
                     py::arg("acceleration_settings"),
                     py::arg("bodies_to_integrate"),
                     py::arg("initial_states"),
                     py::arg("termination_settings"),
                     py::arg("propagator") = tp::cowell,
                     py::arg("output_variables") = std::shared_ptr<tp::DependentVariableSaveSettings>(),
                     py::arg("print_interval") = TUDAT_NAN)
                .def(// ctor 3
                     py::init<const std::vector<std::string> &,
                     const tba::AccelerationMap &,
                     const std::vector<std::string> &,
                     const Eigen::Matrix<double, Eigen::Dynamic, 1> &,
                     const double,
                     const tp::TranslationalPropagatorType,
                     const std::shared_ptr<tp::DependentVariableSaveSettings>,
                     const double>(),
                     py::arg("central_bodies"),
                     py::arg("acceleration_models"),
                     py::arg("bodies_to_integrate"),
                     py::arg("initial_states"),
                     py::arg("termination_time"),
                     py::arg("propagator") = tp::cowell,
                     py::arg("output_variables") = std::shared_ptr<tp::DependentVariableSaveSettings>(),
                     py::arg("print_interval") = TUDAT_NAN)
                .def(// ctor 4
                     py::init<const std::vector<std::string> &,
                     const tss::SelectedAccelerationMap &,
                     const std::vector<std::string> &,
                     const Eigen::Matrix<double, Eigen::Dynamic, 1> &,
                     const double,
                     const tp::TranslationalPropagatorType,
                     const std::shared_ptr<tp::DependentVariableSaveSettings>,
                     const double>(),
                     py::arg("central_bodies"),
                     py::arg("acceleration_settings"),
                     py::arg("bodies_to_integrate"),
                     py::arg("initial_states"),
                     py::arg("termination_time"),
                     py::arg("propagator") = tp::cowell,
                     py::arg("output_variables") = std::shared_ptr<tp::DependentVariableSaveSettings>(),
                     py::arg("print_interval") = TUDAT_NAN)

|

.. warning:: The template arguments must be *always* provided to ``py::init<>``, even if the constructor is not
   overloaded.

The ``def`` function follows its standard behavior (explained above)
even when it is used to expose a class constructor; in other words, it can take a number of optional arguments
that specify the keyword corresponding to each input argument to the class constructor in Python (i.e.,
``py::arg("dependent_variable_type")``, etc...). In this example, the last two input arguments have default values.

.. note:: The set of parentheses after ``py::init<>()``, needed to comply with the correct syntax, is empty.
   Optional arguments can be passed to create custom constructors in Python [7]_. However, this pybind functionality
   is not used for tudat, therefore it will not be treated in this guide.


Exposing class attributes
#########################

Class attributes in C++ vs. in Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few differences between the Object-Oriented Programming (OOP) philosophy in C++ and Python. It is important
to know these differences before proceeding to the next sections. The reader who is already aware of this information
can skip this section.

One of the principles used in Object-Oriented Programming in C++ is *data encapsulation*. According to this principle,
class attributes should be accessible only from within the class and *not* by the user dealing with an instance of
that class. This is principle is (partly) enforced by C++: for instance, class attributes are by default *private*
(i.e., accessible only from within the class and its methods, also called *friends*) [9]_. This policy is useful mainly for
security reasons (data protection), but also because interaction with the data contained within a class becomes only
possible through its public methods; in other words, the user can interact with the class data through a dedicated
*user interface*, without knowing or dealing with the class's internal functioning directly. This strategy also
ensures that any changes to the class's internal structure will not affect the code that creates and uses instances
of that class [10]_. The most basic form of a user interface are *accessors* and *mutators* (hereafter referred to as
*getters* and *setters*).

In Python, on the other hand, the possibility of keeping class attributes private is not provided. Among Python
programmers, there is a widespread convention to use attribute names starting with an underscore
(e.g., ``myclass._myattribute``) to inform other developers and users that such attribute should *not* be called
directly outside of the class. However, this is only a convention and the programming language does *not* enforce this
behavior. For this reason, getters and setters are not as common in Python as they are in other OOP languages, such as
C++ or Java. In addition, the dot notation in Python to access and mutate class attributes makes the code much
more readable [11]_.

However, there may be cases where getters and setters are needed in Python classes as well. This is the case when code
is exposed from another OOP language, such as C++, as it happens for tudat: it is obviously easier to maintain the
same user interface, thus having keeping getters and setters in Python as well. In this case, it is recommended to
create a *class property*. This solution has the advantage of having getters and setters, while at the same time
benefitting from the dot notation [12]_.

These concepts will be partially re-explained and applied in `Exposing public attributes`_ (for attributes that
are not private, thus do not have associated getters and setters) and
`Exposing private attributes`_ (for attributes that are private, thus do have associated getters and setters, which
can become *properties* in Python).


Exposing public attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~

Analogously to the ``def()`` method of pybind's ``py::class_``, useful to expose member functions, pybind offers two
other methods to expose public attributes of a class (for private attributes, see `Exposing private attributes`_) [9]_.
``def_readwrite()`` can be used to expose a non-constant attribute. For instance, let's consider the following
`piece of code`_ that exposes `this class`_:

.. _`piece of code`: https://github.com/tudat-team/tudatpy/blob/61b07e8529c95f0fe48cd8c961811ce1e6aa0600/tudatpy/kernel/expose_astro/expose_aerodynamics.cpp#L223-L229
.. _`this class`: https://github.com/tudat-team/tudatpy/blob/61b07e8529c95f0fe48cd8c961811ce1e6aa0600/tudatpy/kernel/expose_astro/expose_aerodynamics.cpp#L51-L61

.. code-block:: c++
   :emphasize-lines: 5,6,7

   py::class_<ta::AerodynamicGuidance, ta::PyAerodynamicGuidance,
            std::shared_ptr< ta::AerodynamicGuidance > >(m, "AerodynamicGuidance")
            .def(py::init<>())
            .def("updateGuidance", &ta::AerodynamicGuidance::updateGuidance, py::arg("current_time") )
            .def_readwrite("angle_of_attack", &ta::PyAerodynamicGuidance::currentAngleOfAttack_)
            .def_readwrite("bank_angle", &ta::PyAerodynamicGuidance::currentBankAngle_)
            .def_readwrite("sideslip_angle", &ta::PyAerodynamicGuidance::currentAngleOfSideslip_);

The highlighted lines show the ``def_readwrite()`` function at work. It takes two arguments in the same way explained
in `Exposing a function`_:

1. the name of the attribute of the exposed Python class, passed as a string;
2. the attribute of the original C++ class, passed as a reference.

Similarly, the ``def_readonly()`` function can be used to expose ``const`` public class attributes. For instance, look
at `this example`_ exposing this `thrust direction class`_:

.. _`this example`: https://github.com/tudat-team/tudatpy/blob/a8839bd4195a41fa6bb1a48f4a091122802069bc/tudatpy/kernel/expose_simulation/expose_propagation_setup.cpp#L595-L604
.. _`thrust direction class`: https://github.com/tudat-team/tudat/blob/7b8b91943e67ad5db367989d71c33fa978aa3937/include/tudat/simulation/propagation_setup/thrustSettings.h#L75-L99

.. code-block:: c++
   :emphasize-lines: 9,10

    py::class_<
         tss::ThrustDirectionGuidanceSettings,
         std::shared_ptr<tss::ThrustDirectionGuidanceSettings>>(m, "ThrustDirectionGuidanceSettings")
         .def(py::init<
              const tss::ThrustDirectionGuidanceTypes,
              const std::string>(),
              py::arg("thrust_direction_type"),
              py::arg("relative_body"))
         .def_readonly("thrust_direction_type", &tss::ThrustDirectionGuidanceSettings::thrustDirectionType_)
         .def_readonly("relative_body", &tss::ThrustDirectionGuidanceSettings::relativeBody_);

The highlighted lines use ``def_readonly()`` in the same way as for ``def_readwrite()``.

.. note:: In tudat, it was decided to have as few public attributes as possible. Therefore, in principle,
   a developer should *not* rely on ``def_readonly()`` and ``def_readwrite()`` too much, as classes should be designed
   so that attributes are generally private and interaction with those is possible through getters (and setters).

.. _`private_attributes`:
Exposing private attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If class attributes are private, it is likely that they can be accessed (and, in some cases, modified) through
getters and setters. pybind has specific methods from the ``py::class_`` to deal with this situation, namely with
``def_property()`` and ``def_property_readonly()`` [13]_.
The latter is used for private attributes that have both getters and setters,
while the former is used for private attributes that cannot be modified (i.e., they only have a getter).
The following `example`_, exposing a `spherical harmonics class`_ in tudat, illustrates the usage of both:

.. _`example`: https://github.com/tudat-team/tudatpy/blob/7ac8fa9fb3bd8a40ac02c5028bc8316a7f452c3e/tudatpy/kernel/expose_astro/expose_gravitation.cpp#L37-L46
.. _`spherical harmonics class`: https://github.com/tudat-team/tudat/blob/a2691ad01255f5943e03470a123a49e07e712c70/include/tudat/astro/gravitation/sphericalHarmonicsGravityField.h#L67-L346

.. code-block:: c++

   py::class_<tg::SphericalHarmonicsGravityField,
            std::shared_ptr<tg::SphericalHarmonicsGravityField >,
            tg::GravityFieldModel>(m, "SphericalHarmonicsGravityField")
            .def_property_readonly("reference_radius", &tg::SphericalHarmonicsGravityField::getReferenceRadius )
            .def_property_readonly("maximum_degree", &tg::SphericalHarmonicsGravityField::getDegreeOfExpansion )
            .def_property_readonly("maximum_order", &tg::SphericalHarmonicsGravityField::getOrderOfExpansion )
            .def_property("cosine_coefficients", &tg::SphericalHarmonicsGravityField::getCosineCoefficients,
                          &tg::SphericalHarmonicsGravityField::setCosineCoefficients)
            .def_property("sine_coefficients", &tg::SphericalHarmonicsGravityField::getSineCoefficients,
                          &tg::SphericalHarmonicsGravityField::setSineCoefficients);

The syntax is as follows:

1. the first argument is, as usual, the name of the attribute of the exposed Python class, passed as a string;
2. the second argument is the getter function of the original C++ class, passed as a reference;
3. [only for ``def_property()``] the third argument is the setter function of the original C++ class,
   passed as a reference.

As a result, in Python it will be possible to operate without getter and setters, simply accessing properties through
the dot notation (see the `Python documentation`_ about the *property* decorator). As an example, in Python one could
do:

.. _`Python documentation`: https://docs.python.org/3/library/functions.html#property

.. code-block:: python

   # Create spherical harmonics object
   spherical_harmonics_model = ...
   # Retrieve sine coefficients
   sin_coeff = spherical_harmonics_model.sine_coefficients
   # Set sine coefficients
   spherical_harmonics_model.sine_coefficients = sin_coeff
   # Retrieve reference radius
   r = spherical_harmonics.reference_radius
   # Set reference radius
   spherical_harmonics.reference_radius = r  # THIS WOULD THROW AN ERROR

.. note:: In the current status of tudatpy, ``def_property()`` is not always used, because in some cases the getter
   and setter functions are exposed individually through the traditional ``def()`` method. However, this behavior is
   discouraged when generating other binding code in the future. When getters (and setters) are available in C++,
   it is recommended to rely on ``def_property()`` or ``def_property_readonly()``.

.. todo:: @Dominic, @Geoffrey, do you confirm the note above?

.. _`class_methods`:
Exposing class methods
#########################

Other class methods that are not part of the categories explained above can be simply exposed with the same syntax
used for free functions (see `Exposing a function`_).


Exposing an enum
----------------

Exposing enumerations types is relatively straightforward. Suppose we would like to expose `the following enum`_, located
in the ``tudat::propagators`` namespace:

.. _`the following enum`: https://github.com/tudat-team/tudat/blob/9a9143fcfec89db5f9a48e7607518855193913c9/include/tudat/astro/propagators/singleStateTypeDerivative.h#L27-L35

.. code-block:: c++

   //! Enum listing types of dynamics that can be numerically integrated
   enum IntegratedStateType
   {
        hybrid = 0,
        translational_state = 1,
        rotational_state = 2,
        body_mass_state = 3,
        custom_state = 4
   };

This can be done through pybind's ``py::enum_<>`` function as follows (`original code`_):

.. _`original code`: https://github.com/tudat-team/tudatpy/blob/239e508e47ad079761f08b4cb0b5621f12088837/tudatpy/kernel/expose_simulation/expose_propagation_setup.cpp#L1510-L1516

.. code-block:: c++

   py::enum_<tp::IntegratedStateType>(m, "StateType")
            .value("hybrid_type", tp::IntegratedStateType::hybrid)
            .value("translational_type", tp::IntegratedStateType::translational_state)
            .value("rotational_type", tp::IntegratedStateType::rotational_state)
            .value("mass_type", tp::IntegratedStateType::body_mass_state)
            .value("custom_type", tp::IntegratedStateType::custom_state)
            .export_values();

``py::enum_<>`` takes the name of the original C++ enum as template argument and the name of the Python equivalent as
second parameter (i.e., ``" StateType"``), with the first one being the module ``m`` as usual.
Each element of the enum can then be exposed using the ``value()`` function, that takes two parameters:

1. the name of the element in Python;
2. the name of the original C++ element to be exposed (where ``tp`` is, as usual, a shortcut for the
   ``tudat::propagators`` namespace).

The final function ``export_values()`` is needed to export the elements to the parent scope; without it,
``tudat::propagators::hybrid_type`` would be not be valid code [14]_.

.. todo:: to address: structure of the PYBIND11_MODULE (in kernel) and module/submodule definition. However, this
   overlaps with the content of `this tudat developer guide`_.
   I propose to either redirect from here to there or transfer its content here.

   .. _`this tudat developer guide`: https://tudat-developer.readthedocs.io/en/latest/primer/software/environment.html

References
----------

.. [1] `<https://pybind11.readthedocs.io/en/stable/basics.html#creating-bindings-for-a-simple-function>`_
.. [2] `<https://pybind11.readthedocs.io/en/stable/basics.html#keyword-arguments>`_
.. [3] `<https://pybind11.readthedocs.io/en/stable/basics.html#default-arguments>`_
.. [4] `<https://pybind11.readthedocs.io/en/stable/classes.html#creating-bindings-for-a-custom-type>`_
.. [5] `<https://pybind11.readthedocs.io/en/stable/advanced/smart_ptrs.html#std-shared-ptr>`_
.. [6] `<https://pybind11.readthedocs.io/en/stable/classes.html#inheritance-and-automatic-downcasting>`_
.. [7] `<https://pybind11.readthedocs.io/en/stable/advanced/classes.html#custom-constructors>`_
.. [8] `<https://pybind11.readthedocs.io/en/stable/classes.html#overloaded-methods>`_
.. [9] `<http://www.cplusplus.com/doc/tutorial/classes/>`_
.. [10] `<https://press.rebus.community/programmingfundamentals/chapter/encapsulation/>`_
.. [11] `<https://www.python-course.eu/python3_properties.php>`_
.. [12] `<https://docs.python.org/3/library/functions.html?highlight=property#property>`_
.. [13] `<https://pybind11.readthedocs.io/en/stable/classes.html#instance-and-static-fields>`_
.. [14] `<https://pybind11.readthedocs.io/en/stable/classes.html#enumerations-and-internal-types>`_
