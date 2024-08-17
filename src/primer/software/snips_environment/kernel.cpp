// expose tudat versioning
#include <tudat/config.hpp>

// include all exposition headers
#include "expose_simulation.h"
// other submodule headers...

// standard pybind11 usage
#include <pybind11/pybind11.h>
namespace py = pybind11;

PYBIND11_MODULE(kernel, m) {

    // Disable automatic function signatures in the docs.
    // NOTE: the 'options' object needs to stay alive
    // throughout the whole definition of the module.
    py::options options;
    options.disable_function_signatures();
    options.enable_user_defined_docstrings();

    // export the tudat version.
    m.attr("_tudat_version_major") = TUDAT_VERSION_MAJOR;
    m.attr("_tudat_version_minor") = TUDAT_VERSION_MINOR;
    m.attr("_tudat_version_patch") = TUDAT_VERSION_PATCH;

    // simulation module definition
    auto simulation = m.def_submodule("simulation");
    tudatpy::expose_simulation(simulation);

    // other submodule definitions...

    // versioning of kernel module
    #ifdef VERSION_INFO
      m.attr("__version__") = VERSION_INFO;
    #else
      m.attr("__version__") = "dev";
    #endif
}
