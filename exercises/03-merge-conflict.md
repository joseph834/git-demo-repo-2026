# Exercise 3: Resolve a merge conflict in VS Code

## Goal

Create a planned conflict with a teammate, merge the latest team branch into your own branch, and resolve the conflict using VS Code.

## Setup: choose two people

Within each team, choose two participants:

- **Person A** changes the medium-risk threshold and gets their pull request merged first.
- **Person B** adds a very-high risk band on their own branch, then updates from the team branch.

Both people must create their personal branches from the same starting version of the team branch.

## Starting function

Both participants edit this function in `src/risk_score.py`:

```python
def risk_band(score):
    """Map a score to a human-readable risk band."""
    if score >= 50:
        return "high"
    if score >= 25:
        return "medium"
    return "low"
```

## Person A: make and merge the first change

Change the medium threshold from `25` to `30`:

```python
def risk_band(score):
    """Map a score to a human-readable risk band."""
    if score >= 50:
        return "high"
    if score >= 30:
        return "medium"
    return "low"
```

Commit and push:

```bash
git add src/risk_score.py
git commit -m "Adjust medium risk threshold"
git push
```

Create a PR into the team branch and merge it:

```text
workshop-health/team-<team-number>/<person-a>
→ workshop-health/team-<team-number>/main
```

## Person B: make a different change

On your own branch, add a `very-high` risk band:

```python
def risk_band(score):
    """Map a score to a human-readable risk band."""
    if score >= 70:
        return "very-high"
    if score >= 50:
        return "high"
    if score >= 25:
        return "medium"
    return "low"
```

Commit and push:

```bash
git add src/risk_score.py
git commit -m "Add very high risk band"
git push
```

## Person B: fetch and merge the team branch

Fetch the latest remote history:

```bash
git fetch origin
```

Merge the updated team branch into your current personal branch:

```bash
git merge origin/workshop-health/team-<team-number>/main
```

Git should report a conflict in `src/risk_score.py`.

Check the state:

```bash
git status
```

## Resolve it in VS Code

Open the repository in VS Code:

```bash
code .
```

Open the conflicted file. VS Code shows these choices:

| Option | Meaning in this merge |
|---|---|
| Accept Current Change | Keep Person B's change from the branch currently checked out |
| Accept Incoming Change | Keep Person A's change arriving from the team branch |
| Accept Both Changes | Keep both versions, then edit them into valid final code |

Your instructor will assign your team one of these options.

### If assigned: Accept Current Change

Choose **Accept Current Change**. The final function retains Person B's `very-high` band but does not include Person A's threshold change.

### If assigned: Accept Incoming Change

Choose **Accept Incoming Change**. The final function retains Person A's medium threshold of `30` but does not include Person B's `very-high` band.

### If assigned: Accept Both Changes

Choose **Accept Both Changes**, then tidy the function so it is valid Python:

```python
def risk_band(score):
    """Map a score to a human-readable risk band."""
    if score >= 70:
        return "very-high"
    if score >= 50:
        return "high"
    if score >= 30:
        return "medium"
    return "low"
```

Do not leave conflict markers in the file:

```text
<<<<<<< HEAD
=======
>>>>>>> origin/workshop-health/team-<team-number>/main
```

## Finish the merge

After saving the resolved file:

```bash
git add src/risk_score.py
git status
git commit -m "Resolve risk band merge conflict"
git push
```

Update Person B's existing pull request, or create a new one, into:

```text
workshop-health/team-<team-number>/main
```

## If you get stuck

To abandon the merge and return to the state before it began:

```bash
git merge --abort
```

Then ask the instructor for help.