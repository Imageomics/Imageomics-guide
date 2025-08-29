# GitHub Pull Request (PR) Guide Overview

This guide is divided into three essential sections to help you effectively manage pull requests in a collaborative project:

- [Create a Pull Request](#1-create-a-pull-request): This section explains how to properly prepare and submit a pull request (PR) to ensure that your changes are well-documented, easy to review, and aligned with project goals.
- [Review a Pull Request](#2-review-a-pull-request): Learn the best practices for providing constructive feedback, identifying potential issues, and ensuring code quality during the review process.
- [Respond to a Pull Request Review](#3-respond-to-a-pull-request-review): Understand how to address reviewer feedback, make necessary changes, and ensure your pull request meets the required standards for approval.

By following these steps, you will contribute to a smooth and efficient workflow, ensuring collaboration and quality in your project.

## 1. Create a Pull Request

Before creating a pull request, first, please follow [the GitHub Workflow](The-GitHub-Workflow.md) to create and push your branch.

### 1.1 Navigate to the Repository's Main Page

On GitHub, go to the main page of the repository where you’ve pushed your branch.

### 1.2 Select Your Branch

From the "Branch" menu, choose the branch that contains your changes (the one you just pushed).

### 1.3 Click 'Compare & pull request'

You’ll see a button labeled Compare & pull request. Click this to begin the process of creating a pull request for your changes.

![GitHub's Compare & pull request button](images/GH-PR-guide/365234535-659b312e-d95d-4bee-a958-4ce23fc4255d.png){ loading=lazy, width="800" }
/// caption
///

### 1.4 Add Title and Description

In the pull request form, type a descriptive title for your PR. Provide a detailed description of the changes you've made, why they are important, and any other relevant information.

![GitHub's pull request title and description interface](images/GH-PR-guide/365234601-90a0bfcf-807d-4983-a643-0678ace542d2.png){ loading=lazy, width="800" }

### 1.5 Choose Review Type

- If your pull request is ready for review, click Create Pull Request.
- If you want to create a draft version of the pull request for further work before it's ready for others to review, click the drop-down and select Create Draft Pull Request, then click Draft Pull Request.

![GitHub's Create pull request button dropdown options](images/GH-PR-guide/365234701-72dd00f2-936e-44df-af79-ab7522a51def.png){ loading=lazy, width="350" }
/// caption
///

## 2. Review a Pull Request

### 2.1 Navigate to the **Pull requests** tab

![GitHub's Pull Requests tab](images/GH-PR-guide/369927182-fe1bc8e0-6a9a-48cf-a3b3-e9dc11f9fe13.png){ loading=lazy, width="800" }
/// caption
///

### 2.2 Select a Pull Request

In the list of pull requests, click the pull request that you'd like to review.

![Example pull request selection list](images/GH-PR-guide/362360024-c03d12bf-78ce-4311-8a5e-badc9ca1ebef.png){ loading=lazy, width="800" }
/// caption
///

### 2.3 Review Changes

In the pull request page, click **Files changed** so as to see the changes.

![The Files Changed buttin inside the pull request interface](images/GH-PR-guide/362372502-0380ad63-3e22-473f-9eeb-336e43edb81f.png){ loading=lazy, width="600" }
/// caption
///

2.3.1 by clicking ![Gear icon](images/GH-PR-guide/362361806-198206f8-6d94-452f-b136-cebec0472e10.png){ loading=lazy, width="20"}, you can choose the unified or split view.

![Unified vs. split view for file diffs in a pull request](images/GH-PR-guide/362373284-ba099090-8f60-444f-8ae6-c7ab13b7d78f.png){ loading=lazy, width="600" }
/// caption
///

### 2.4 Add Comments or Suggestions

When hovering over the lines of code, you can click the blue comment icon to add your review comments.

![In-line comments button](images/GH-PR-guide/362373606-77b1e2ea-08ab-4fdc-8ef3-22ba678da422.png){ loading=lazy, width="800" }
/// caption
///

2.4.1 If you'd like to add a comment on multiple lines, please click the line number of the first line you want to add comments and drag down to select a range of lines.

### 2.5 Suggest Changes

If you'd like to suggest a specific change to the lines, click ![Suggest changes button](images/GH-PR-guide/362393831-18d9f1f8-9c93-430a-9667-2dbe01248ff0.png){ loading=lazy, width="20"}, and then edit the text within the suggestion block.

![Suggested changes interface](images/GH-PR-guide/362394354-7bce4591-4ff7-44c7-8377-d250eabd3c2c.png){ loading=lazy, width="600" }
/// caption
///

### 2.6 Comment on a File

If you'd like to comment on a file, click ![Comment button](images/GH-PR-guide/362398001-12afff80-ceb8-4c5c-bff0-d95b9c78216a.png){ loading=lazy, width="20"} at the right top of the file, then add your comments.

![Comment button in context](images/GH-PR-guide/362398683-c497797a-da7c-48be-8db9-dcff89ce0fcf.png){ loading=lazy, width="500" }
/// caption
///

### 2.7 Mark Files as Viewed

After you finished reviewing a file, you can mark it as viewed.

![Viewed button](images/GH-PR-guide/362409533-b4297e2f-f74d-4945-a6ab-81da6726e985.png){ loading=lazy, width="600" }
/// caption
///

### 2.8 Start or Add to a Review

When you're done, click Start a review. If you have already started a review, please click Add review comment.
!!! note "Notice"
    All line comments are pending and only visible to you. You can edit the comments when needed. If you'd like to abandon your review, please go to in **Review changes** and click **Abandon review**

### 2.9 Review and Summarize Proposed Changes

Click Review changes, and then type comments to summarize your proposed changes.

![Review changes button](images/GH-PR-guide/364920995-8ce17b45-8a2a-428e-a254-eab0abebb318.png){ loading=lazy, width="500" }
/// caption
///

### 2.10 Select Review Type

![{Review summary interface}](images/GH-PR-guide/362403686-2afb0ae6-6cdc-45c6-b91e-b7b9cfc30189.png){ loading=lazy, width="600" }
/// caption
///

- Select Comment: Provide general feedback on the changes without explicitly approving or rejecting them.
- Select Approve: Indicate that you’ve reviewed the changes and approve them for merging. A common comment for simple approvals is "LGTM" (Looks Good to Me).
- Select Request changes: Provide feedback indicating that revisions are needed before the changes can be approved.

### 2.11 Click Submit review

Current review round is done; this publishes your comments and suggestions. Then the PR can either be merged or updated (depending on approval or comments). We generally expect that whoever submits the PR will merge once all feedback has been incorporated or otherwise addressed.

## 3. Respond to a Pull Request Review

### 3.1 Navigate to the Repository's Main Page

Navigate to your repository name, click **Pull requests**

![Pull requests tab](images/GH-PR-guide/369927182-fe1bc8e0-6a9a-48cf-a3b3-e9dc11f9fe13.png){ loading=lazy, width="600" }
/// caption
///

### 3.2 Incorporate Feedback Changes

After receiving feedback on your pull request, you can apply the changes in one of two ways: either by committing each change individually or by grouping several changes into a single commit. The method you choose depends on whether you prefer fine-grained control over the commit history or a more streamlined approach.

#### 3.2.1 Apply a change in its own commit

If you agree with at suggested change, qpply it by creating a separate commit for it. This approach helps keep your commit history clear and each change traceable.

![Commit suggestions button](images/GH-PR-guide/369920474-be5503d3-6cc2-4313-b49d-069a5a806ac4.png){ loading=lazy, width="600" }
/// caption
///

#### 3.2.2 Add multiple suggestions to a batch of changes

If you plan to include multiple changes in one commit, you can add suggestions to a batch. Once you've collected all the desired suggestions, click "Commit suggestions" to apply them in one go.

![Add suggested change to batch button](images/GH-PR-guide/369920952-1b4e0db0-3451-448b-822f-dd1b14679ec6.png){ loading=lazy, width="600" }
/// caption
///

### 3.3 Add Commit Message

In the commit message field, enter a brief, descriptive message that clearly explains the changes made to the file(s).

### 3.4 Click Commit changes

After entering your commit message, click the "Commit changes" button to finalize and save your modifications to the repository. This step ensures that your changes are recorded and can be reviewed or merged into the main codebase.

### 3.5 Re-requesting a Review

If you’ve addressed all the requested changes and your pull request requires further review, re-request a review by notifying the reviewers. This action prompts them to evaluate your updated code and provide feedback or approval.

### 3.6 Out-of-scope Suggestion

If the suggested change falls outside the scope of your pull request, create a new issue to address the feedback separately. Issues can be created directly from a PR comment.
