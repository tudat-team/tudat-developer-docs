``tudatpy`` API Docs Pipeline
=============================

This Azure pipeline is designed to trigger the documentation build process for the ``tudatpy`` project on ReadTheDocs upon the successful completion of the ``tudatpy-feedstock`` pipeline. It selectively triggers based on updates to specific branches or tags and includes a robust testing framework to ensure the reliability and accuracy of the trigger script.

**Pipeline Resources**
----------------------

The pipeline listens for completion events from the ``tudatpy-feedstock`` pipeline and triggers based on updates to the ``main`` and ``develop`` branches, or any tags.

.. list-table:: Trigger Conditions
   :widths: 20 30 50
   :header-rows: 1

   * - Resource Type
     - Condition
     - Description
   * - Branch
     - ``main``
     - Triggers a build with ``branches=stable`` to ensure documentation reflects the stable version.
   * - Branch
     - ``develop``
     - Triggers a build with ``branches=latest``, suitable for previewing upcoming changes.
   * - Tag
     - ``*``
     - Any tag triggers a build with ``branches=<tag name>``, allowing documentation to correspond directly to specific releases.

**Script and Testing**
----------------------

The pipeline uses a shell script to dynamically set the ``branches`` parameter based on the source of the trigger. The script logic is encapsulated in a separate script file to facilitate testing and maintenance. These scripts are located in the repository under the following paths:

- Pipeline Script: ``tudatpy-feedstock/azure-readthedocs-pipeline.yml``
- Trigger Script: ``tudatpy-feedstock/scripts/prepare_api_build_trigger.sh``
- Test Script: ``tudatpy-feedstock/scripts/test_prepare_api_build_trigger.bats``

**Shell Script Logic Explained**

.. code-block:: bash

    # Determine the branch or tag from the source reference
    refType=$(echo $(Build.SourceBranch) | cut -d'/' -f2)
    refName=$(echo $(Build.SourceBranch) | awk -F/ '{print $NF}')

    # Default to "stable" for the main branch
    branchArg="stable"
    if [ "$refType" = "heads" ]; then
        if [ "$refName" = "develop" ]; then
            branchArg="latest"
        fi
    elif [ "$refType" = "tags" ]; then
        branchArg="$refName"
    fi

    # The actual API call is made here
    curl -X POST \
         -d "token=$(READTHEDOCS-TOKEN)" \
         -d "branches=$branchArg" \
         https://readthedocs.org/api/v2/webhook/tudatpy/200830/

**Automated Testing**

To ensure the script performs as expected across different scenarios, a series of automated tests are conducted using `bats` (Bash Automated Testing System). These tests simulate input conditions and verify the output of the script.

.. code-block:: text

    ✓ Output 'stable' for main branch
    ✓ Output 'latest' for develop branch
    ✓ Output tag name for a tag

**Testing Results**

The tests confirm that the script correctly identifies the type of branch or tag and sets the `branchArg` accordingly. This validation process ensures the reliability of the pipeline trigger mechanism.

**Pipeline Execution**

.. code-block:: yaml

    # app-ci YAML pipeline
    # This pipeline initiates when the tudatpy-feedstock pipeline completes.
    # It listens for changes in specific branches or tags and triggers accordingly.
    resources:
      pipelines:
        - pipeline: readthedocs-api-docs
          source: tudatpy-feedstock
          trigger:
            branches:
              include:
                - main
                - develop
            tags:
              include:
                - '*'

    steps:
      - script: |
            branchArg=$(./scripts/prepare_api_build_trigger.sh $(Build.SourceBranch))
            curl -X POST \
                 -d "token=$(READTHEDOCS-TOKEN)" \
                 -d "branches=$branchArg" \
                 https://readthedocs.org/api/v2/webhook/tudatpy/200830/
        displayName: Trigger readthedocs API docs build

.. todo:: Discuss proposal on modified docs build to something more direct and simple