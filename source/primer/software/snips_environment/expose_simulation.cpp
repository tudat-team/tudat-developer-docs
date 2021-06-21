
// include own exposition headers
#include "expose_simulation.h"
// include submodule exposition headers
#include "expose_simulation/expose_environment_setup.h"
#include "expose_simulation/expose_estimation_setup.h"
#include "expose_simulation/expose_propagation_setup.h"
#include "expose_simulation/expose_shape_based_thrust.h"

// standard pybind11 usage
#include <pybind11/pybind11.h>
namespace py = pybind11;

// bundling submodules for expose_simulation in tudatpy namespace
namespace tudatpy {
void expose_simulation(py::module &m) {

  // environment_setup submodule definition
  auto environment_setup = m.def_submodule("environment_setup");
  expose_environment_setup(environment_setup);

  // propagation_setup submodule definition
  auto propagation_setup = m.def_submodule("propagation_setup");
  expose_propagation_setup(propagation_setup);

  // estimation_setup submodule definition
  auto estimation_setup = m.def_submodule("estimation_setup");
  expose_estimation_setup(estimation_setup);

  // shape_based_thrust submodule definition
  auto shape_based_thrust = m.def_submodule("shape_based_thrust");
  expose_shape_based_thrust(shape_based_thrust);
};

}// namespace tudatpy