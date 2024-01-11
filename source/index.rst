.. tudat-developer documentation master file, created by
   sphinx-quickstart on Mon Apr 26 20:32:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. or Developer's Guide

Tudat Developer Documentation
=============================

Welcome to the Tudat Developer Documentation. Browse the latest developer
documentation, including tutorials, sample code, articles and external API
references.

.. panels::
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    ---

    .. link-button:: Development Operations
          :type: ref
          :text: Development Operations
          :classes: btn-outline-primary btn-block

    ^^^

    :ref:`Code Collaboration`

    :ref:`Release Versioning`

    :ref:`Package Management`

    :ref:`Continuous Deployment`

    ---

    .. link-button:: Software Documentation
          :type: ref
          :text: Software Documentation
          :classes: btn-outline-primary btn-block

    ^^^


    :ref:`Sphinx Documentation`

    :ref:`API Documentation`

    ---

    .. link-button:: Software Development
          :type: ref
          :text: Software Development
          :classes: btn-outline-primary btn-block

    ^^^

    :ref:`Build System`

    :ref:`Developer Environment`

    :ref:`Extending Features`

    :ref:`Exposing C++ to Python`
    
    :ref:`Exposing kernel modules directly through tudatpy`

    :ref:`Autocompletion in Python`



.. toctree::
   :maxdepth: 3
   :caption: Primer
   :hidden:

   primer/devops
   primer/docs
   primer/software
   primer/bib

Follow tutorials that demonstrate specific tasks that concern the maintenance,
development, and documentation of Tudat.

.. note:: The following items are **placeholders**.

.. toctree::
   :maxdepth: 3
   :caption: Guides

   guides/managing_access_tokens
   guides/new_conda_package
   guides/new_forge_feedstock
   guides/new_tudat_function
   guides/new_tudat_class
   guides/new_tudat_module
   guides/pdf_with_sphinx
   guides/hybrid_modules

.. toctree::
   :maxdepth: 3
   :caption: Resources
   :hidden:

   resources/commands
   resources/tools
   ./../CHANGELOG

.. todo:: (*) Rename ``rerendering_a_feedstock.rst`` to  ``rerendering_feedstocks.rst``