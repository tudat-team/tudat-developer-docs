// include own exposition header
#include "expose_constants.h"

// enable usage of docstrings (%!)
#include "tudatpy/docstrings.h"

// include relevant tudat src code headers
#include "tudat/constants.h"
#include "tudat/astro/basic_astro/timeConversions.h"

// enable pybind usage
#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
namespace py = pybind11;

// aliasing tudat namespaces for convenience
namespace tbc = tudat::celestial_body_constants;
namespace tpc = tudat::physical_constants;
namespace tmc = tudat::mathematical_constants;
namespace tba = tudat::basic_astrodynamics;


namespace tudatpy {
// dedicated 'constants' namespace inside tudatpy namespace (%!)
namespace constants {

void expose_constants(py::module &m) {
// content from tudat namespaces is exposed via pybind:

  m.attr("__doc__") = tudatpy::get_docstring("constants").c_str();

  // celestialBodyConstants.h
  m.attr("EARTH_EQUATORIAL_RADIUS") = tbc::EARTH_EQUATORIAL_RADIUS;
  m.attr("EARTH_FLATTENING_FACTOR") = tbc::EARTH_FLATTENING_FACTOR;
  m.attr("EARTH_GEODESY_NORMALIZED_J2") = tbc::EARTH_GEODESY_NORMALIZED_J2;
  // exposing more content (here attributes) from celestialBodyConstants.h

  // physicalConstants.h
  m.attr("SEA_LEVEL_GRAVITATIONAL_ACCELERATION") = tpc::SEA_LEVEL_GRAVITATIONAL_ACCELERATION;
  m.attr("JULIAN_DAY") = tpc::JULIAN_DAY;
  m.attr("JULIAN_DAY_LONG") = tpc::JULIAN_DAY_LONG;
  // exposing more content (here attributes) from physicalConstants.h

  // exposing more content from other tudat namespaces (tudat::mathematical_constants, tudat::basic_astrodynamics)

  };

}// namespace constants
}// namespace tudatpy