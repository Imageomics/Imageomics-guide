# Command Line Cheat Sheet
<!-- Disable rule for in-line HTML; it is needed for better table formatting and brackets aren't recognized as being in a code block by the linter on this page. -->
<!-- markdownlint-disable MD033 -->
See also [GitHub's Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

## Useful bash and git

<!-- The pipe in the final row of this column isn't recognized as being in a code block by the linter
     so this rule must be ignored here to avoid errors -->
<!-- markdownlint-disable MD056 -->
| Command | Action |
| --- | --- |
| `<cmd> -h` |          print the help documentation for a command, showing usage information and options |
| `cd`	|		change directory |
|`cd ..` |		up one directory |
| `pwd` | 		current working directory |
| `ls` | 		list everything in current directory (use `-a` to also show **a**ll files including hidden, `-l` for a **l**ong list including permissions and ownership info, `-1` ("dash one") to display the output with **1** item on each line) |
| `wc -l <file>` |      use the **w**ord **c**ount command with the `-l` **l**ines option to list the number of lines in a file |
| `du <dirname>/`|      calculate and show how much **d**isk **u**sage is consumed by a directory (use `-h` to make it **h**uman-readable, i.e. report in MB, GB or whatever units are most appropriate, and `-s` for **s**ummary of all the contents together rather than each item individually) |
| ++ctrl+r++ |		search for command (will pop up `bck-i-search:`) |
| `rm <target>` |       remove a file (or folder with `-r`). Beware when using `rm -rf <folder>` to **f**orce the **r**ecursive removal of all contents in a folder, which cannot be undone unless there is a backup. |
| `<cmd1> | <cmd2>` |   The "pipe" operator (++pipe++) feeds the output of the first command (`cmd1`) to the input of the second command (`cmd2`). For example, show the total number of files in a directory with `ls -1 <dir> | wc -l` |
<!-- markdownlint-enable MD056 -->

### Git-Specific

| Command | Action |
| --- | --- |
| `git log`   | 		list of commits with author, date, time (type `q` to leave) |
| `git log --oneline` | 		list of just commits (ID, location, message), type `q` to leave |
| `git status`  | 	status of local vs remote repo (commits, ignored files, etc), <br> shows changed files that git is tracking and that git is not tracking   |
| `git rm <target>`   | 		remove file (or folder with `-r`) from repo and filesystem (or just from the repo and not filesystem with `--cached`) <br>cache file ex: `git rm -r --cached __pycache__` |
| `git mv <file> <folder>`   | 			move file to folder <br>or rename: `git mv <filename> <new_filename>` |
| `git branch`   | 				list branches, current branch has `*` in front and is green |
| `git checkout -b <branch>`   | 		create new branch and check it out |
| `git checkout <branch>`   |			checkout branch |
| `git branch -d <branch>`   | 			delete branch |

!!! tip "Pro tip: Simplify your git history"
    - Use `git mv` to rename a file so that it is tracked as a rename (with or without changes).
    - If you rename a file then `git add` its parent directory, the diff will show the deletion of the original file and addition of a "completely new" file, even if nothing has changed. This makes reviewing changes much more complicated than necessary.

#### Usual Process

After making changes to a file on a branch, check the status of your current working branch (with `git status`). Then, you "add" the file, state what is new about the file ("commit the change"), and `push` the file from your local copy of the repo to the remote copy:

```bash
git add <filename>

git commit -m "Changed x,y,z"

git push
```

!!! tip "Pro tip: Check the stage"
    After using `git add <folder>` or `git add <regex>` (a pattern match), run `git status` to ensure that all intended files--and ***only*** intended files--are staged for commit.

!!! note Note
    If you need to update your branch with changes from the remote `main`, first switch to the branch, then set pull from `main` instead of the current branch, as below.

    ```bash
    git checkout <branch>		

    git pull origin main
    ```
