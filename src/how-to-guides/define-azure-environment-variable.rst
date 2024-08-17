
Define Azure Environment Variables
----------------------------------

.. note::
   This section is intended for maintainers of the feedstock repositories (at current). If you are not a maintainer, you can safely ignore this section. A more advanced guide on Azure Pipelines can be found `here <https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables>`_.

1. Navigate to https://dev.azure.com/ and sign in.

.. image:: /assets/screenshots/azure_pipeline_1.png

2. Click the ``feedstock-builds`` project under the ``tudat-team`` organization (https://dev.azure.com/tudat-team).

.. image:: /assets/screenshots/azure_pipeline_2.png

3. Click "Pipelines" under the ``feedstock-builds`` project.

.. image:: /assets/screenshots/azure_pipeline_3.png

4. Click on the specific pipeline in which you want to set the environment variable (e.g. ``tudat-feedstock``).

.. image:: /assets/screenshots/azure_pipeline_4.png

5. Click "Edit" in the top-right of the page.

.. image:: /assets/screenshots/azure_pipeline_5.png

6. Click "Variables" in the top-right of the page.

.. image:: /assets/screenshots/azure_pipeline_6.png

7. Update an existing token (e.g. ``BINSTAR_TOKEN``), or create a new one with the ``+`` icon.

.. image:: /assets/screenshots/azure_pipeline_7.png

.. important::
   It is crucial to keep the environment variables private and secure. Ensure that you do not share them or commit them to a public repository, as this could lead to security issues.
