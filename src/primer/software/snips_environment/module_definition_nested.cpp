
// include .h
#include "expose_astro.h"

// include .h of selected submodule definition
#include "expose_astro/expose_fundamentals.h"
#include "expose_astro/expose_ephemerides.h"
// ...

// pybind11 usage
#include <pybind11/pybind11.h>
namespace py = pybind11;

// namespace package level
namespace tudatpy {
// namespace module level
namespace astro {

// module definition function
void expose_astro(py::module &m) {

  // include selected submodules (source code exposition in nested namespaces 'fundamentals', 'ephemerides', etc):

  // expose_fundamentals.h
  auto fundamentals = m.def_submodule("fundamentals");
  expose_fundamentals(fundamentals);

  // expose_ephemerides.h
  auto ephemerides = m.def_submodule("ephemerides");
  expose_ephemerides(ephemerides);

  // ...

};

} // namespace module level
} // namespace package level



