\# Lab 5 — Reflection



\## 1. Which issue was easiest to fix, and why?



The easiest issue was removing the unused `import math` and the unused

variables `bed\_charge`, `base\_bill`, and `p`. These required no logic

changes — I only deleted lines that were never used, so there was no

risk of breaking the program.



\## 2. Which issue was hardest to fix, and why?



The hardest issue was replacing `eval()` in `calculate\_treatment\_cost`.

The original code used `eval("base\_bill \* 1.12")` to compute the bill,

and I could not simply delete it without changing behaviour. I replaced

it with a small AST-based evaluator that only allows numbers, the name

`base\_bill`, and the operators `+ - \* /`. This keeps the original

formula working while eliminating arbitrary code execution.



\## 3. How did each static analysis tool help?



\- \*\*Bandit\*\* found the security problems I would have missed: the

&#x20; `eval()` call (B307), the weak MD5 hash (B324), the non-cryptographic

&#x20; `random` token (B311), the shell call `os.system(...)` (B605), the

&#x20; bare `except: pass` (B110), and the hardcoded access key (B105).

\- \*\*Pylint\*\* found the code-quality problems: the mutable default

&#x20; argument, the unused variables and import, missing docstrings, the

&#x20; non-snake\_case function name, the `== None` comparison, and the

&#x20; redundant `if/else` around a boolean return.

\- \*\*Flake8\*\* found the PEP 8 style issues: line length, bare `except`,

&#x20; and the missing final newline.



\## 4. Would you use these tools on future projects?



Yes. Running Bandit first (security), then Pylint (quality), then

Flake8 (style) matches the order used in most CI pipelines. Static

analysis catches problems before code is executed and before code

review, which saves time and prevents security bugs from reaching

production.



\## 5. Final results



| Tool   | Before | After |

|--------|--------|-------|

| Pylint | 5.37/10 | 10.00/10 |

| Bandit | 5 issues (2 High, 1 Medium, 2 Low) | 0 issues |

| Flake8 | 11 issues | 0 issues |



