# Guide to GitHub Projects

When starting a new project, it can be helpful to have a shared tracker or project board to keep track of who is responsible for which tasks, what has and has not yet been done, which tasks are necessary for various goals of the project, and so on. Note that many of these items are also helpful when working on a project by oneself. GitHub provides a very useful tool for just this purpose: [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). GitHub projects can be linked with one or more GitHub repos to automatically keep track of issues and PRs associated with your project.

## Some advantages of working with GitHub Projects

- Different view options that sync automatically.
- Easy to see who's doing what and keep track of progress.
    - Profile images show up for assignees to various tasks.
    - Clicking on an assignees profile image will show only that person's assigned tasks (similarly for labels and milestones attached to tasks).
- More columns/categories can be added for different aspects of the project.
- Multiple repos can be linked to a single project.
    - Access to issues _is_ controlled by repo access permissions; only the existence of issues is universal to the project.
- Closing an issue will automatically move the task to "Done".
- Tasks can be reordered within their columns/categories to keep most pressing tasks at the top.

## Interacting with GitHub Projects

To help you get started working with [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects), we have a [General Project Template](https://github.com/orgs/Imageomics/projects/31/views/1) with both a [Taskboard](https://github.com/orgs/Imageomics/projects/31/views/1) and [Table](https://github.com/orgs/Imageomics/projects/31/views/2) view initialized, along with label and milestone displays turned on.
Both of these views will automatically stay updated so that each member of the project can utilize whichever version they find most informative.

Issues can be added directly to the project board/table or on the repo. If added through the repo, they must be linked to the project and have status assigned. Milestones must be created on the repo (under the Issues tab, select "Milestones" to create one), similarly for labels.

!!! note "Note"
    Issues on a project board that are linked to a repository to which a user does not have access will not be visible to them, even if they have access to the project. They will show up (for that user) as unidentified issues with no status.
