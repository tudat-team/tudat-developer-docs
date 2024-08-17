
// include .h
#include "expose_ephemerides.h"

// include .h of considered source content
#include <tudat/astro/ephemerides.h>
#include <tudat/simulation/simulation.h> // TODO: EphemerisType should be in <tudat/astro/ephemerides.h>

// pybind11 usage
#include <pybind11/eigen.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
namespace py = pybind11;

// aliasing namespaces of considered source content
namespace te = tudat::ephemerides;
namespace tss = tudat::simulation_setup;

// namespace package level
namespace tudatpy {
// namespace submodule level
namespace ephemerides {

void expose_ephemerides(py::module &m) {

  // tudat source code (C++) to tudatpy (python) interfaces defined in submodule namespace:

  py::class_<te::Ephemeris, std::shared_ptr<te::Ephemeris>>(m, "Ephemeris")
      .def("get_cartesian_state", &te::Ephemeris::getCartesianState, py::arg("seconds_since_epoch") = 0.0)
      .def("get_cartesian_position", &te::Ephemeris::getCartesianPosition, py::arg("seconds_since_epoch") = 0.0)
      .def("get_cartesian_velocity", &te::Ephemeris::getCartesianVelocity, py::arg("seconds_since_epoch") = 0.0);

  py::enum_<tss::EphemerisType>(m.attr("Ephemeris"), "EphemerisType")
      .value("approximate_planet_positions", tss::approximate_planet_positions)
      .value("direct_spice_ephemeris", tss::direct_spice_ephemeris)
      // ...

  py::class_<te::RotationalEphemeris,
             std::shared_ptr<te::RotationalEphemeris>>
      RotationalEphemeris_(m, "RotationalEphemeris");

  // ...

};

} // namespace submodule level
} // namespace package level
