import re

def password_strength_checker(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Feedback
    print("Password Strength Feedback:")
    if length_criteria:
        print("✓ Password length is sufficient (8 or more characters).")
    else:
        print("✗ Password is too short (less than 8 characters).")

    if uppercase_criteria:
        print("✓ Contains uppercase letter(s).")
    else:
        print("✗ Does not contain any uppercase letters.")

    if lowercase_criteria:
        print("✓ Contains lowercase letter(s).")
    else:
        print("✗ Does not contain any lowercase letters.")

    if number_criteria:
        print("✓ Contains number(s).")
    else:
        print("✗ Does not contain any numbers.")

    if special_criteria:
        print("✓ Contains special character(s).")
    else:
        print("✗ Does not contain any special characters.")

    # Strength Rating
    strength_count = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    if strength_count == 5:
        print("Overall Strength: Strong")
    elif 3 <= strength_count < 5:
        print("Overall Strength: Medium")
    else:
        print("Overall Strength: Weak")

# Example usage
password = input("Enter your password: ")
password_strength_checker(password)
