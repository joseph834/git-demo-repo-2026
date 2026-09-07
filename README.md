# Team Git Workshop

A small dependency-free Python project for practising Git collaboration in the VS Code terminal.

The code is deliberately simple. The goal is Git: branches, commits, pushes, pull requests, and merge-conflict resolution.

## Branch model

The repository-level `main` branch is the clean, unchanged baseline.

Each team works in its own area:

```text
main
└── workshop-health/team-1/main
    ├── workshop-health/team-1/<username>
    └── workshop-health/team-1/<username>
```

- `main`: Do not edit or merge into this branch during the workshop.
- `workshop-health/team-<number>/main`: Your team's shared main branch.
- `workshop-health/team-<number>/<username>`: Your personal working branch.

## Exercises

1. Create a personal branch and make a commit.
2. Publish the branch and create a pull request into the team branch.
3. Update your branch and resolve a merge conflict in VS Code.

## Useful commands

```bash
git status
git branch
git switch -c <branch-name>
git diff
git add <file>
git commit -m "Message"
git push -u origin <branch-name>
git fetch origin
```