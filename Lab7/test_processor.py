import math

from hypothesis import given, strategies as st
from processor import verify_isbn10_format, calculate_depreciation_factor, lookup_condition_multiplier
#PES2UG24CS011

@given(st.text() | st.none())
def test_verify_isbn10_format_no_crash(s):
    try:
        result = verify_isbn10_format(s)
    except Exception as e:
        assert False, f"verify_isbn10_format crashed with: {e!r} on input {s!r}"
    # Property: result is either a formatted string or None (invalid input)
    assert result is None or isinstance(result, str)


@given(st.text() | st.none())
def test_calculate_depreciation_factor_safe(s):
    try:
        result = calculate_depreciation_factor(s)
    except Exception as e:
        assert False, f"calculate_depreciation_factor crashed with: {e!r} on input {s!r}"
    # Property: result is None (invalid input) or a finite factor in [0.1, 1.0]
    assert result is None or (math.isfinite(result) and 0.1 <= result <= 1.0)


@given(st.text() | st.none())
def test_lookup_condition_multiplier_safe(s):
    try:
        result = lookup_condition_multiplier(s)
    except Exception as e:
        assert False, f"lookup_condition_multiplier crashed with: {e!r} on input {s!r}"
    # Property: result is None (unknown condition) or one of the known multipliers
    assert result is None or result in (1.25, 1.00, 0.80, 0.60, 0.30)


# ---- Extra fuzzing beyond the starter: non-string types and structured inputs ----

@given(st.one_of(st.integers(), st.floats(), st.booleans(), st.lists(st.integers()),
                 st.dictionaries(st.text(), st.integers()), st.binary()))
def test_all_functions_reject_non_strings_gracefully(x):
    for fn in (verify_isbn10_format, calculate_depreciation_factor, lookup_condition_multiplier):
        try:
            assert fn(x) is None
        except Exception as e:
            assert False, f"{fn.__name__} crashed with: {e!r} on input {x!r}"


@given(st.floats(allow_nan=True, allow_infinity=True), st.floats(allow_nan=True, allow_infinity=True))
def test_depreciation_numeric_edge_cases(age, life):
    try:
        result = calculate_depreciation_factor(f"{age}/{life}")
    except Exception as e:
        assert False, f"crashed with: {e!r} on age={age!r}, life={life!r}"
    assert result is None or (math.isfinite(result) and 0.1 <= result <= 1.0)


@given(st.text(alphabet="0123456789-xX ", max_size=20))
def test_isbn_digit_like_strings(s):
    try:
        result = verify_isbn10_format(s)
    except Exception as e:
        assert False, f"crashed with: {e!r} on input {s!r}"
    assert result is None or isinstance(result, str)
