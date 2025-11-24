"""
Linux user password checker and generator.

This module checks if a Linux user exists, prompts for a password
or generates one, and validates it against security requirements.
"""

import getpass
import subprocess
from pass_oop import PasswordGenerator


def check_user_exists(username):
    """
    Check if a user exists in the system.

    Args:
        username (str): Username to check.

    Returns:
        bool: True if user exists, False otherwise.

    Examples:
        >>> check_user_exists("root")
        True
        >>> check_user_exists("nonexistent_user")
        False
    """

    result = subprocess.run(["id", username], capture_output=True)

    if result.returncode == 0:
        return True
    else:
        return False


def get_or_generate_password():
    """
    Get password from user or generate if empty.

    Returns:
        str: User-provided or generated password.

    Note:
        If user presses Enter without typing, generates a 12-character
        password with all character types.
    """

    password_input = getpass.getpass("Please enter your password: ")

    if password_input == "":
        generator = PasswordGenerator(12, True, True, True, True)
        passwd = generator.generate_password()
        return passwd
    else:
        return password_input


def check_password_requirements(password):
    """
    Check if password meets security requirements.

    Requirements:
        - Minimum length: 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character

    Args:
        password (str): Password to check.

    Returns:
        bool: True if password meets all requirements, False otherwise.

    Examples:
        >>> check_password_requirements("Abc123!@")
        True
        >>> check_password_requirements("weak")
        False
    """

    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_dig = False
    has_sumb = False

    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True
        if i.isdigit():
            has_dig = True
        if not i.isalnum():
            has_sumb = True
    return has_upper and has_lower and has_dig and has_sumb


def main():
    """Main function to run password checker."""

    username = input("Type your user name: ")

    if not check_user_exists(username):
        print("This user does not exist, try again")
        return

    print(f"Welkome: {username}")

    password = get_or_generate_password()

    is_valid = check_password_requirements(password)

    print(f"\nUser: {username}")
    print(f"Password: {password}")

    if is_valid:
        print("Password is correct!")
    else:
        print("Password does not meet requirements")


if __name__ == "__main__":
    main()
