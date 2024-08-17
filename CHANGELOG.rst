==========================
Changelog
==========================

.. current developments

v0.1.4
====================

**Added:**

* Separated page on readthedocs (:ref:`Release an online version`)
* API docstrings (:ref:`How to write docstrings`)
* YAML template page (:ref:`YAML templates`)

**Changed:**

* Moved readthedocs content from :ref:`Sphinx Documentation` to :ref:`Release an online version`
* Moved bumpversion content from :ref:`Sphinx Documentation` to :ref:`Releasing a new version with bumpversion`

**Authors:**

* Filippo Oggionni

v0.1.3
====================

**Changed:**

* Structure of :ref:`Development Operations`

**Authors:**

* Filippo Oggionni

v0.1.2
====================

**Added:**

* :ref:`How to contribute to Tudat`

**Removed:**

* Section about `rever`

**Authors:**

* Filippo Oggionni

v0.1.1
====================

**Changed:**

* How unstable releases work in :ref:`Sphinx Documentation`

**Authors:**

* Filippo Oggionni

v0.1.0
====================

**Added:**

* Releasing versions of documentation in :ref:`Sphinx Documentation`
* Note about clearing browser caches in :ref:`Sphinx Documentation`

**Changed:**

* How to compile the documentation in :ref:`Sphinx Documentation`
* Transferred some content from `tudat-space <https://docs.tudat.space>`_

**Authors:**

* Filippo Oggionni

v0.0.11
====================

**Added:**

* :ref:`Cloning a Repository`
* Trial "Mission Brief" detailing practical tasks in primer.
* Content in :ref:`Develop and Master Branches` for switching to ``develop``
  branch in Tudat Git workflow.
* Note on ``git branch`` and variants in detailing local and remote branches
  available.
* Added :ref:`Feature Branches`. Placeholders added for :ref:`Release Branches`
  and :ref:`Hotfix Branches` to explain the Gitflow Workflow.

**Changed:**

* Extracted "git - the simple guide" from Mission brief, moved to top level
  :ref:`Code Collaboration`.

**Authors:**

* Geoffrey H. Garrett



v0.0.10
====================

**Added:**

* Quality of life improvement for Code Collaboration/ Git. Note for users
  on how to save git credentials via the Command Line (if they choose to do so
  with the security risk).

* Added :ref:`News Workflow` to :ref:`Release Versioning` topic. Currently
  identical and unadapted from https://regro.github.io/rever-docs/news.html.

* Added todo for elaborating on ``osx_arm64`` build variants.

**Authors:**

* Geoffrey H. Garrett



v0.0.9
====================

**Added:**

* Tutorial: Re-rendering a ``conda-smithy`` feedstock (placeholder)
* Todo for renaming file aforementioned tutorial.

**Fixed:**

* Fixed all errors/warnings during ``make html`` for sphinx docs.

**Authors:**

* Geoffrey H. Garrett


v0.0.8
====================

**Changed:**

* Fixed Change Log formatting. (Basically figuring out consistent workflow
  for ``rever`` with these commits)

**Authors:**

* Geoffrey H. Garrett



v0.0.7
====================

**Changed:**

* ``author`` variable is now retrieve directly from rever ``AUTHORS`` files
  during the building of docs.

**Authors:**

* Geoffrey H. Garrett


v0.0.6
====================

**Changed:**

* Changed ``rever.xsh`` activity ordering. Placed author activity as first.

**Authors:**

* Geoffrey H. Garrett



v0.0.5
====================

**Added:**

* Topics are used to contextualise external and internal tools, workflows and
  conventions in the context of the Tudat Developer user case.

* Topics:
    - Development Operations
        - Code Collaboration (ongoing)
        - Release Versioning (ongoing)
        - Package Management (ongoing)
        - Continuous Deployment (ongoing)
    - Software Documentation (ongoing)
    - Software Development (ongoing)
        - Build System (ongoing)
        - Developer Environment (ongoing)
        - Extending Features (ongoing)
        - Exposing C++ in Python (ongoing)

* Tutorials: (added placeholders)
    - Adding a Package to Conda
    - Adding a Function to Tudat
    - Adding a Class to Tudat
    - Adding a Module to Tudat
    - Generate PDFs with Sphinx Locally

**Authors:**

* Geoffrey H. Garrett
