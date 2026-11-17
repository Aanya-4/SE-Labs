# Lab 6: Code and Branch Coverage Analysis

**Name:** Aanya K | **SRN:** PES2UG24CS011 | **Section:** 5A

## Files

| File | Purpose |
|------|---------|
| `bookstore_trade_in.py` | Application under test |
| `test_bookstore_trade.py` | Starter test supplied with the repo |
| `CodeCoverageTest_bookstore_trade_in.py` | Tests written to reach more than 90% code coverage (14 tests) |
| `BranchCoverageTest_bookstore_trade_in.py` | Tests written to reach more than 90% branch coverage (36 tests) |
| `code_coverage_line.png`, `code_coverage_branch.png` | Terminal output for the code coverage tests (line and branch runs) |
| `branch_coverage_line.png`, `branch_coverage_branch.png` | Terminal output for the branch coverage tests (line and branch runs) |

## Results

| Test file | Tests | Line coverage | Branch coverage |
|-----------|-------|---------------|-----------------|
| `test_bookstore_trade.py` (starter) | 1 | 49% | 45% |
| `CodeCoverageTest_bookstore_trade_in.py` | 14 | 100% | 100% |
| `BranchCoverageTest_bookstore_trade_in.py` | 36 | 100% | 100% |

## How to run

```bash
pip install coverage pytest
coverage run -m pytest CodeCoverageTest_bookstore_trade_in.py
coverage report -m
coverage run --branch -m pytest BranchCoverageTest_bookstore_trade_in.py
coverage report -m
```
