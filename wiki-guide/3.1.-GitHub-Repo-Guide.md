# GitHub Repo Guide

Just joining or starting a new project and need a repository to store your work? You've come to the right place! Below we have compiled guidance on conventions and best practices for maintaining a shared (or shareable) repository of your work.


# Setting up a New Organization Repository

**Note:** We recommend doing development in a public repo, or at least publishing the repo in which development was done at the time of publication/release. However, if you're looking to have a public-facing repo _and_ a private repo for development, please be sure to read our guidance on the [Two Repo Problem](Two-Repo-Problem.md) before proceeding.

## Standard Files
For each repository, include the following files in the root directory as soon as possible; they can (and should) be instantiated when you create a new repository. 
* [README.md](#readme)
* [LICENSE.md](#license)
* [.gitignore](#gitignore)
* [software requirements](#software-requirements-file)

More [recommendations](#recommended-files) are discussed below.

### README
The README.md file is what everyone will notice first when they open your repository on GitHub. When creating your repo be sure to include a brief description, as this will populate the `About` field in the top right of your repo, as well as start your README with some text. 

Once you've created your repo, populate your README (you can do this by clicking on the file "README.md", then clicking the pencil at the top left to edit). Editing your README in the browser allows you to preview the formatting of the file before committing changes. The content of your README may vary based on the purpose or goal of your repo, but there are key elements that should always be included.

* Summary of the repo:
    * This could be a simple explanation of what the package or tool developed in your repo is intended to do,
    * Or an abstract describing your research.
* Detailed documentation on how to access and use the project software (User Guide).  
    * Including installation of [dependencies](#dependencies-and-environments).
    * If your tool requires input be in a particular format, this would be included in the README. It would also help to include an example file demonstrating the format. 
* Information about the sources you've used (links and what they were used for), such as:
    * Tools from other repos
    * Data for analysis

For more inspiration on making an awesome README, check out [this list](https://github.com/matiassingers/awesome-readme).

### LICENSE
#### 1. Select a license.
Alongside the appropriate stakeholders, select a license that is [Open Source Initiative](https://opensource.org/licenses) (OSI) compliant.

*Remember, a public repository on GitHub with no license can be viewed and forked by others under GitHub's ToS, but unless the author associates a license, it is unclear what others are allowed to do with it legally. Adding an OSI license can help others feel comfortable contributing!*

For more information on how to choose a license and why it matters, see [Choose A License](https://choosealicense.com) and [A Quick Guide to Software Licensing for the Scientist-Programmer](https://doi.org/10.1371/journal.pcbi.1002598) by A. Morin, et al.

#### 2. Add LICENSE.md to the repository.
Once a license has been chosen, add a LICENSE.md file to the root of the repository. An easy way to do this is using a GitHub-provided [license template](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository). Do not forget to update necessary fields in the template. 

### GITIGNORE
The `.gitignore` file is an important tool for maintaining a clean repository by ensuring that git will not track temp files of any and all your collaborators (no pesky `pycache` or `.DS_Store` files floating around). 

GitHub has premade `.gitignore` files which can be selected from a dropdown when creating a repo. They are available for review [here](https://github.com/github/gitignore) and are generally tailored to particular languages (eg., [R](https://github.com/github/gitignore/blob/main/R.gitignore) or [Python](https://github.com/github/gitignore/blob/main/Python.gitignore)), operating systems, etc. The initial choice can be updated as needed. In particular, we recommend selecting a template based on the primary language used for your work. 

If you or anyone on your team uses a Mac (or if you intend to encourage outside collaboration on this repo), add 
```
# Mac system
.DS_Store
```
at the end of the `.gitignore` file.

### Software Requirements File
It is also advisable to include a machine-readable file with minimal software requirements for your project. For Python projects, this often takes the form of a `requirements.txt` file containing the packages and their versions that were used (eg., `pandas==2.0.1`). If you use `conda`, you may instead opt for an `environment.yml`. These are essential to ensuring the reproducibility and interoperability of your work (by yourself and others). Note that they should _**not**_ be listed in the README.

For more information on managing these environments and generating such files programmatically, see the wiki entry [Virtual Environments](Virtual-Environments.md). 

## Recommended Files

Though the following files are not included in every repository and do not have a simple selection process integrated into GitHub, they are extremely important (if not essential) to maintaining FAIR principles and reproducibility in projects, as well as ensuring proper attribution for your work.

### CONTRIBUTING
If you are looking to open your project to more public contributions, it is a good idea to include contributing guidelines. This could take the form of a "CONTRIBUTING.md" file or a subsection of your README.

Contributing guidelines are important to maintain consistency across the way people work on a project. It is important to establish conventions about the important things while avoiding excessive constraints and bureaucracy that would make contributing a pain. Important things include efficient and effective communication.

### CITATION
Make it easier for people to cite your project by including a [CITATION.cff file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files); you can copy-paste the template below.

As with journal publications, we expect to be cited when someone uses our code. To facilitate proper attribution, GitHub will automatically read a [CITATION.cff file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) and display a link to "cite this repository". Providing this file is as simple as filling your information into one of their example files and uploading it to your repo. More examples and information about the Citation File Format can be found on the [citation-file-format repo](https://github.com/citation-file-format/citation-file-format), including helpful [related tools](https://github.com/citation-file-format/citation-file-format#tools-to-work-with-citationcff-files-wrench).

You can check your CITATION.cff file prior to upload using this [validator tool](https://www.yamllint.com/).

**Note:** 
- Subcategories of `preferred-citation` do not get bullet points, but the first subcategory of `references` must be bulleted (as below).
- This is generally intended as a reference for your code. Preferred citation can be used for the paper, though it is better to ask in the `README` that someone cites _both_ and provide the paper reference there (only the `preferred-citation` will show up to be copied from the citation box if it is included).
```yaml
abstract: "<describe your code/package>"
authors:
- family-names:
  given-names: "<First M.I.>"
  orcid: "https://orcid.org/<ORCID #>"
cff-version: 1.2.0
date-released: "YYYY-MM-DD"
identifiers:
  - description: "The GitHub release URL of tag <version>."
    type: url
    value: "https://github.com/Imageomics/<repo>/releases/tag/<tag-name>"
  - description: "The GitHub URL of the commit tagged with <tag-name>."
    type: url
    value: "https://github.com/Imageomics/<repo>/tree/<commit-hash>"
keywords:
  - imageomics
license:
message: "If you find this software helpful in your research, please cite both the software and our paper."
repository-code: "https://github.com/Imageomics/<repo>"
title: "<repo title>"
version: <release version>
doi: <DOI from Zenodo>
type: software
preferred-citation:
  type: article
  authors:
    - family-names:
      given-names:
    - family-names:
      given-names:
  title: 
  year:
  journal:
  doi: 
references:
  - authors:
      - family-names:
        given-names:
      - family-names:
        given-names:
    title: 
    version:
    type:
    doi: 
    date-released:
```

## Additional Considerations

### Formatting and Naming Conventions
* Dates and Times: For interoperability and avoiding ambiguity, [dates and times should be reported](https://dataoneorg.github.io/Education/bestpractices/describe-formats-for) in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601).
  - For dates, this means `YYYY-MM-DD` (for ISO 8601 compliance, the dashes are required).
  - For times, use `THHMMSS` in 24-hour format. 
  - For example, the moment when there were 60 seconds left before New Year 2000 would be 1999-12-31T235900.
* Branches 
  * Primary branch: `main`
  * Other branches: follow the pattern `category/reference/description`
    * category: `feature`, `bugfix`, `experiment`
      * `feature` is for new functionality
      * `bugfix` is for fixing errors
      * `experiment` is for more open-ended
    * the associated issue (if no issue, put no-ref), formatted as `issue-NN`
    * description: brief description, e.g. `solve-world-hunger`
  * e.g. `git branch feature/issue-1/general-ai`
* Commits: to combine human- and computer-readability into commit messages, follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/#summary).

### Workflow
Do not conduct routine work in the `main` branch. Only do one thing on a branch at a time. Prune a branch once its purpose is fulfilled and it is merged (i.e., delete it). 

For more information on creating, merging, and deleting branches, see the [GitHub Workflow Guide](2.1.-The-GitHub-Workflow.md).
  
## General Repository Structure
In addition to the [standard files](#standard-files) recommended for every repo, you will likely have some code, notebooks, and data. For an easily accessible and readable repo, it is good to organize these files within a clear directory (folder) structure, such as

```
Project_Directory
    - scripts
    - notebooks
    - src
    - data
```
    
**Note:** Depending on the size of your data, `data` may only be local on your machine in which case it is good to include instructions to access the data where appropriate.



***



# Working on GitHub
After the initial creation of a repo on the GitHub website, there are two primary modes of interacting with it. 

1. Through git on the Command Line

    This requires a `bash` or `zsh` shell on your computer. On Mac you can use terminal, while Windows requires installing git and a bash emulator.
    
2. Through the GitHub Desktop App, [GitHub Desktop](https://desktop.github.com/)

    GitHub provides documentation to get started on [Mac](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop?platform=mac) or [Windows](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop?platform=windows), as well as extensive documentation on use cases we discuss throughout the wiki [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop).
    
    **Note:** The bulk of our step-by-step guides will outline interaction through the command line, but the same principles apply to using GitHub Desktop. 
    
## Cloning a Repository

Navigate to the main ("<> Code") page of your repository and click the green button at the top right corner (as shown below) and copy the link (for command line) or select "Open with GitHub Desktop". For command line interaction, navigate within the `bash` shell to the directory where you would like to place your local copy of the repo (`cd <folder_name>`), then clone the repo into that folder (`git clone <repo_url>`), this will generate a local copy of the repo on your computer.

![Screenshot 2023-05-16 at 5 22 25 PM](https://github.com/Imageomics/internal-guidelines/assets/38985481/43857a4d-789b-4073-b872-da29c4474916)

If you would like a specific branch, use `git clone -b <branch_name> <repo_url>`.

## Workflow Summary
Generally, repositories are organized around an Imageomics Project/Topic/Team, eg., butterflies. These broader topics may contain various projects organized under a GitHub [Team](https://github.com/orgs/Imageomics/teams) focused on that topic. Both [projects](https://github.com/orgs/Imageomics/projects?query=is%3Aopen) and [repositories](https://github.com/orgs/Imageomics/repositories) may be linked to teams, providing an organizational structure upon which to plan and manage tasks while maintaining a clear link/connection to the work being done on those tasks. Note that a project may encapsulate multiple repositories just as a repository may be referenced by multiple projects.

Ideally, each task will be linked to an issue in the relevant repository. Team members may then be assigned tasks, and asynchronous discussions about the task can be recorded on its issue page in the repository. To accomplish the task, a new branch should be created following the [branch naming conventions](#formatting-and-naming-conventions); do not work directly on the `main` branch. Once the task is completed, a pull request can be opened to merge the changes into the main branch (see the [GitHub Workflow Guide](2.1.-The-GitHub-Workflow.md) and the [PR Guide](2.1.2-The-GitHub-Pull-Request-(PR)-Guide.md) for more details on this process). Reviewers may be assigned to each pull request to ensure compatibility and that the proposed solution functions as expected/needed; this is an opportunity for more dialogue. 


