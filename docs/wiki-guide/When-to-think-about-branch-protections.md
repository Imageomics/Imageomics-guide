# Branch Protections

Is your project going public? Are you releasing a package or tool for general use? Then it's time to think about adding branch protections to `main`.

## What are branch protections and why do we need them?

Branch protections are essentially a more formalized implementation of contributing guidelines for your repository. This could be anything from requiring a pull request before pushing or merging updates to `main`, to requiring approval by particular parties before merging a pull request. For more information on branch protections, see GitHub's docs on [branch protection rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). 

Generally speaking, once the set of potential users exceeds that of repository developers (i.e., the repo goes public), it is wise to apply branch protections, especially for the `main` branch of the repo. The primary purpose is to--at a minimum--alert developers of changes prior to their implementation. For more information on potential branch protection rules, see GitHub's [docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).

## How to Implement Branch Protections

From your repository, navigate to "Settings" and select "Branches" from the left toolbar. Provide the name of the branch you would like to protect, for instance `main`, and select the rules that you want applied to the branch. It is also possible to set the rules for branches matching a particular pattern (eg., type `*release*` to apply the rules to any branch containing the word `release`). You can also edit branch protection rules from this page.

The example below shows the addition of branch protection rules for `main` that require a pull request and that it be approved prior to merging. It also will remove approval if other changes are added that require approval.


### Example Branch Protection Rules for `main`

![GitHub branch protections in a repo's Settings](images/GH-branch-protections/239086285-190b758a-68f7-4cbf-9368-a8df9bef7a08.png){ loading=lazy }
/// caption
///

## How to Implement Rulesets (Newer Version of Branch Protections)

From your repository, navigate to "Settings" and select "Rules" from the left toolbar. Click on "New ruleset" and select the type you wish to create ("New branch ruleset" is the ruleset equivalent to branch protections). 

![Select New ruleset in Rules settings](images/GH-branch-protections/382110241-02304951-367a-4c03-bf4b-cf0d53960da9.png){ loading=lazy }
/// caption
///

Here we have selected "New branch ruleset", and named it "published-branch", as we will be applying it to our publication branches (i.e., `main` and `gh-pages`). Be sure to select "Active" to enable the protections.

![Interface for creating a new ruleset](images/GH-branch-protections/382110848-691a2831-ddf6-4ed9-bc27-5288f2936577.png){ loading=lazy }
/// caption
///

We choose to apply these to the default branch (`main` or `master`). 

![Select add target under target branches for branch ruleset](images/GH-branch-protections/382111392-8157d014-0482-4d4f-b695-ab3b7624d5e4.png){ loading=lazy }
/// caption
///

As with branch protections, it is also possible to set the rules for branches matching a particular pattern (eg., type `*release*` to apply the rules to any branch containing the word `release`). We will do this for `gh-pages`.

![Add target pattern for gh-pages under target branches for branch ruleset](images/GH-branch-protections/382111988-20d6499e-fb12-4335-8b8d-76ac6b989528.png){ loading=lazy }
/// caption 
///

You can also edit branch rulesets from this page.
The example below shows the addition of a branch ruleset that requires a pull request and that it be approved prior to merging. It also will remove approval if other changes are added that require approval. This is equivalent to the branch protection example given above.

![Rules checklist](images/GH-branch-protections/382113942-39fd79d4-ff95-404b-86c4-8ab875cc9a4b.png){ loading=lazy }
/// caption
///
