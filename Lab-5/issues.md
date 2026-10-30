# Lab 5: Static Code Analysis — Issue Documentation

## Overview
This document records the issues identified during static analysis of `scholarship_disbursement.py` using **Bandit**, **Flake8**, and **Pylint**, along with the remediation strategy for each issue.

---

## Identified Issues and Fix Approaches

| Issue | Tool | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SQL Injection Vector (B608)** | Bandit | Security (Medium) | 10 | Unsafe string formatting `%s` and `%d` used to construct an SQL `INSERT` statement, allowing potential SQL injection. | Replace string formatting with parameterized queries using `?` placeholders passed as a tuple parameter. |
| **Insecure Process Spawning (B605 / B607)** | Bandit | Security (Low) | 26 | `os.system("echo archiving awards")` spawns a system shell process with a partial executable path, vulnerable to command injection and environment tampering. | Replace `os.system()` with safe Python built-in output (`print()`) or logging, and remove unused `os` import. |
| **Silent Exception Swallowing (B110 / W0718)** | Bandit / Pylint | Security / Bug (Low) | 27-28 | `try ... except Exception: pass` catches all general exceptions and silently discards them, masking runtime and system failures. | Remove empty pass block and avoid catching overly broad exceptions; handle specific exceptions or log errors appropriately. |
| **Mutable Default Argument (W0102)** | Pylint | Bug / Logic (Medium) | 9 | `audit=[]` creates a mutable list default that persists across multiple function invocations, causing state leakage between calls. | Set default value to `None` (`audit=None`) and initialize a new list inside the function body if `audit is None`. |
| **Non-idiomatic Comparison to None (E711 / C0121)** | Flake8 / Pylint | Style (PEP 8) | 32 | Equality operator `==` used for comparison with `None` (`scheme == None`) instead of identity comparison. | Use Python identity operator: `if scheme is None:`. |
| **Line Length Limit Exceeded (E501 / C0301)** | Flake8 / Pylint | Style (PEP 8) | 5, 10, 17, 19, 34 | Several lines exceed the maximum line length limit of 79 characters defined by PEP 8. | Break multi-line SQL strings, method chains, and statements cleanly into multiple lines within 79 characters. |
| **Global State Mutation (W0603 / C0103)** | Pylint | Design / Maintainability | 6, 16 | Module-level global variable `disbursed_total` mutated via `global` statement inside `disburse()`, harming encapsulation and testability. | Encapsulate database connection and state inside a `ScholarshipLedger` class or structured manager. |
| **Inconsistent Return Statements (R1710)** | Pylint | Code Quality | 15-21 | Function `disburse()` returns `row[0]` on success but implicitly falls through to `None` when `row` is falsy. | Explicitly return `None` when `row` is not found to make return signatures unambiguous. |
| **Non-standard Naming Style (C0103)** | Pylint | Style (PEP 8) | 31 | Function name `bySchemeCount` uses camelCase instead of PEP 8 compliant snake_case (`by_scheme_count`). | Rename function to `by_scheme_count` and provide `bySchemeCount` alias for backward compatibility. |
| **Missing Module & Function Docstrings (C0114 / C0116)** | Pylint | Documentation | 1, 9, 15, 24, 31, 37 | Module and functions lack explanatory docstrings explaining their parameters and purpose. | Add informative docstrings to module, classes, and all functions. |
