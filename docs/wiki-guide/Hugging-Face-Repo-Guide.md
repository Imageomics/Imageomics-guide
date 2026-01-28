# Hugging Face Repo Guide

Need a repository to store your data or model? You've come to the right place! Below we have compiled guidance on conventions and best practices for maintaining a shared (or shareable) Hugging Face repository of your work.

## Setting up a New Organization Repository

### Standard Files

For each repository, include the following files and metadata in the root directory as soon as possible; a license can (and should) be instantiated with the Dataset or Model card (`README.md`), and the standard `.gitattributes` will be generated for you. On the [Imageomics HF](https://huggingface.co/imageomics) select `New` and pick which type of repository you need.

- [README.md](#readme)
- [License](#license)
- [.gitignore](#gitignore)
- [.gitattributes](#gitattributes)

!!! note
    Hugging Face does not support the use of a `CITATION.cff`. Instead, citation guidance is provided in the Citation Section of the [Dataset](HF_DatasetCard_Template_mkdocs.md) or [Model](HF_ModelCard_Template_mkdocs.md) card. When [generating a DOI on Hugging Face](DOI-Generation.md##1-generate-a-doi-on-hugging-face), author names must be added manually in the intended order for them to be displayed in the DOI "Cite this dataset" link.

#### README

The README.md file is generally referred to as either a Dataset or Model Card and is what everyone will notice first when they open your repository on Hugging Face. Choose the appropriate Imageomics-specific HF template ([model](HF_ModelCard_Template_mkdocs.md) or [dataset](HF_DatasetCard_Template_mkdocs.md)) to get started. Be sure to include a brief description and as much information as possible at the beginning. You can update this file as you go, so don't remove the recommended sections prior to completion. The templates include descriptions of many fields, Imageomics grant information, citation formatting, and some notes on HF-flavored markdown to get you started.

Once you've created your repo, populate your README (you can do this online by selecting "Create Dataset/Model Card" and pasting in the appropriate Imageomics HF template, then filling in your info). Editing your README in the browser allows you to preview the formatting of the file before committing changes.

#### License

##### 1. Select a license

Alongside the appropriate stakeholders, select a license following the guidelines set forth in the [Digital Products Release and Licensing Policy](Digital-products-release-licensing-policy.md). For Datasets, this would be public domain or terms no more restrictive than requiring attribution (e.g., [CC-BY](https://creativecommons.org/licenses/by/4.0/)); Models and Spaces should be released under a license that is [Open Source Initiative](https://opensource.org/licenses) (OSI) compliant.

!!! note "Remember"
    A public repository on Hugging Face with no license can be viewed and accessed by others, but unless the author associates a license, it is unclear what others are allowed to do with it legally. Adding an OSI license can help others feel comfortable building off your work!

For more information on how to choose a license and why it matters, see [Choose A License](https://choosealicense.com). Keep in mind that your available license options may also be limited by your data sources or base model. Data should not be republished where not explicitly warranted or required.[^1]

[^1]: For instance, when working with images aggregated from multiple sources, a catalog of all images used with URLs to access the images and download instructions ([cautious-robot](Helpful-Tools-for-your-Workflow.md#cautious-robot) can help with this) respects the original source data producers interests. However, if you have processed the images in a resource-intensive pipeline and the image licenses allow, the _processed_ images should be published for ease of re-use. In this case, it is important to provide the citation for the source data as well.

##### 2. Add a license to the repository

Once a license has been chosen (if not initialized with one), add the appropriate license identifier in the `yaml` portion of the README (the web UI generates a dropdown of recommendations under "Edit dataset/model card", [license identifiers](https://huggingface.co/docs/hub/en/repositories-licenses)).

!!! note
    Unlike in GitHub, a `LICENSE.md` file is not supported. Instead, the license for the digital object is added through the `yaml` (for ease of API access) and further clarifications can be included in the License Section of the [Dataset](HF_DatasetCard_Template_mkdocs.md) or [Model](HF_ModelCard_Template_mkdocs.md) card.

#### gitignore

As with GitHub, the `.gitignore` file is an important tool for maintaining a clean repository by ensuring that git will not track temp files of any and all your collaborators (no pesky `pycache` or `.DS_Store` files floating around).

The same [options for GitHub](https://github.com/github/gitignore) are usable here, and if you or anyone on your team uses a Mac (or if you intend to encourage outside collaboration on this repo), add

```
# Mac system
.DS_Store
```

at the end of the `.gitignore` file.

#### gitattributes

The `.gitattributes` file determines file patterns to be tracked by [`git LFS`](https://git-lfs.com/) (Git Large File Storage). The preset `gitattributes` file includes many binary file types, but you may need to add particular files if they get too large (eg., a large CSV, but do **NOT** store all CSV files with `git LFS`, just add the particular one or pattern). Pattern-matching can be done using `*`. You can either add the file (and appropriate pattern description) to the `.gitattributes` file, or add it in the command line:

```
git lfs track "my-big-list.csv"
```

Then add and commit the `.gitattributes` file as described below.

## Hugging Face Pull Requests With Local Edits

Hugging Face also has a pull request (PR) feature, though the process is a bit different from GitHub.

As with GitHub, you can interact through the web browser or a command line interface (eg., terminal on Mac). However, instead of the `create new branch` option, there is a `create new pull request` option. It is still preferable to avoid committing everything directly to main. To make further changes to the particular PR created on the browser, one must first clone the repo:

```
git clone <repo-url> 
```

Then, navigate to that folder `cd <repo-name>`, and fetch the PR files:

```
git fetch origin refs/pr/<PR#>:pr/<PR#>
git checkout pr/<PR#>
```

You can then make your updates, add and commit them, then push those back to the remote. Note that the push is the one line that differs from GitHub and must be used each time:

```
git add <changed files>
git commit -m "<change>"
git push origin pr/<PR#>:refs/pr/<PR#>
```

For more information on Hugging Face Pull Requests and Discussions, see their [documentation](https://huggingface.co/docs/hub/repositories-pull-requests-discussions).

## Templates for Model and Dataset Cards

See [About Templates](About-Templates.md) for guidelines on using templates for these important pieces of documentation.
