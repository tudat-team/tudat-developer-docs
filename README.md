# Tudat Developer Documentation

[![Documentation Status](https://readthedocs.org/projects/tudat-developer/badge/?version=latest)](https://tudat-developer.readthedocs.io/en/latest/?badge=latest)

TU Delft Astrodynamics Toolkit Developer Documentation

## Building the Developer Documentation

This section provides guidelines for building the Tudat developer
documentation.

### With `conda`

1. Ensure you
   have [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
   installed. You can check with:
   ```bash
     conda -V
   ```
   > **Note**: If you don't have conda installed or are unsure about it, follow
   the installation guidelines on
   the [official conda installation page](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

2. Navigate to the `tudat-developer-docs` root directory:
   ```bash
   cd tudat-developer-docs
   ```

3. Create a new conda environment with the required dependencies:
   ```bash
    conda env create -f environment.yml
    ```

4. Activate the newly created environment:
    ```bash
    conda activate tudat-developer-docs
    ```

5. Build the documentation:
    - Using the helper script:
      ```bash
      ./build.sh
      ```
    - For a standard build, use:
      ```bash
      sphinx-build source build/html
      ```
    - For auto-building (continuous updates during development), use:
      ```bash
      sphinx-autobuild source build/html
      ```
    - For auto-building on specific port and IP address, use:
      ```bash
      IPADDR=$(hostname -I | cut -d' ' -f1)
      sphinx-autobuild --host $IPADDR --port 8000 source build/html
      ```
