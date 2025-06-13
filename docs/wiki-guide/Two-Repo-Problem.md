# Two Repo Problem
When working on a research project often the code is kept private until a paper is published.

In conflict with this is the need to have a public repo for following purposes:

- Host a website (via a `gh-pages` branch)
- Act as a placeholder for when the paper is published
- Share code from an earlier paper

The typical approach is to have one __public git repo__ and one __private git repo__.

## Merging Challenges
Once code changes are complete in the __private git repo__ moving them to the __public git repo__ can be a problem.
For instance, if the __public git repo__ and the __private git repo__ were created separately they will have unrelated histories. 

**Common challenges when merging:**

- Determining the correct git commands and steps to perform the merge
- Cleaning up many small commits into one or a few larger commits
- Merge conflicts - Files such as the README that may have diverged and result in merge conflicts
- Accidentally losing changes or duplicating changes

## Solutions

### Create private from public repo
To ensure related histories, create the public repo and then create a private repo from it.
The public repo will be created with a README file ensuring it has a commit.
The private repo will be created without any extra files so it will have no commits.

#### 1. Create Public Repo
First create a public repo with commits.

Visit https://github.com/organizations/Imageomics/repositories/new

- Enter the public repo name
- Click the checkbox for `Add a README file`
- Choose a license
- Select an appropriate `.gitignore` template
- Click `Create repository`

After this step you should see a repo with commits similar to the following:

![New public repository Initial commit indicator](images/two-repo-problem/340342731-d174b21a-0d2d-480d-a7b5-77c7cacf16af.png){ loading=lazy, width=600 }
/// caption
///

#### 2. Update Main Branch of Public Repo
Make changes to the [README](GitHub-Repo-Guide.md#readme) and [`.gitignore`](GitHub-Repo-Guide.md#gitignore) in the public repo such that no further changes will be needed until the private repo is merged.

After this step you should see a repo with at least 2 commits similar to the following:

![New commits indicator](images/two-repo-problem/340343092-84608140-6d1a-4708-8659-bd03e715afb2.png){ loading=lazy, width=600 }
/// caption
///

#### 3. Add Branch Protections to Public Repo
Once your repository is set up, only changes to the `gh-pages` branch are recommended; establish branch protections on both `main` and `gh-pages` that require review and approval (see [When to think about branch protections](When-to-think-about-branch-protections.md) for more information). 

There are two issues at play here:

1. There is potential to introduce merge conflicts when bringing in the development repo to merge with the `main` branch if it has been changed. Hence, it is important that you avoid making changes to the `main` branch after spin-off.
2. The `gh-pages` branch will generate the website for the publication. Hence, it is a "published" branch, requiring regular checks with protections like the `main` branch.


#### 4. Create Private Repo
First create a private repo __without__ commits.

Visit https://github.com/organizations/Imageomics/repositories/new

- Enter the private repo name (ex: `<public-repo>-dev`)
- __DO NOT__ check `Add a README file`
- __DO NOT__ Choose a license
- __DO NOT__ select a .gitignore template
- Click `Create repository`

After this step you should see a repo without any commits with a box similar to the following:

![New private repo after creation](images/two-repo-problem/340343305-7f0f79f9-956b-4a46-b110-235e2ed4295a.png){ loading=lazy, width=600 }
/// caption
///

#### 5. Push initial changes from public to private
In the following example we will clone the private repo: `johnbradley/research-project-x-private`.
And pull commits from the public repo: `johnbradley/research-project-x`.

##### 5a. Clone Private Repo
```console
git clone git@github.com:johnbradley/research-project-x-private.git
```

Output will have a warning similar to the following:
```
Cloning into 'research-project-x-private'...
warning: You appear to have cloned an empty repository.
```

##### 5b. Pull Commits to Private Repo
Switch to the private repo directory.
```console
cd research-project-x-private
```

Add a new remote repo named `upstream` that points to the public GitHub repo.
```console
git remote add upstream git@github.com:johnbradley/research-project-x.git
```

Pull commits from the public repo.
```console
git pull upstream main
```

!!! note "Note"
    Running `git remote -v` will confirm where a standard git push (or git pull) will send (or receive) commits from.


##### 5c. Push Commits to Private Repo on GitHub
```
git push
```
After the above command you should be able to see commits in the private repo similar to the following:

![Private repo status after merge](images/two-repo-problem/340343584-069c445a-487d-432c-8b82-c3867be863ae.png){ loading=lazy, width=600 }
/// caption
///

Now you're ready to work on development in the private repo following the standard [GitHub Workflow](The-GitHub-Workflow.md) with the private repo as your remote.

### Merge Private to Public
Once your changes are done on the private repo (i.e., when you're ready to make your project public) you can push the changes to the public repo.

For this example the public repo will be at `johnbradley/research-project-x` and the private will be at `johnbradley/research-project-x-private`.
A branch named `v1` will be created on the public repo with changes from the private repo.

#### Create a branch on Public with Private commits
Clone the public repo, cd into the directory.
```console
git clone git@github.com:johnbradley/research-project-x.git
cd research-project-x
```

Ensure we are on the main branch and up to date with GitHub:
```console
git checkout main
git pull
```

Create a branch named `v1`. Checkout the branch.
This branch will hold the private repo changes.
```console
git branch v1
git checkout v1
```

Add an upstream remote pointing at the private repo.
```console
git remote add upstream git@github.com:johnbradley/research-project-x-private.git
```

 Pull main branch changes from private repo into `v1` branch.
```console
git pull upstream main
```

At this point you could rebase the commits to reduce them to meaningful commits. However, keep in mind that this would result in different commit histories on the public and private repos after pushing `v1`, which may impact the ability to use this strategy for a `v2`. It would be preferable to use this strategy in [pull requests (PRs)](The-GitHub-Workflow.md#9-open-a-pull-request) during development.


Push `v1` branch to the public repo.
```console
git push --set-upstream origin v1
```

#### Next Steps
At this point the main branch of the public repo should match the main branch of the private repo.
Additional changes should be made only to the private repo, preferably using a branch.
See [Github-Workflow](The-GitHub-Workflow.md) for more details.
When you are ready to release a new version of the code in the private repo follow the [Merge Private to Public instructions](#merge-private-to-public) again using a new version branch name (eg. `v2`).

<Hr>

## _What if I already have mismatched repos?_
If you find yourself with two repositories that have misaligned histories, please read the following and reach out to the Imageomics Informatics Team so we can help.

### Resolving Mismatched Public/Private Repos
If you already have a public and private repo with unrelated histories resolving this can be challenging.

Three approaches to resolve merging disparate public/private repos are documented here.

- Merge - use when the public and private repos contain only unrelated commits.
- Reset - use when all public repo commits can be deleted and replaced with private repo commits.
- Cherry Pick - use when the same commits exist in both repos with different hashes.

### Merge
Merge commits from the `main` branch of the private repo into the `main` branch of the public repo.

!!! warning "Warning"
    If the repos have commits in common with different hashes this will result in merge conflicts and duplicated commits.

Merge the main branch of the private repo with the main branch of the public repo.
As far as maintaining history this is the safest approach. Often this approach results in merge conflicts.
Merging conflicts can take time to manually resolve and is challenging to learn.
The allow unrelated histories flag is necessary for this approach:
```
git merge --allow-unrelated-histories ...
```

### Reset
Replace all commits on the `main` branch of the public rep with commits from the `main` branch of the private repo.

!!! danger "Danger"
    This will destroy all history in the public repo main branch!

This option is only safe to do when releasing the first version of a version on the public repo.
After setting up the remote for upstream run a command similar to the following:
```
git reset --hard upstream/main
```

### Cherry Pick
This method is used when the same commits exist in both repos with different hashes.
This requires finding which commits are in the private repo but not in the public repo.

!!! warning "Warning"
    If the commits you cherry-pick have commits in common with different hashes this will result in merge conflicts and duplicated commits.

After fetching your upstream branch you can cherry pick a range of commits to add like so:
```
git cherry-pick <start-commit-hash>..<end-commit-hash>
```
