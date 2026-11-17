# L6_L7_09 — Bookstore Trade-In

Lab 7: Fuzz Testing with Hypothesis

Author: Aanya K (PES2UG24CS011)

## About

A set of property-based fuzz tests targeting ISBN-10 format validation, book depreciation ratios, and condition multiplier lookups to expose type and bound crashes. The buggy starter `processor.py` was fuzzed with Hypothesis, the crashes were analysed, and the module was hardened with input validation.

## Files

| File | Description |
|------|-------------|
| `processor.py` | Fixed module: every function validates its input and returns `None` instead of crashing |
| `test_processor.py` | Completed Hypothesis tests (3 starter tests + 3 extra edge-case tests) |
| `PES2UG24CS011_Lab7_Fuzzing_Report.pdf` | Report with screenshots for Steps 2, 4, 5 and 6 |

## Bugs found by fuzzing (original `processor.py`)

| Function | Crashes on |
|----------|-----------|
| `verify_isbn10_format` | Short or empty strings (`IndexError`), non-digit input such as `abc` (`ValueError`), `None` (`AttributeError`) |
| `calculate_depreciation_factor` | Missing or extra `/`, non-numeric text, `None`, lifespan of `0` (division by zero); also accepted `nan`, `inf` and negative values |
| `lookup_condition_multiplier` | Unknown condition codes (`KeyError`), `None` (`AttributeError`) |

## The fix

- Each function checks that its input is a string and returns `None` for anything invalid.
- ISBN-10 must be 9 ASCII digits followed by a digit or `X` (hyphens and surrounding spaces are ignored).
- Depreciation input must be `age/lifespan` with finite numbers, `age >= 0` and `lifespan > 0`; the result stays in `[0.1, 1.0]`.
- Condition lookup uses `dict.get`, so unknown codes return `None`.
- `main()` prints a clear message when a function returns `None`.

Valid inputs behave exactly as before (for example `0-306-40615-2`, `3/10`, `MINT`).

## How to run

```bash
pip install hypothesis pytest
python processor.py
python -m pytest test_processor.py
```

Expected result with the fixed `processor.py`: `6 passed`. Against the original buggy script, all 6 tests fail.

## Tests

| Test | What it checks |
|------|----------------|
| `test_verify_isbn10_format_no_crash` | Text or `None` never crashes; result is a string or `None` |
| `test_calculate_depreciation_factor_safe` | Text or `None` never crashes; result is `None` or finite and within `[0.1, 1.0]` |
| `test_lookup_condition_multiplier_safe` | Text or `None` never crashes; result is `None` or a known multiplier |
| `test_all_functions_reject_non_strings_gracefully` | Ints, floats, bools, lists, dicts and bytes return `None` |
| `test_depreciation_numeric_edge_cases` | NaN, infinity and extreme floats in `age/life` form |
| `test_isbn_digit_like_strings` | Strings made only of digits, `-`, `x`, `X` and spaces |
