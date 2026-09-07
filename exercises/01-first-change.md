# Exercise 1: Create a branch and commit a change

## Goal

Create your own branch from your team's branch, make a very small change, and commit it.

## 1. Start from your team's branch

Replace `<team-number>` with your team number:

```bash
git fetch origin
git switch workshop-health/team-<team-number>/main
git pull
```

Check where you are:

```bash
git status
git branch
```

## 2. Create your personal branch

Replace `<username>` with your assigned username or short name:

```bash
git switch -c workshop-health/team-<team-number>/<username>
```

Example:

```bash
git switch -c workshop-health/team-1/jane
```

Check it:

```bash
git branch
```

The `*` marks your current branch.

## 3. Make a small change

Open `src/customer_data.py` and add one customer record to the `CUSTOMERS` list.

Copy this example and change at least the customer ID:

```python
{
    "customer_id": "C004",
    "age": 35,
    "annual_income": 42000,
    "claim_count": 1,
    "postcode_risk": "medium",
},
```

## 4. Review and commit

```bash
git status
git diff
git add src/customer_data.py
git diff --staged
git commit -m "Add sample customer"
```

Check the result:

```bash
git log --oneline -3
git status
```