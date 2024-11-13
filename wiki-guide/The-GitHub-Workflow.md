# GitHub Workflow Guide

Thank you for contributing!

This document outlines guidelines for collaboratively contributing to a repository (repo). 
This workflow is ideal for when:
* You are a member of the Imageomics Institute and have write access to the repository you're contributing to.
* You have (or expect to have) multiple people contributing to the repository and want to keep contributions organized and all team members up-to-date on progress.
* You are working on a repository individually and want to keep contributions organized and log progress for your future self or others interested in seeing it.

It follows a branch and pull request (PR) based workflow, which provides a controlled way to bring internal contributions together for those with write access to the repository (those without write access will need to fork the repository first before making contributions).

Importantly, this workflow suggests that **_contributions are created through PRs_** rather than directly committing to or merging into the `main` branch.

## To contribute as an Imageomics member with write access:
### 1. Clone the repo to your machine.
```sh
git clone https://github.com/Imageomics/<repo-name>.git
cd <repo-name>
```

### 2. Create a new branch.
For example, if you want to add a feature to your code that simulates human vision, you could name the branch `feature/simulate-vision`.

> _pro-tip_: make a new branch for each PR scoped by the task, feature, or bug fix.
```sh
git branch feature/simulate-vision
git checkout feature/simulate-vision
```
or to create and switch to the new branch with a single command:
```sh
git checkout -b feature/simulate-vision
```

### 3. Make your desired changes.
For example, imagine you created three new files, each simulating a component of the human visual system: `retina.py`, `occipital.py`, and `visual_cortex.py`.

### 4. Stage and commit changes to the new branch.
Commit frequently with each commit based on a logical self-contained change using descriptive commit messages.

> _pro-tip_: use imperative phrases beginning with words such as "add", "update", "fix", "refactor", "remove", "improve", ...

> _pro-tip_: write a multi-line commit message with a short summary on the first line and a longer description if needed using `git commit -m "Short summary" -m "Long description"`

```sh
git add retina.py occipital.py visual_cortex.py
git commit -m "Implement the retina, occipital, and visual cortex components of the human visual system."
```

### 5. Update your local `main` branch.
Ensure your local `main` branch is up-to-date with the remote to incorporate any changes other collaborators may have made.

> _pro-tip_: if you're unsure what branch you should have checked out, remember that the branch being merged to or committed to should be the branch that is active. Check with `git branch` and look for `*` next to what's active.
```sh
git checkout main
git pull origin main
```

### 6. Merge changes made to `main` to your new branch.
If updates were pulled into your local `main` branch, merge them into your new branch.
```sh
git checkout feature/simulate-vision
git merge main
```

### 7. Push your new branch to the remote.
This should contain any updates made by others as well as your new changes. The first time this is done for a branch, you will need to map the branch on your local 'downstream' repo to the corresponding branch on the remote 'upstream' repo. Following this, simply push.
```sh
git push --set-upstream origin HEAD # to auto-match upstream branch name to your current branch name
# or
git push --set-upstream origin feature/simulate-vision # to specify the upstream branch name
# or
git push # subsequent pushes for this branch once the remote tracking branch is set
```

### 8. Make, commit, and push with this branch as needed.
Repeat steps 3-7 until results are in a state suitable to merge with the project's `main` branch.

### 9. Open a Pull Request.
On the GitHub repo page, click the `Pull requests` tab, click the `New pull requests` button, select the new branch you pushed as the head branch and keep the base branch as `main` (where you want to merge your changes into). Click `Create pull request`. 

You can also set the PR to draft status for visibility and discussion of ongoing work. 

If you like doing everything from the command line, you can consider using the [GitHub CLI](https://cli.github.com/) for this step.

> _pro-tip_: keep PRs small and manageable for review; the scope should be focused on the task, feature, or bug fix associated with the branch.

### 10. Verify the repositories and branches in the PR.
**Base Repository:** The original repo you are contributing into. 

**Head Repository:** The repo you are contributing from, which is the same as the base repo unless you are working from a fork. 

**Base Branch:** `main` (or the branch you want to merge your changes into) 

**Compare Branch:** Your new branch with changes.

### 11. Title and describe the PR.
Create a brief title describing the primary issue addressed in the PR.
In the PR description, give a consolidated overview of the motivation for the change(s) and description of choices made. It should briefly summarize the holistic effect resulting from the component commits.
Assign appropriate reviewer(s) and/or link the PR to a project.

### 12. Submit the PR.
Click `Create pull request` to submit.

### 13. Clean up branches.
After a branch is merged and a PR is closed, delete the branch from the remote and your local repository to keep things tidy.

> _pro-tip_: remember, a branch should exist to create a functional contribution to the repository through a PR, and once the function is merged in, the purpose of the branch is fulfilled.
```sh
git checkout main # switch to the main branch before deleting another branch
git branch -d feature/simulate-vision # delete the local branch that was merged
git push origin --delete feature/simulate-vision # delete the remote branch that was merged
git fetch --prune # optionally, this removes any references to deleted remote branches
```

### 14. Update your local main branch before starting new work.
```sh
git pull
```

And for a slightly abbreviated visual summary, the same workflow looks like this:
![image](https://user-images.githubusercontent.com/31709066/230167049-6315b056-74d5-4a18-bb60-5bc06a191783.png)
(image credit: [dbt Labs](https://www.getdbt.com/analytics-engineering/transformation/git-workflow/))