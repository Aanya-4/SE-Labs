# Software Engineering Labs

**Name:** Aanya K
**SRN:** PES2UG24CS011
**Section:** 5A
**University:** PES University, Department of CSE

One folder per lab. Each folder has its own `README.md` listing its files and results.

## Labs

| Folder | Lab | Main deliverables |
|--------|-----|-------------------|
| [Lab1](Lab1/) | Requirements Engineering & UML Use-Case Modelling | Requirements table, use-case diagram, use-case flow |
| [Lab2](Lab2/) | Agile Backlog Creation & Sprint Simulation in Jira | Jira screenshots, reflection |
| [Lab3](Lab3/) | Component Modelling & Architectural Pattern Selection | Component diagram, justification |
| [Lab4](Lab4/) | VibeCoding (Tic-Tac-Toe) | Before/after videos, updated code, chat history |
| [Lab5](Lab5/) | Static Code Analysis (Pylint, Bandit, Flake8) | Fixed script, before/after reports, issues table, reflection |
| [Lab6](Lab6/) | Code and Branch Coverage Analysis | Coverage test files, terminal screenshots |
| [Lab7](Lab7/) | Fuzzing for Input Validation Bugs (Hypothesis) | Fixed script, fuzz tests, screenshots report |

Labs 1 to 3 use Problem Statement #09 (Faculty Research Grant & Publication Tracker); the problem statement PDF is included in each of those folders.

## Structure

```
SE-Labs/
├── README.md
├── Lab1/   requirements, use-case diagram, use-case flow, problem statement
├── Lab2/   Jira submission PDF, reflection, problem statement
├── Lab3/   component diagram, justification, problem statement
├── Lab4/   videos, chat history, tic-tac-toe/ (code)
├── Lab5/   theater_system.py, reports/before/, reports/after/, issues.md, reflection.md
├── Lab6/   bookstore_trade_in.py, coverage tests, screenshots
└── Lab7/   processor.py, test_processor.py, fuzzing report
```

## Running the code labs

| Lab | Commands (run inside the lab folder) |
|-----|--------------------------------------|
| Lab4 | `cd tic-tac-toe && pip install -r requirements.txt && python main.py` |
| Lab5 | `pip install pylint bandit flake8`, then `pylint theater_system.py`, `bandit -r theater_system.py`, `flake8 theater_system.py` |
| Lab6 | `pip install coverage pytest`, then `coverage run --branch -m pytest BranchCoverageTest_bookstore_trade_in.py` and `coverage report -m` |
| Lab7 | `pip install hypothesis pytest`, then `python -m pytest test_processor.py` |
