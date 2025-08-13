# Hugging Face Repo Guide

Need a repository to store your data or model? You've come to the right place! Below we have compiled guidance on conventions and best practices for maintaining a shared (or shareable) Hugging Face repository of your work.

## Setting up a New Organization Repository

### Standard Files

For each repository, include the following files in the root directory as soon as possible; a license can (and should) be instantiated when you create a new repository, and the standard `.gitattributes` will be generated for you. On the [Imageomics HF](https://huggingface.co/imageomics) select `New` and pick which type of repository you need.

- [README.md](#readme)
- [LICENSE.md](#license)
- [.gitignore](#gitignore)
- [.gitattributes](#gitattributes)

#### README

The README.md file is generally referred to as either a Dataset or Model Card and is what everyone will notice first when they open your repository on Hugging Face. Choose the appropriate Imageomics-specific HF template ([model](HF_ModelCard_Template_mkdocs.md) or [dataset](HF_DatasetCard_Template_mkdocs.md)) to get started. Be sure to include a brief description and as much information as possible at the beginning. You can update this file as you go, so don't remove the recommended sections prior to completion. The templates include descriptions of many fields, Imageomics grant information, citation formatting, and some notes on HF-flavored markdown to get you started.

Once you've created your repo, populate your README (you can do this online by selecting "Create Dataset/Model Card" and pasting in the appropriate Imageomics HF template, then filling in your info). Editing your README in the browser allows you to preview the formatting of the file before committing changes.

#### LICENSE

##### 1. Select a license

Alongside the appropriate stakeholders, select a license that is [Open Source Initiative](https://opensource.org/licenses) (OSI) compliant.

!!! note "Remember"
    A public repository on Hugging Face with no license can be viewed and accessed by others, but unless the author associates a license, it is unclear what others are allowed to do with it legally. Adding an OSI license can help others feel comfortable building off your work!

For more information on how to choose a license and why it matters, see [Choose A License](https://choosealicense.com) and [A Quick Guide to Software Licensing for the Scientist-Programmer](https://doi.org/10.1371/journal.pcbi.1002598) by A. Morin, et al.

##### 2. Add LICENSE.md to the repository

Once a license has been chosen (if not initialized with one), add the appropriate license label in the `yaml` portion of the README (the web UI generates a dropdown of recommendations under "Edit dataset/model card").

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
