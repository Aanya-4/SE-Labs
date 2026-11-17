import math
import re

#PES2UG24CS011

# 9 ASCII digits followed by a digit or X/x (ISBN-10 check character)
_ISBN10_PATTERN = re.compile(r"[0-9]{9}[0-9Xx]")

_MULTIPLIERS = {
    "MINT": 1.25,
    "LIKE_NEW": 1.00,
    "VERY_GOOD": 0.80,
    "GOOD": 0.60,
    "POOR": 0.30,
}


def verify_isbn10_format(isbn_str):
    """Return a summary string for a well-formed ISBN-10, else None."""
    if not isinstance(isbn_str, str):
        return None
    cleaned = isbn_str.replace('-', '').strip()
    if not _ISBN10_PATTERN.fullmatch(cleaned):
        return None
    first_digit = int(cleaned[0])
    group_code = cleaned[1:4]
    check_char = cleaned[9].upper()
    return f"Group {group_code}: Starts {first_digit}, Checksum {check_char}"


def calculate_depreciation_factor(book_age_str):
    """Parse 'age/lifespan' and return a factor in [0.1, 1.0], else None."""
    if not isinstance(book_age_str, str):
        return None
    parts = book_age_str.split('/')
    if len(parts) != 2:
        return None
    try:
        age = float(parts[0])
        life = float(parts[1])
    except ValueError:
        return None
    if not (math.isfinite(age) and math.isfinite(life)):
        return None
    if age < 0 or life <= 0:
        return None
    try:
        depreciation = 1.0 - (age / life)
    except (ZeroDivisionError, OverflowError):
        return None
    if not math.isfinite(depreciation):
        return None
    return round(max(0.1, depreciation), 2)


def lookup_condition_multiplier(condition_code):
    """Return the price multiplier for a known condition code, else None."""
    if not isinstance(condition_code, str):
        return None
    grade = condition_code.strip().upper()
    return _MULTIPLIERS.get(grade)


def main():
    print("==== Running verify_isbn10_format ====")
    isbn_in = input("Enter ISBN-10 (e.g. 0-306-40615-2): ")
    isbn_out = verify_isbn10_format(isbn_in)
    print(isbn_out if isbn_out is not None else "Invalid ISBN-10 format.")

    print("\n==== Running calculate_depreciation_factor ====")
    age_in = input("Enter age/lifespan in years (e.g. 3/10): ")
    dep = calculate_depreciation_factor(age_in)
    print("Depreciation Factor:", dep if dep is not None else "Invalid age/lifespan input.")

    print("\n==== Running lookup_condition_multiplier ====")
    cond_in = input("Enter condition (e.g. MINT, GOOD, POOR): ")
    mult = lookup_condition_multiplier(cond_in)
    print("Multiplier:", mult if mult is not None else "Unknown condition.")


if __name__ == "__main__":
    main()
