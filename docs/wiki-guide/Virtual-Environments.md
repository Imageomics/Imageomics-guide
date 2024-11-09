# Managing Dependencies and Environments
Recording dependencies and environment information is crucial for reproducibility and interoperability across different platforms. There are many options for this, and sometimes it is appropriate to use multiple within the same project.

The goal is to make it as easy as possible for others (including your future self) to run the code.

## Conda Environments
The following example commands will get you set up with a Conda environment that can be tracked and shared.

- Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Create an environment: `conda create --name <env-name>`
- Activate the environment: `conda activate <env-name>`
- Install packages you need: `conda install -c conda-forge python=3.9 pandas matplotlib`
    - `-c conda-forge` specifies the channel to install from. ([more information](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html))
    - You can specify the version of a package or omit this to get the latest available. ([more information](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#id2))
- Once the needed packages are installed, export the environment to a file: 
```bash
conda env export --no-builds --from-history | grep -v "prefix" > environment.yml
```
  - `--no-builds` and `--from-history` flags will cause the environment file to only specify the packages and versions that you manually installed. This may help with cross-platform compatibility by giving conda the flexibility to find compatible sub-dependencies on another system.
  - `| grep -v "prefix"` eliminates your system-specific environment storage location (what is called the `prefix`) from being added to the file
  - If you want to add the actual package versions that were installed (if you did not specify during installation) to the `environment.yml` file, you can check those and copy-paste them in manually with `conda env list`. 
  - Don't forget to also add and track this new file with git!
- To install the dependencies somewhere else from this file, use `conda env create -f environment.yml`.

## Pip Virtual Environment
For virtual environments using `pip` to install packages (Python environments), use `python -m pip freeze` to print a list of packages (and their versions) installed in the environment. `python -m pip freeze > requirements.txt` will populate a `requirements.txt` file with all these packages and versions listed (eg., `pandas==2.0.1`). Note that this will _not_ give only minimum software requirements, but will also print all dependencies. For more information, see the [pip documentation](https://pip.pypa.io/en/stable/cli/pip_freeze/).

This machine-readable file can then be installed using `pip install -r requirements.txt` when in the appropriate folder.
