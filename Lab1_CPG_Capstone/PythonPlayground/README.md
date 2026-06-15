# Python Playground 🐍

**Simple Console Applications for Young Learners (3rd Grade Level)**

This repository contains beginner-friendly Python programs designed to be easy for 3rd graders to understand and run. Each program uses basic concepts like `print()`, `input()`, simple math, `if/else`, and `random` — nothing complicated!

## The Programs

### 1. `greeting.py`
A friendly program that asks your name and says hello.

**How it works:** Uses `input()` to get your name and `print()` to greet you.

### 2. `adder.py`
A super simple calculator that adds two numbers.

**How it works:** Asks for two numbers, converts them to integers, adds them, and shows the result.

### 3. `guess.py`
A fun number guessing game. The computer picks a number between 1 and 5 — can you guess it?

**How it works:** Uses `random.randint()` to pick a secret number and `if/else` to check your guess.

### 4. `story.py`
Create your own silly short story! (Like a mini Mad Libs)

**How it works:** Asks for an animal, food, and place, then builds a funny sentence.

## How to Run These Programs

1. Make sure you have Python installed (python.org).
2. Open your terminal (Command Prompt on Windows, Terminal on Mac).
3. Navigate to this folder:
   ```
   cd path/to/PythonPlayground
   ```
4. Run any program like this:
   ```
   python greeting.py
   ```
   or on some systems:
   ```
   python3 greeting.py
   ```

Try them all! Change the code and experiment.

## Lab 1: Branching, Git & Python Collaboration

**Objective:** Practice team-based Git workflows by building (and improving) this simple Python project. Focus on branching, collaboration, commits, and merges — not on making the code complex.

### Repository Requirements Met
- ✅ Brand new GitHub repository created from scratch (no templates)
- ✅ README.md (this file!)
- ✅ .gitignore (Python-appropriate)
- ✅ Multiple Python files (.py) — 4 total (more than 2 per student)

### Step-by-Step Git Workflow (Do This in Order)

Follow these steps exactly. **You will intentionally make some common mistakes** so you learn how to fix them — this is part of the learning!

#### Step 0: Create Your GitHub Repository
1. Go to github.com and log in (create account if needed).
2. Click the **+** icon → **New repository**.
3. Name it: `PythonPlayground-YourName` (example: `PythonPlayground-Alex`)
4. **Do NOT** initialize with README, .gitignore, or license (we will add them ourselves).
5. Create the repository. Copy the HTTPS URL (it looks like `https://github.com/yourusername/PythonPlayground-YourName.git`).

#### Step 1: Clone the Empty Repository (Local Setup)
```bash
git clone https://github.com/yourusername/PythonPlayground-YourName.git
cd PythonPlayground-YourName
```

#### Step 2: Add the Starter Files (Initial Commit on main)
Copy the files from this example into your new local folder:
- `.gitignore`
- `README.md`
- `greeting.py`
- `adder.py`
- `guess.py`
- `story.py`

Then run:
```bash
git add .
git commit -m "Initial commit: Add starter Python files and docs"
git push origin main
```

**Common Mistake #1 (Intentional):** Many beginners commit directly to `main` without thinking. That's what we just did — it's okay for the very first commit, but from now on we use branches!

#### Step 3: Create a Feature Branch for Your Changes
Never work directly on `main` after the first commit. Always create a feature branch.

```bash
git checkout -b feature/add-more-fun
```

**What this does:** Creates and switches to a new branch called `feature/add-more-fun`.

#### Step 4: Make Code Changes on Your Branch
Edit one or more Python files to add a small improvement or new feature. Examples of easy changes for 3rd graders:

**Option A: Improve `greeting.py`**
Add a fun fact or ask their favorite color.

**Option B: Improve `adder.py`**
Make it also do subtraction (add another input and print the difference).

**Option C: Improve `guess.py`**
Give a hint if the guess is too high or too low.

**Option D: Improve `story.py`**
Add one more question (e.g., favorite color or silly action).

**Example change for `adder.py`** (add this after the addition):
```python
# Add after the result line
diff = int(num1) - int(num2)
print(num1 + " - " + num2 + " = " + str(diff))
```

Save the file, then commit your work:
```bash
git add adder.py
git commit -m "Add subtraction to the adder program"
```

**Common Mistake #2 (Intentional):** Forgetting to `git add` changed files before committing. If you run `git commit` without `add`, Git will complain or make an empty commit. Practice fixing it with `git status` to see what changed.

#### Step 5: Update Documentation (README.md)
On the same branch, update the README to document your change.

Example addition at the bottom of README:
```markdown
## My Contribution (Your Name - Date)
- Added subtraction feature to `adder.py` so kids can learn adding AND subtracting!
- Tested on my little brother — he loved it!
```

Commit the doc update:
```bash
git add README.md
git commit -m "Update README with my new subtraction feature"
```

#### Step 6: Push Your Feature Branch
```bash
git push origin feature/add-more-fun
```

Go to GitHub → your repo → you should see a banner "Compare & pull request". Create a Pull Request (PR) from your feature branch to `main`.

**Common Mistake #3 (Intentional):** Pushing to the wrong branch or forgetting to push the new branch. If your branch doesn't appear on GitHub, double-check with `git branch -a`.

#### Step 7: Simulate Collaboration & Create a Merge Conflict (The Fun Part!)
To practice real teamwork, we will **intentionally create a merge conflict**.

**On GitHub (or ask a classmate):**
- Have someone else (or you in another terminal/folder) create their own feature branch from `main`.
- Edit the **same line** in the same file (e.g., both edit the last `print` line in `adder.py` or the story sentence in `story.py`).
- Both push their branches and open PRs.

**Example conflict scenario:**
- You changed: `print("You got it! Great job!")` in guess.py
- Classmate changed the same line to something slightly different.

When you try to merge the PRs, GitHub will show **Merge conflict**.

**How to resolve a merge conflict (do this locally):**
1. Checkout main and pull latest:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Merge the feature branch (this will trigger the conflict):
   ```bash
   git merge feature/add-more-fun
   ```
   You will see conflict markers like:
   ```
   <<<<<<< HEAD
   Your version here
   =======
   Classmate's version here
   >>>>>>> feature/add-more-fun
   ```

3. **Edit the file** in your code editor: Remove the `<<<<<<<`, `=======`, `>>>>>>>` lines and keep the version you want (or combine them nicely).

4. Mark as resolved and commit:
   ```bash
   git add guess.py
   git commit -m "Resolve merge conflict in guess.py - combined both greeting messages"
   ```

5. Push the resolved main:
   ```bash
   git push origin main
   ```

**Common Mistake #4 (Intentional):** Leaving conflict markers in the code (bad!). Always clean them up before committing. This is why we practice!

#### Step 8: Clean Up and Finalize
- After successful merge, you can delete the feature branch locally and on GitHub (optional but good practice):
  ```bash
  git branch -d feature/add-more-fun
  ```
  (On GitHub: Settings → Branches → delete)

- Check your history:
  ```bash
  git log --oneline --graph --all
  ```

### What You Should Have Learned
- ✅ Create and switch branches (`git checkout -b`)
- ✅ Make changes, stage (`add`), commit, and push feature branches
- ✅ Update documentation alongside code
- ✅ Create Pull Requests on GitHub
- ✅ Intentionally create and **resolve** merge conflicts
- ✅ Recognize common mistakes: committing to main, forgetting to add files, pushing wrong branch, leaving conflict markers
- ✅ Good habits: descriptive commit messages, branch naming (`feature/...`), pulling before merging

### Tips for Success
- Always run `git status` to see what is happening.
- Use clear commit messages like "Add feature X" not "stuff".
- Pull from main often to avoid big conflicts.
- For real teams: Use issues or a shared doc to decide who works on what file.

**This lab is about Git discipline more than Python code.** The Python programs are kept simple on purpose so you can focus on the workflow.

Have fun collaborating and happy coding! 🎉

## Example Contribution (from feature/add-subtraction branch)
- Added subtraction to `adder.py` so kids can practice both adding and subtracting numbers.
- Updated this README to document the new feature.
- This demonstrates a complete feature branch workflow with documentation update.

**Tested by:** Lab Student  
**Date:** June 2026

---
*Created for Lab 1 — Branching, Git, & Python Collaboration*