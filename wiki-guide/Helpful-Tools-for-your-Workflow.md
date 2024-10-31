This page is dedicated to tools that can facilitate or improve project workflows. If there's something you use regularly that you think should be on this list, please suggest it!

## Jupytext

If you use Jupyter Notebooks in your project (as many of us do), you may want to consider adding [Jupytext](https://jupytext.readthedocs.io/en/latest/) to your repertoire. [Jupytext](https://github.com/mwouts/jupytext) allows you to [pair](https://github.com/mwouts/jupytext#paired-notebooks) a Jupyter Notebook to a `.py` (or `.md`) file so that `git` renders clearer and more informative diffs, showing only the code and markdown cells that have been updated between commits.
This makes it easier to see the differences between versions as you work through your project. For instance, if you re-ran your notebook with just a new random seed, the diff in the commit would show that without reproducing the whole thing, and you could go look at the output in the notebook.

### How it Works

Notebooks can be [paired](https://github.com/mwouts/jupytext#paired-notebooks) individually, or you can set a [global config](https://jupytext.readthedocs.io/en/latest/config.html) in your notebooks folder to generate a pairing automatically. Unfortunately, this automated pairing only works if you use Jupyter Lab (i.e., run notebooks through the terminal), not if you work in VS Code or other IDEs. [Manual pairing](https://github.com/mwouts/jupytext/blob/main/docs/faq.md#can-i-use-jupytext-with-jupyterhub-binder-nteract-colab-saturn-or-azure) code is given below.

#### Jupytext commands in terminal for VS Code:
```bash
jupytext --set-formats ipynb,py:percent <notebook-name>.ipynb  # Pair a notebook to a py script
jupytext --sync <notebook-name>.ipynb             # Sync the two representations
```

#### But wait! ...There's another way to automate it!
There is a [jupytext pre-commit hook](https://jupytext.readthedocs.io/en/latest/using-pre-commit.html) that can be used to sync your paired files automatically when updating your GitHub repo. To learn more about pre-commit hooks in general, see the [git docs on pre-commit hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).



## Ruff

[Ruff](https://github.com/astral-sh/ruff) is a fast python formatter and linter. You can install it with `pip install ruff` or `conda install ruff` in your virtual/conda environment. They also have extensions for [VS Code](https://github.com/astral-sh/ruff-vscode) and [other editors supporting LSP](https://github.com/astral-sh/ruff-lsp).

To format a file, run:
```bash
ruff format <path/to/file>
```
and to lint it run
```bash
ruff check <path/to/file>
```

Ruff can also be set up as part of a pre-commit hook or GitHub Workflow. See their [Usage section](https://github.com/astral-sh/ruff?tab=readme-ov-file#usage) for more information.

