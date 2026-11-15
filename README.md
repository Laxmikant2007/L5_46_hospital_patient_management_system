# Lab 5: Static Code Analysis — Hospital Patient System (Completed)

## ✅ Student Submission Summary

I have completed all tasks for this lab. 
- **Pylint Score:** Improved from `5.37/10` to `10.00/10`
- **Bandit:** Reduced from `5 issues` (2 High, 1 Medium, 2 Low) to `0 issues`
- **Flake8:** Fixed all `11 PEP 8 style violations`

### Key Fixes Applied:
- **Security (Bandit):** Removed `eval()`, replaced MD5 with SHA-256, replaced `random` with `secrets`, removed `os.system()`, and moved the hardcoded access key to an environment variable.
- **Code Quality (Pylint):** Fixed mutable default arguments, removed bare `except`, added docstrings, renamed functions to snake_case, and removed unused variables.
- **Style (Flake8):** Fixed line lengths, removed unused imports, and added a final newline.

### Deliverables included in this repository:
- `hospital_patient_system.py` — The refactored and secured Python script.
- `issues.md` — Log of all issues found and how they were fixed.
- `reflection.md` — Reflection on the static analysis process.
- `*_report_before.txt` and `*_report_after.txt` — The raw reports from Pylint, Bandit, and Flake8 before and after the fixes.

---
---

# Original Assignment Instructions

# Lab 5: Static Code Analysis — Hospital Patient System

**Your file:** `hospital_patient_system.py`

Follow the lab handout for the full instructions.

## About the program

A hospital patient records and admission manager. It admits patients into specific wards, processes discharges, calculates dynamic treatment costs, and exports admission ledgers.

The code works, but only just. It has quality, style and security problems of the kind Pylint, Flake8 and Bandit are built to find.

## What to do

1. **Run it first** and read the output carefully:
   ```bash
   python hospital_patient_system.py
   ```
   It asks one question. Press Enter to use the default, then try a few inputs of your own. Not every problem in this file is something a tool will flag, so pay attention to output that looks wrong.

2. **Install the tools:**
   ```bash
   pip install pylint bandit flake8
   ```

3. **Run the analysis** and save the reports:
   ```bash
   pylint hospital_patient_system.py > pylint_report.txt
   bandit -r hospital_patient_system.py > bandit_report.txt
   flake8 hospital_patient_system.py > flake8_report.txt
   ```

4. **Document the issues** in `issues.md` using this table (at least 4 rows, high and medium severity first):

   | Issue | Type | Line(s) | Description | Fix Approach |
   |-------|------|---------|-------------|--------------|
   | ... | ... | ... | ... | ... |

5. **Fix the code.** Fix at least 4 of the issues you documented, then rerun all three tools to confirm they are gone. Repeat until you are satisfied. The program should still do its job when you are done.

6. **Reflect.** Answer the four reflection questions from the handout in `reflection.md`.

## Deliverables

1. `hospital_patient_system.py`: your cleaned version, with at least 4 issues fixed.
2. `issues.md`: the completed issue table.
3. `reflection.md`: your answers to the reflection questions.

**Target:** aim for a Pylint score above 9.5 on your final file. A perfect 10.00/10 is very good.

Be ready to explain the bugs you found and how you fixed them. You may be called on to present.
