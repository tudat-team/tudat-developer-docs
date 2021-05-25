
// include .h
#include "expose_constants.h"

// include .h of considered source content
#include "tudatpy/docstrings.h"
#include "tudat/constants.h"
#include "tudat/astro/basic_astro/timeConversions.h"

// pybind11 usage
#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
namespace py = pybind11;

// aliasing namespaces of considered source content
namespace tbc = tudat::celestial_body_constants;
namespace tpc = tudat::physical_constants;
// ...

// namespace package level
namespace tudatpy {
// namespace module level
namespace constants {

// module definition function
void expose_constants(py::module &m) {

  // tudat source code (C++) to tudatpy (python) interfaces defined in module namespace:

  // docstrings (no source code interface here)
  m.attr("__doc__") = tudatpy::get_docstring("constants").c_str();

  // celestialBodyConstants.h
  m.attr("EARTH_EQUATORIAL_RADIUS") = tbc::EARTH_EQUATORIAL_RADIUS;
  m.attr("EARTH_FLATTENING_FACTOR") = tbc::EARTH_FLATTENING_FACTOR;
  m.attr("EARTH_GEODESY_NORMALIZED_J2") = tbc::EARTH_GEODESY_NORMALIZED_J2;
  // ...

  // physicalConstants.h
  m.attr("SEA_LEVEL_GRAVITATIONAL_ACCELERATION") = tpc::SEA_LEVEL_GRAVITATIONAL_ACCELERATION;
  m.attr("JULIAN_DAY") = tpc::JULIAN_DAY;
  m.attr("JULIAN_DAY_LONG") = tpc::JULIAN_DAY_LONG;
  // ...

  // ...

};

}// namespace module level
}// namespace package level
