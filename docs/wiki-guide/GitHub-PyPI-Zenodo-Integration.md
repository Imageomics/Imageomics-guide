# PyPI & Zenodo Release Automation

This page is a quick reference for setting up a repository to automatically release to the [Python Package Index (PyPI)](https://pypi.org/) and [Zenodo](https://zenodo.org/) on a GitHub release. At the bottom of the page are [checklists](#release-checklist) for first-time releases, new releases, and post-release steps. These are set up to be copied into a relevant issue on your GitHub repository for easier tracking.

!!! warning
    Before setting a release, please review the [Digital Product Policy](About-Digital-Product-Policies.md) and check your repository against the [Code Repo Checklist](Code-Checklist.md).

!!! note
    Steps marked with an `*` need only be completed once (the first time this is set up).

## Before Generating a Release

### Set version in... <!-- markdownlint-disable-line MD026 -->

- `__about__.py` file
    - Version should be set *dynamically* in the `pyproject.toml` from this file.*
- [`CITATION.cff`](GitHub-Repo-Guide.md#citation-templates)
- [`.zenodo.json`](GitHub-Repo-Guide.md#zenodo-metadata)

### Add/Update Citation and Zenodo Metadata Files

Review or create both a [`CITATION.cff`](GitHub-Repo-Guide.md#citation) and [`.zenodo.json`](GitHub-Repo-Guide.md#zenodo-metadata) file following guide instructions. Be sure to include

!!! tip "Pro tip"
    Add this [test to validate the Zenodo metatdata file](https://github.com/Imageomics/Collaborative-distributed-science-guide/blob/main/.github/workflows/validate-zenodo.yaml). It will run whenever the `.zenodo.json` or workflow file are edited, ensuring that your Zenodo integration will run smoothly.

Before release, ensure that...

- All authors are included and appropriately ordered.
    - This list may or may not change, and may differ from an associated paper author list, as discussed in the [Digital Product Lifecycle](Digital-Product-Lifecycle.md#exploration-phase) and the [Imageomics Author Guide](https://docs.google.com/spreadsheets/d/1GwlCukfoQPL8JI2yyWRD3g4uiMTO3tlGNE_qeb_xBCs/edit?usp=sharing).
- All project keywords are listed, using quotes for multi-word tags.
- The release date in both files is correct.

    !!! info
        This should be added in a PR as the last commit before a release, but check that the date matches, since these PRs may not necessarily be merged on the same day they are created.

- Set [citation file identifiers](GitHub-Repo-Guide.md#__codelineno-1-8):
    - Version tag link should match the updated version. The commit hash of the version will be filled in *after* release.
    - DOI should be the *general software* DOI from Zenodo to avoid mis-matched version confusion (since it must be added ***after*** release).*

        !!! note
            If you have not generated a release yet, then leave the `doi` key commented out; it will be added **after** release.

### Automate publish to PyPI on release*

Complete all steps below to automatically publish releases to PyPI. These steps need only be completed once before the first release; only dependencies and other keys in the `pyproject.toml` may need updating over time.

- Set up a [`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) with your project repo information and dependencies.
    - Include your project keywords in `pyproject.toml` (no spaces, even within quotes).
    - Version in `pyproject.toml` set *dynamically*.
- Add PyPI publication workflow*. See [pybioclip workflow](https://github.com/Imageomics/pybioclip/blob/main/.github/workflows/publish-to-pypi.yml) as an example.[^1]
    - For this to work on upload, you must configure GitHub as a "pending" publisher on PyPI. See PyPI's ["pending" publisher docs](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) for instructions.

### Update `README` Installation Instructions*

Update the installation instructions in the `README` to `pip install <package-name>` instead of `pip install git+<GitHub URL>` right before the release and concurrent PyPI publication.

### Turn Repository Sync on in your Zenodo Account*

This must be set specifically for the target repo. See [Automatic DOI Generation with Zenodo](DOI-Generation.md#automatic-generation) for more information.

## After a Release is Generated

There are a few updates required after generating a release, though the last listed here is the only one that is required for each release.

- Add DOI badge to `README`*.
    - Make sure to use the *version-agnostic* DOI, used to reference all releases. The badge display will then auto-update with each release to match the DOI of *that* release.
    - See [Add a Zenodo DOI Badge](DOI-Generation.md#add-a-zenodo-doi-badge) for instructions.
- Add PyPI badges to `README`*.
- Add *version-agnostic* DOI to `CITATION.cff`*.
- Add release commit hash to `CITATION.cff` [identifiers](GitHub-Repo-Guide.md#__codelineno-1-8).

## Release Checklist

!!! tip "Pro tip"

    Copy the markdown for the relevant checklist below into an issue on your GitHub [Repo](GitHub-Repo-Guide.md) or [Project](Guide-to-GitHub-Projects.md) so you can check the boxes as you complete each step to genearate a release for your GitHub repository.

=== "First Release"

    ```Markdown
    ### Set version in... 
    - [ ] `__about__.py` file (the only repeated PyPI update).
      - Version should be set *dynamically* in the `pyproject.toml` from this file.*
    - [ ] [`CITATION.cff`](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#citation-templates).
    - [ ] [`.zenodo.json`](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#zenodo-metadata).
    
    ### Add/Update the [citation](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#citation) and [Zenodo metadata](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#zenodo-metadata) files.
    
    Ensure that...
    - [ ] All authors are included and appropriately ordered.
      - This list may or may not change, and may differ from an associated paper author list, as discussed in the [Digital Product Lifecycle](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/Digital-Product-Lifecycle/#exploration-phase) and the [Imageomics Author Guide](https://docs.google.com/spreadsheets/d/1GwlCukfoQPL8JI2yyWRD3g4uiMTO3tlGNE_qeb_xBCs/edit?usp=sharing).
    - [ ] All project keywords are listed, using quotes for multi-word tags.
    - [ ] The release date in both files is correct.
    > [!IMPORTANT]
    > This should be added in a PR as the last commit before a release, but check that the date matches, since these PRs may not necessarily be merged on the same day they are created.
    - Set [citation file identifiers](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#__codelineno-1-8):
      - [ ] Version tag link should match the updated version. The commit hash of the version will be filled in *after* release.
    > [!NOTE]
    > You have not generated a release yet, so leave the `doi` key commented out; it will be added **after** release.
    - [ ] Add [test to validate Zenodo file](https://github.com/Imageomics/Collaborative-distributed-science-guide/blob/main/.github/workflows/validate-zenodo.yaml).*

    ### Automate publish to PyPI on release:
    - [ ] Set up a [`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) with your project repo information and dependencies.
      - [ ] Include your project keywords in `pyproject.toml` (no spaces, even within quotes).
      - [ ] Version in `pyproject.toml` set *dynamically*.
    - [ ] Add PyPI publication workflow*. See [pybioclip workflow](https://github.com/Imageomics/pybioclip/blob/main/.github/workflows/publish-to-pypi.yml) as an example.[^1]
      - [ ] Configure GitHub as a "pending" publisher on PyPI. See PyPI's ["pending" publisher docs](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) for instructions.*
    
    ### Update installation instructions to reflect imminent release and PyPI publication:*
    - [ ] `pip install <package-name>` instead of `pip install git+<GitHub URL>`.
    
    ### Zenodo Sync
    - [ ] Turn on repository sync in your Zenodo account; this must be set specifically for the target repo. See [Automatic DOI Generation with Zenodo](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/DOI-Generation/#automatic-generation) for more information.
    ```

=== "New Release"

    ```Markdown
    ### Set version in... 
    - [ ] `__about__.py` file (the only repeated PyPI update).
      - Version should be set *dynamically* in the `pyproject.toml` from this file.*
    - [ ] [`CITATION.cff`](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#citation-templates).
    - [ ] [`.zenodo.json`](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#zenodo-metadata).
    
    ### Update the [citation](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#citation) and [Zenodo metadata](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#zenodo-metadata) files. 
    
    Ensure that...
    - [ ] All authors are included and appropriately ordered.
    - [ ] All project keywords are listed, using quotes for multi-word tags.
    - [ ] The release date in both files is correct.

    > [!IMPORTANT]
    > This should be added in a PR as the last commit before a release, but check that the date matches, since these PRs sometimes are not merged on the day they are created.

    - [ ] Set version tag in [citation file identifiers](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#__codelineno-1-8) to match the updated version. The commit hash of the version will be filled in *after* release.
    ```

=== "After First Release"
    ```Markdown
    - [ ] Add *version-agnostic* DOI badge to `README`*.
        - See [Add a Zenodo DOI Badge](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/DOI-Generation/#add-a-zenodo-doi-badge) for instructions.
    - [ ] Add PyPI badges to `README`*.
    - [ ] Add *version-agnostic* DOI to `CITATION.cff`*.
    - [ ] Add release commit hash to `CITATION.cff` [identifiers](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#__codelineno-1-8).
    ```

=== "After Release"

    ```Markdown
    - [ ] Add release commit hash to `CITATION.cff` [identifiers](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#__codelineno-1-8).
    ```

[^1]: Note that this follows the [PyPI Trusted Publishers docs](https://docs.pypi.org/trusted-publishers/using-a-publisher/) to remove the need for a token, though you must first configure GitHub as a ["pending" Trusted Publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) for the project on PyPI.
