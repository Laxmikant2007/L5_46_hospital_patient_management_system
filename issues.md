\# Lab 5 — Static Code Analysis: Issue Log



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| Mutable default argument | Bug (High) | 13 | `intake\_log=\[]` is shared across all calls | Changed default to `None` and initialized inside the function |

| Bare `except: pass` | Bug (High) | 24 | Silently swallows every exception (Bandit B110) | Removed; used `.get()` with a `None` check instead |

| `eval()` on user input | Security (Medium) | 40 | Code injection risk (Bandit B307) | Replaced with a whitelisted `ast`-based evaluator |

| Weak MD5 hash | Security (High) | 45 | MD5 is not collision-safe (Bandit B324) | Replaced with SHA-256 |

| Insecure `random` token | Security (Low) | 49 | Not cryptographically secure (Bandit B311) | Replaced with `secrets.randbelow` |

| `os.system("echo …")` | Security (High) | 56 | Shell injection risk (Bandit B605) | Replaced with `print()` |

| Hardcoded access key | Security (High) | 79 | Secret stored in source code (Bandit B105) | Read from `HOSPITAL\_NURSE\_MASTER\_KEY` environment variable |

| Unused imports/variables | Code quality | 4, 29, 39, 61 | `math`, `bed\_charge`, `base\_bill`, `p` unused | Removed unused import and variables |

| `open()` without `with` | Resource leak | 52–55 | File may not be closed on error | Wrapped in `with open(...) as handle` |

| Missing docstrings, non-snake\_case names, long lines | Style | many | Pylint C/E codes and Flake8 E501 | Added docstrings, renamed functions, wrapped long lines |

