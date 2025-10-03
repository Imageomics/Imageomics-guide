# Helpful Tools for your Workflow

This page is dedicated to tools that can facilitate or improve project workflows. There are many available options to solve most of these challenges; these suggestions are based on tools used regularly within our community. If there's something you use regularly that you think should be on this list, please [suggest it](https://github.com/Imageomics/Imageomics-guide/issues)!

## Better Version Control for Notebooks

When working with Notebooks that may be re-run without changes to code, it's particularly hard in a collaborative setting to keep track of these changes&mdash;or lack thereof. [Jupytext](#jupytext) and [marimo](#marimo) are a couple of useful tools to address this challenge and improve the Notebook experience.

### Jupytext

If you use Jupyter Notebooks in your project (as many of us do), you may want to consider adding [Jupytext](https://jupytext.readthedocs.io/en/latest/) to your repertoire. [mwouts/jupytext](https://github.com/mwouts/jupytext) allows you to [pair](https://github.com/mwouts/jupytext#paired-notebooks) a Jupyter Notebook to a `.py` (or `.md`) file so that `git` renders clearer and more informative diffs, showing only the code and markdown cells that have been updated between commits.
This makes it easier to see the differences between versions as you work through your project. For instance, if you re-ran your notebook with just a new random seed, the diff in the commit would show that without reproducing the whole thing, and you could go look at the output in the notebook.

#### How it Works

Notebooks can be [paired](https://github.com/mwouts/jupytext#paired-notebooks) individually, or you can set a [global config](https://jupytext.readthedocs.io/en/latest/config.html) in your notebooks folder to generate a pairing automatically. Unfortunately, this automated pairing only works if you use Jupyter Lab (i.e., run notebooks through the terminal), not if you work in VS Code or other IDEs. [Manual pairing](https://github.com/mwouts/jupytext/blob/main/docs/faq.md#can-i-use-jupytext-with-jupyterhub-binder-nteract-colab-saturn-or-azure) code is given below.

##### Jupytext commands in terminal for VS Code

```bash
jupytext --set-formats ipynb,py:percent <notebook-name>.ipynb  # Pair a notebook to a py script
jupytext --sync <notebook-name>.ipynb             # Sync the two representations
```

##### But wait! ...There's another way to automate it!

There is a [jupytext pre-commit hook](https://jupytext.readthedocs.io/en/latest/using-pre-commit.html) that can be used to sync your paired files automatically when updating your GitHub repo. To learn more about pre-commit hooks in general, see the [git docs on pre-commit hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

### Marimo

[marimo](https://marimo.io/) functions similarly to a Jupyter Notebook, but has many built-in reproducibility and error-avoidance features, including the fact that it saves as a Python program (similar to the paired file created by [Jupytext](#jupytext)). See the summary in their [README](https://github.com/marimo-team/marimo?tab=readme-ov-file) or explore the [docs](https://docs.marimo.io/) to get started.

## Formatting and Linting

Have you found yourself saying, "I just need to clean up my code first"? Make this easier, and do it as you go, with linters! Additionally, formatting can impact code consistency and readability, while altering display of Markdown and generally adding noise version control diffs. [Ruff](#ruff) and [markdownlint](#markdownlint) are two tools designed to resolve this challenge, for Python and Markdown, respectively.

### Ruff

Fast _Python_ formatter and linter. You can install [astral-sh/ruff](https://github.com/astral-sh/ruff) with `pip install ruff` or `conda install ruff` in your virtual/conda environment. They also have extensions for [VS Code](https://github.com/astral-sh/ruff-vscode) and [other editors supporting LSP](https://github.com/astral-sh/ruff-lsp).

To format a file, run:

```bash
ruff format <path/to/file>
```

and to lint it run

```bash
ruff check <path/to/file>
```

Ruff can also be set up as part of a pre-commit hook or GitHub Workflow. See their [Usage section](https://github.com/astral-sh/ruff?tab=readme-ov-file#usage) for more information.

### Markdownlint

Fast _Markdown_ formatter and linter. We use the [DavidAnson/markdownlint](https://github.com/DavidAnson/markdownlint) package for this site; see instructions and example in the [linting section](https://github.com/Imageomics/Collaborative-distributed-science-guide/blob/main/CONTRIBUTING.md#linting) of our contributing guidelines. It is flexible in configuration and allows for simple checking or even fixing straight-forward formatting issues.

## FAIR Data Access and Validation

Don't add to the reproducibility crisis! Are you using existing data accessed through URLs and need to ensure consistency for re-use? Do you have a folder of images with all their metadata documented through their filenames? [Cautious Robot](#cautious-robot) and [Sum Buddy](#sum-buddy) are here to help.

### Cautious Robot

Simple image from CSV downloader. The [Imageomics/cautious-robot](https://github.com/Imageomics/cautious-robot) package provides a FAIR and Reproducible method for **downloading a collection of images from URLs**.

- Configurable wait time and max attempts for retry.
- Names images by given column with unique values.
- Logs all successful responses and errors for review after download.
- Uses [sum-buddy](#sum-buddy) to record checksums of all downloaded images.
- Performs minimal check that the number of expected images matches the number sum-buddy counts.

**Optional features:**

- Organize images into subfolders based on any column in CSV.
- Create square images for modeling:
    - Organizes images in a second directory (same format) with copies of images in specified size.
- **Buddy-check:** verifies all expected images downloaded intact (compares given checksums with sum-buddy output).

#### Sample Command

Given a CSV (`example.csv`) with a list of image URLs in a `file_url` column with `filename` providing unique IDs for each image, the following snippet will download these into an `example_images/` directory and validate the contents with provided MD5 hashes from the `md5` column of the CSV.

```console
cautious-robot --input-file example.csv --output-dir example_images -v "md5"
```

To download larger (10-100M image scale), more distributed datasets, to HPC systems please see [Imageomics/distributed-downloader](https://github.com/Imageomics/distributed-downloader).

### Sum Buddy

Simple and flexible checksum calculator, from a single file to an entire directory. The [Imageomics/sum-buddy](https://github.com/Imageomics/sum-buddy) package provides a FAIR and Reproducible method for **duplicate file identification**, efficient **metadata generation**, and general **file integrity and validation** support.

- Input: Folder with things to checksum.
- Output: CSV or printout of filepaths, filenames, and checksums.
- Options:
    - Ignore subfolders and patterns,
    - Hash algorithm to use,
    - Avoid hidden files and directories.
- Usage: Run as a CLI or with exposed Python methods.

#### Sample Use Case

Given a collection of images, e.g., in an `images/` directory, with no accompanying metadata, quickly generate a metadata file listing the filepaths, filenames, and checksums of all images contained in the folder. Note the option to include an "ignore file". This operates similarly to a `.gitignore`, allowing one to avoid inclusion of particular files or file types. In this case, let's assume there may be some `.doc` or similar included with the images. Hidden files and directories (e.g., `.DS_Store`) are ignored by default.

```console
sum-buddy --output-file metadata.csv --ignore-file .sbignore images/
```

The added benefit to this method of metadata CSV generation is the ability to quickly and easily check for duplicate images within a collection. See our [data training repo](https://github.com/Imageomics/data-workshop-AH-2024) to learn more about this subject.
