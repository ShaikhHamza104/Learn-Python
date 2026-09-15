"""
📚 Topic: Variable Naming Rules & Conventions

This script covers Python's lexical identifier rules, explaining which
characters are valid in variable names, forbidden patterns (like leading digits
or embedded whitespace), and PEP 8 snake_case recommendations.

💡 Key points:
    1️⃣ Allowed characters: letters, digits, and underscores (`_`)
    2️⃣ Identifiers must begin with a letter or an underscore, never a digit
    3️⃣ Spaces and special characters are illegal and trigger SyntaxError

🧠 Beginner tip:
    Follow PEP 8: use all-lowercase words separated by underscores
    (`snake_case`) for variable and function names.
"""


def main():
    """
    This function provides examples of valid and invalid variable names.
    """
    # A variable name can contain alphabets, digits, and underscores.
    alpha = "A"
    day_of_week = "sunday"
    user_id_123 = "user123"

    # A variable name can only start with an alphabet or an underscore.
    sameer = 20
    _name = 36

    # A variable name can't start with a digit.
    # 111_invalid_name = 1  # This would cause a SyntaxError

    # No whitespace is allowed to be used inside a variable name.
    # first name = "name"  # This would cause a SyntaxError

    print("Valid variable names:")
    print(f"alpha = {alpha}")
    print(f"day_of_week = {day_of_week}")
    print(f"user_id_123 = {user_id_123}")
    print(f"sameer = {sameer}")
    print(f"_name = {_name}")

    print("\nInvalid variable names are commented out to prevent errors.")


if __name__ == "__main__":
    main()
