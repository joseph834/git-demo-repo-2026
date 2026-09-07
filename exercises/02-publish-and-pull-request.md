# Exercise 2: Publish your branch and open a pull request

## Goal

Push your branch to the shared remote repository, then create a pull request into your team's shared branch.

## 1. Publish your branch

Make sure you are on your personal branch:

```bash
git status
git branch
```

Push the branch and configure its upstream:

```bash
git push -u origin workshop-health/team-<team-number>/<username>
```

Example:

```bash
git push -u origin workshop-health/team-1/jane
```

The `-u` remembers the remote branch. Future pushes should normally be:

```bash
git push
```

## 2. Create a pull request

Open the repository in GitHub/GitHub Enterprise or use the VS Code GitHub Pull Requests extension.

Create a pull request with:

```text
Base branch:    workshop-health/team-<team-number>/main
Compare branch: workshop-health/team-<team-number>/<username>
```

Example title:

```text
Add sample customer
```

## 3. Review and merge

Ask a teammate to review the **Files changed** tab.

Once approved, a designated team member merges the pull request into the team branch.

Do not merge anything into the repository-level `main` branch during this workshop.

## Checkpoint

Your personal branch should now have a remote copy, and your change should be present in:

```text
workshop-health/team-<team-number>/main
```