# Code Checklist

This checklist provides expectations for the code repositories created for the Experiential AI & Ecology Course (Spring Semester 2025). 

## Required Files
- [ ] **License**: Verify and include an appropriate license (e.g., `MIT`, `CC0-1.0`, etc.). See discussion in the [guide](GitHub-Repo-Guide.md/#license).
- [ ] **README File**: Following the [guide](GitHub-Repo-Guide.md/#readme), provide a detailed `README.md` with:
    - [ ] Overview of the project.
    - [ ] Installation instructions.
    - [ ] Basic usage examples.
    - [ ] Links to related/created dataset(s).
    - [ ] Links to related/created model(s).
    - [ ] Acknowledge source code dependencies and contributors.
    - [ ] Reference related datasets used in training or evaluation.
- [ ] **Requirements File**: Provide a [file detailing software requirements](GitHub-Repo-Guide.md/#software-requirements-file), such as a `requirements.txt` or `pyproject.toml` for Python dependencies.
- [ ] **Gitignore File**: GitHub has premade `.gitignore` files ([here](https://github.com/github/gitignore)) tailored to particular languages (eg., [R](https://github.com/github/gitignore/blob/main/R.gitignore) or [Python](https://github.com/github/gitignore/blob/main/Python.gitignore)), operating systems, etc.
- [ ] **CITATION CFF**: This facilitates citation of your work, follow guidance provided in the [guide](GitHub-Repo-Guide.md/#citation).

### Data-Related
- [ ] Preprocessing code.
- [ ] Description of dataset(s), including description of training and testing sets (with links to relevant portions of dataset card, which will have more information).

### Model-Related
- [ ] Training code.
- [ ] Inference/evaluation code.
- [ ] Model weights (if not in Hugging Face model repository).
- [ ] Description of model(s)/benchmark(s).
- [ ] Explanation of training and testing (with links to relevant portions of model card, which will have more information).

!!! note
    The [bioclip GitHub repository](https://github.com/Imageomics/bioclip) provides an example of incorporating data-and model-related code into a GitHub repository as published open-source code for both data and model development.

## General Information

- [ ] **Repository Structure**: Ensure the code repository follows a clear and logical directory structure. (See [guide](GitHub-Repo-Guide.md/#general-repository-structure).)
- [ ] **Code Comments**: Include meaningful inline comments and function descriptions for clarity.
- [ ] **Random Seed Control**: Save random seeds to ensure reproducible results.


## Security Considerations

- [ ] **Sensitive Data Handling**: Ensure no hardcoded sensitive information (e.g., API keys, credentials) are included in your repository. These can be shared through a config file on OSC.


!!! note
    The best practices described below will help you meet the above requirements. The more advanced development practices noted further down are included for educational purposes and since some groups have chosen to use linters. They are not required for this course; however, we recommend having a group discussion about the topics covered in [Code Quality](#code-quality).

---

## Best Practices

The [Repo Guide](GitHub-Repo-Guide.md/) provides general guidance on repository structure, [collaborative workflow](The-GitHub-Workflow.md/), and [how to make and review pull requests (PR)](The-GitHub-Pull-Request-Guide.md/). Below, we highlight some best practices in checklist form that are recommended for this course and beyond. 

### Reproducibility

- **Version Control**: Use Git for version control and commit regularly.
- **Modularization**: Structure code into reusable and independent modules.
- **Code Execution**: Provide Notebooks to demonstrate how to reproduce results.


### Code Review & Maintenance

- **Code Reviews**: Regular peer reviews for quality assurance. Refer to the [GitHub Repo Guide](GitHub-Repo-Guide.md/).
- **Issue Tracking**: Use GitHub issues for tracking bugs and feature requests. 
- **Versioning**: Tag releases, changelogs can be auto-generated and informative when PRs are appropriately scoped.


### Installation and Dependencies

- [ ] **Environment Setup**: Include setup instructions (e.g., `conda` environment file, `Dockerfile`).
- [ ] **Dependency Management**: Use virtual environments (e.g., `venv`, `conda`, `uv` for Python) to isolate dependencies.

---

# More Advanced Development

## Documentation

- [ ] **API Documentation**: Generate API documentation (e.g., `MkDocs` for Python or wiki pages in the repo). 
- [ ] **Docstrings**: Add comprehensive docstrings for all functions, classes, and modules. These can be incorporated to help generate documentation.
- [ ] **Example Scripts**: Include example scripts for common use cases.
- [ ] **Configuration Files**: Use `yaml`, `json`, or `ini` for configuration settings.


## Code Quality

- [ ] **Consistent Style**: Follow coding style guidelines (e.g., `PEP 8` for Python).
- [ ] **Linting**: Ensure the code passes a linter (e.g., `Ruff` for Python).
- [ ] **Logging**: Use logging instead of print statements for better debugging (e.g., `logging` in Python).
- [ ] **Error Handling**: Implement robust exception handling to avoid crashes.


## Testing

- [ ] **Unit Tests**: Write unit tests to validate core functionality.
- [ ] **Integration Tests**: Ensure components work together correctly.
- [ ] **Test Coverage**: Check test coverage
- [ ] **Continuous Integration (CI)**: Set up CI/CD pipelines (e.g., GitHub Actions) for automated testing.


## Code Distribution & Deployment

- [ ] **Packaging**: Provide installation instructions (e.g., `setup.py`, `hatch`, `poetry`, `uv` for Python).
- [ ] **Deployment Guide**: Document deployment procedures
