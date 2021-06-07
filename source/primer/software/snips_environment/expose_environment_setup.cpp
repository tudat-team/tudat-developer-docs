
// include own exposition header
#include "expose_environment_setup.h"

// enable usage of docstrings (%!)
#include "tudatpy/docstrings.h"

// include relevant tudat src code headers
#include <tudat/simulation/environment_setup.h>
#include <tudat/astro/reference_frames/referenceFrameTransformations.h>

// enable pybind usage (%! details in other topic?)
#include <pybind11/eigen.h>
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/complex.h>
//#include <pybind11/chrono.h>
//#include <pybind11/numpy.h>
namespace py = pybind11;

// aliasing tudat namespaces for convenience
namespace tss = tudat::simulation_setup;
namespace te = tudat::ephemerides;
namespace ti = tudat::interpolators;
namespace tba = tudat::basic_astrodynamics;
namespace ta = tudat::aerodynamics;
namespace trf = tudat::reference_frames;
namespace tg = tudat::gravitation;
namespace tcc = tudat::coordinate_conversions;


namespace tudatpy {

// grouping exposure of aerodynamic_coefficient_setup-related content in a dedicated exposure function
void expose_aerodynamic_coefficient_setup(py::module &m) {

    /////////////////////////////////////////////////////////////////////////////
    // createAerodynamicCoefficientInterface.h
    /////////////////////////////////////////////////////////////////////////////
    py::class_<tss::AerodynamicCoefficientSettings,
            std::shared_ptr<tss::AerodynamicCoefficientSettings>>
            AerodynamicCoefficientSettings_(m, "AerodynamicCoefficientSettings",
                                            get_docstring("AerodynamicCoefficientSettings").c_str());

    py::class_<tss::ConstantAerodynamicCoefficientSettings,
            std::shared_ptr<tss::ConstantAerodynamicCoefficientSettings>,
            tss::AerodynamicCoefficientSettings>(
                m, "ConstantAerodynamicCoefficientSettings", "<no doc>")
            .def(py::init<const double, const double, const double,
                 const Eigen::Vector3d &, const Eigen::Vector3d &,
                 const Eigen::Vector3d &, const bool, const bool,
                 const std::shared_ptr<ti::InterpolatorSettings>>(),
                 py::arg("reference_length"), py::arg("reference_area"),
                 py::arg("lateral_reference_length"),
                 py::arg("moment_reference_point"),
                 py::arg("constant_force_coefficient"),
                 py::arg("constant_moment_coefficient") = Eigen::Vector3d::Zero(),
                 py::arg("are_coefficients_in_aerodynamic_frame") = true,
                 py::arg("are_coefficients_in_negative_axis_direction") = true,
                 py::arg("interpolator_settings") = nullptr)
            .def(py::init<const double, const Eigen::Vector3d &, const bool,
                 const bool>(),
                 py::arg("reference_area"),
                 py::arg("constant_force_coefficient"),
                 py::arg("are_coefficients_in_aerodynamic_frame") = true,
                 py::arg("are_coefficients_in_negative_axis_direction") = true);

    m.def("constant",
          py::overload_cast<const double, const Eigen::Vector3d &, const bool,
          const bool>(
              &tss::constantAerodynamicCoefficientSettings),
          py::arg("reference_area"),
          py::arg("constant_force_coefficient"),
          py::arg("are_coefficients_in_aerodynamic_frame") = true,
          py::arg("are_coefficients_in_negative_axis_direction") = true);

    m.def("custom",
          py::overload_cast<
          const std::function< Eigen::Vector3d( const std::vector< double >& ) >,
          const double, const std::vector< ta::AerodynamicCoefficientsIndependentVariables >,
          const bool, const bool >( &tss::customAerodynamicCoefficientSettings),
          py::arg("force_coefficient_function"),
          py::arg("reference_area"),
          py::arg("independent_variables"),
          py::arg("are_coefficients_in_aerodynamic_frame") = true,
          py::arg("are_coefficients_in_negative_axis_direction") = true);

    // exposing more content from the aerodynamic coefficient setup
}

// grouping exposure of atmosphere_setup-related content in yet another dedicated exposure function
void expose_atmosphere_setup(py::module &m) {

    /////////////////////////////////////////////////////////////////////////////
    py::class_<tss::AtmosphereSettings,
            std::shared_ptr<tss::AtmosphereSettings>>(m, "AtmosphereSettings")
            .def_property("wind_settings", &tss::AtmosphereSettings::getWindSettings,
                          &tss::AtmosphereSettings::setWindSettings );

        py::class_<tss::ExponentialAtmosphereSettings,
                std::shared_ptr<tss::ExponentialAtmosphereSettings >,
                tss::AtmosphereSettings>(m, "ExponentialAtmosphereSettings");

        py::class_<tss::TabulatedAtmosphereSettings,
                std::shared_ptr<tss::TabulatedAtmosphereSettings >,
                tss::AtmosphereSettings>(m, "TabulatedAtmosphereSettings");


    py::class_<tss::WindModelSettings,
            std::shared_ptr<tss::WindModelSettings>>(m, "WindModelSettings");

    m.def("exponential",
          py::overload_cast<const std::string&>(
              &tss::exponentialAtmosphereSettings ),
          py::arg("body_name") );

    m.def("exponential",
          py::overload_cast<const double, const double>(
              &tss::exponentialAtmosphereSettings ),
          py::arg("scale_height"),
          py::arg("surface_density") );

    // exposing more content from the atmospheric setup
}

// exposing other grouped content in many more dedicated exposure function


// define exposure function on submodule level 'environment_setup'
void expose_environment_setup(py::module &m) {

  /*  This exposition follows the structure of
   *  tudat/src/simulation/environment_setup/
   *  environment_setup
   *  ├── body.h
   *  ├── createBodies.h
   *  ├── defaultBodies.h
   *  ├── createAerodynamicCoefficientInterface.h (pre-grouped)
   *  ├── createRadiationPressureInterface.h (pre-grouped)
   *  ├── createRotationModel.h (pre-grouped)
   *  ├── createGravityField.h (pre-grouped)
   *  ├── createEphemeris.h (pre-grouped)
   *  ├── createAtmosphereModel.h (pre-grouped)
   *  ├── createBodyShapeModel.h (pre-grouped)
   *  └── createGravityFieldVariations.h (pre-grouped)
   */

    /////////////////////////////////////////////////////////////////////////////
    // body.h ///////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////////////////////////////
    py::class_<tss::Body, std::shared_ptr<tss::Body>>(m, "Body")
            .def(py::init<const Eigen::Vector6d &>(), py::arg("state") = Eigen::Vector6d::Zero())
            .def("get_ephemeris_frame_to_base_frame", &tss::Body::getEphemerisFrameToBaseFrame)
            .def("set_ephemeris_frame_to_base_frame", &tss::Body::setEphemerisFrameToBaseFrame)
            .def_property("ephemeris_frame_to_base_frame", &tss::Body::getEphemerisFrameToBaseFrame, &tss::Body::setEphemerisFrameToBaseFrame)
            .def("get_state", &tss::Body::getState)
            .def("set_state", &tss::Body::setState)
            // more function definitions
            .def_property("flight_conditions", &tss::Body::getFlightConditions, &tss::Body::setFlightConditions)
            .def_property_readonly("state", &tss::Body::getState)
            // more attribute definitions

        // more class and function exposition from body.h

    // more class and function exposition from createBodies.h
    // more class and function exposition from defaultBodies.h


    // gathering all exposed content that has been pre-grouped with their dedicated exposition functions
    auto aerodynamic_coefficient_setup = m.def_submodule("aerodynamic_coefficients");
    expose_aerodynamic_coefficient_setup(aerodynamic_coefficient_setup);

    auto radiation_pressure_setup = m.def_submodule("radiation_pressure");
    expose_radiation_pressure_setup(radiation_pressure_setup);

    auto rotation_model_setup = m.def_submodule("rotation_model");
    expose_rotation_model_setup(rotation_model_setup);

    auto gravity_field_setup = m.def_submodule("gravity_field");
    expose_gravity_field_setup(gravity_field_setup);

    auto ephemeris_setup = m.def_submodule("ephemeris");
    expose_ephemeris_setup(ephemeris_setup);

    auto atmosphere_setup = m.def_submodule("atmosphere");
    expose_atmosphere_setup(atmosphere_setup);

    auto shape_setup = m.def_submodule("shape");
    expose_shape_setup(shape_setup);

    auto gravity_variation_setup = m.def_submodule("gravity_field_variation");
    expose_gravity_field_variation_setup(gravity_variation_setup);


}

}// namespace tudatpy
