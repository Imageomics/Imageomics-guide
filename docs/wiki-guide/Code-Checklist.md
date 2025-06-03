# Code Checklist

This checklist provides an overview of essential and recommended elements to include in a GitHub repository to ensure that it conforms to FAIR principles and best practices for reproducibility. Along with the generation of a DOI (see [DOI Generation](DOI-Generation.md) and [Digital Products Release and Licensing Policy](Digital-products-release-licensing-policy.md)), following this checklist ensures compliance with the FAIR Principles for research software.[^1]
[^1]: Barker, M., Chue Hong, N. P., Katz, D. S., Lamprecht, A. L., Martinez-Ortiz, C., Psomopoulos, F., Harrow, J., Castro, L. J., Gruenpeter, M., Martinez, P. A., & Honeyman, T. (2022). Introducing the FAIR Principles for research software. _Scientific data_, 9(1), 622. [URL](https://doi.org/10.1038/s41597-022-01710-x).

!!! tip "Pro tip"

    Use the eye icon at the top of this page to access the source and copy the markdown for the checklist below into an issue on your GitHub [Repo](GitHub-Repo-Guide.md) or [Project](Guide-to-GitHub-Projects.md) so you can check the boxes as you add each element to your GitHub repository.

## Required Files

- [ ] **License**: Verify and include an appropriate license (e.g., `MIT`, `CC0-1.0`, etc.). See discussion in the [Repo Guide](GitHub-Repo-Guide.md/#license).
- [ ] **README File**: Following the [Repo Guide](GitHub-Repo-Guide.md/#readme), provide a detailed `README.md` with:
    - [ ] Overview of the project.
    - [ ] Installation instructions.
    - [ ] Basic usage examples.
    - [ ] Links to related/created dataset(s).
    - [ ] Links to related/created model(s).
    - [ ] Acknowledge source code dependencies and contributors.
    - [ ] Reference related datasets used in training or evaluation.
- [ ] **Requirements File**: Provide a [file detailing software requirements](GitHub-Repo-Guide.md/#software-requirements-file), such as a `requirements.txt` or `pyproject.toml` for Python dependencies.
- [ ] **Gitignore File**: GitHub has premade `.gitignore` files ([here](https://github.com/github/gitignore)) tailored to particular languages (eg., [R](https://github.com/github/gitignore/blob/main/R.gitignore) or [Python](https://github.com/github/gitignore/blob/main/Python.gitignore)), operating systems, etc.
- [ ] **CITATION CFF**: This facilitates citation of your work, follow guidance provided in the [Repo Guide](GitHub-Repo-Guide.md/#citation).

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

- [ ] **Repository Structure**: Ensure the code repository follows a clear and logical directory structure. (See [Repo Guide](GitHub-Repo-Guide.md/#general-repository-structure).)
- [ ] **Code Comments**: Include meaningful inline comments and function descriptions for clarity.
- [ ] **Random Seed Control**: Save seed(s) for random number generator(s) to ensure reproducible results.

## Security Considerations

- [ ] **Sensitive Data Handling**: Ensure no hardcoded sensitive information (e.g., API keys, credentials) are included in your repository. These can be shared through a config file on OSC.

!!! note
    The best practices described below will help you meet the above requirements. The more advanced development practices noted further down are included for educational purposes and are highly recommended&mdash;though these may go beyond what is expected for a given project, we advise collaborators to at least have a discussion about the topics covered in [Code Quality](#code-quality) and whether other practices discussed would be appropriate for their project.

---

## Best Practices

The [Repo Guide](GitHub-Repo-Guide.md/) provides general guidance on repository structure, [collaborative workflow](The-GitHub-Workflow.md/), and [how to make and review pull requests (PR)](The-GitHub-Pull-Request-Guide.md/). Below, we highlight some best practices in checklist form to help you meet the requirements described above for a FAIR and Reproducible project.

### Reproducibility

- **Version Control**: Use Git for version control and commit regularly.
- **Modularization**: Structure code into reusable and independent modules.
- **Code Execution**: Provide Notebooks to demonstrate how to reproduce results.

### Code Review & Maintenance

- **Code Reviews**: Regular peer reviews for quality assurance. Refer to the [GitHub PR Review Guide](The-GitHub-Pull-Request-Guide.md/#2-review-a-pull-request).
- **Issue Tracking**: Use GitHub issues for tracking bugs and feature requests.
- **Versioning**: Tag releases, changelogs can be auto-generated and informative when PRs are appropriately scoped.

### Installation and Dependencies

- [ ] **Environment Setup**: Include setup instructions (e.g., `conda` environment file, `Dockerfile`).
- [ ] **Dependency Management**: Use virtual environments and the frameworks that manage them (e.g., `venv`, `conda`, `uv` for Python) to isolate dependencies.

---

## More Advanced Development

### Documentation

- [ ] **API Documentation**: Generate API documentation (e.g., [`MkDocs`](https://www.mkdocs.org) for Python or wiki pages in the repo).
- [ ] **Docstrings**: Add comprehensive docstrings for all functions, classes, and modules. These can be incorporated to help generate documentation. Note that generative AI tools with access to your code, such as GitHub Copilot, can be quite accurate in generating these, especially if you are using type annotations. 
- [ ] **Example Scripts**: Include example scripts for common use cases.
- [ ] **Configuration Files**: Use `yaml`, `json`, or `ini` for configuration settings.

### Code Quality

- [ ] **Consistent Style**: Follow coding style guidelines (e.g., `PEP 8` for Python).
- [ ] **Linting**: Ensure the code passes a linter (e.g., `Ruff` for Python).
- [ ] **Logging**: Use logging instead of print statements for better debugging (e.g., `logging` in Python).
- [ ] **Error Handling**: Implement robust exception handling to avoid crashes or bogus results from input outside of code expectations.

### Testing

- [ ] **Unit Tests**: Write unit tests to validate core functionality.
- [ ] **Integration Tests**: Ensure components work together correctly.
- [ ] **Test Coverage**: Check test coverage, e.g., using [Coverage](https://coverage.readthedocs.io/).
- [ ] **Continuous Integration (CI)**: Set up CI/CD pipelines (e.g., [GitHub Actions](https://docs.github.com/en/actions)) for automated testing.

### Code Distribution & Deployment

- [ ] **Packaging**: Provide installation instructions (e.g., `setup.py`, `hatch`, `poetry`, `uv` for Python).
- [ ] **Deployment Guide**: Document deployment procedures

!!! question "[Questions, Comments, or Concerns?](https://github.com/Imageomics/Imageomics-guide/issues)"
