"""
Password generator module for creating secure random passwords.

This module generates passwords with specified length (8-128 characters)
containing lowercase, uppercase, digits, and special characters.
"""

import random
import string


def validate_password_length(user_input):
    """
    Validate password length input.

    Args:
        user_input (str): User input string.

    Returns:
        int or None: Valid password length (8-128) or None if invalid.

    Examples:
        >>> validate_password_length("16")
        16
        >>> validate_password_length("5")
        None
    """
    try:
        n = int(user_input)
    except ValueError:
        return None

    if n < 8:
        return None
    elif n > 128:
        return None
    else:
        return n


def generate_password(length):
    """
    Generate a random password of specified length.

    Password contains at least:
    - 1 lowercase letter
    - 1 uppercase letter
    - 1 digit
    - 1 special character

    Args:
        length (int): Desired password length (8-128).

    Returns:
        str: Generated password.

    Raises:
        ValueError: If length is not between 8 and 128.

    Examples:
        >>> password = generate_password(12)
        >>> len(password)
        12
        >>> any(c.islower() for c in password)
        True
    """

    if not isinstance(length, int) or length < 8 or length > 128:
        raise ValueError("Length must be between 8 and 128")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    random_lowercase = random.choice(lowercase)
    random_uppercase = random.choice(uppercase)
    random_digits = random.choice(digits)
    random_punctuation = random.choice(punctuation)

    password_chars = [random_lowercase, random_uppercase,
                      random_digits, random_punctuation]

    all_characters = lowercase + uppercase + digits + punctuation

    while len(password_chars) < length:
        password_chars.append(random.choice(all_characters))

    random.shuffle(password_chars)
    password = "".join(password_chars)

    return password


def get_password_length():
    """
    Prompt user for password length until valid input is provided.

    Returns:
        int: Valid password length (8-128).
    """

    print("Please type number from 8 to 128 range")

    while True:
        user_input = input(
            "Please enter the desired password length: "
        ).strip()

        lenght = validate_password_length(user_input)

        if lenght is None:
            print("Its not a number, try again")
            try:
                n = int(user_input)
                if n < 8:
                    print("Type more than 8")
                elif n > 128:
                    print("Type less than 128")
            except ValueError:
                print("Its not a number, try again")
                continue
        print(f"{lenght} is valid")
        return lenght


def main():
    """
    Main function to run password generator.
    """

    print("Welcome to the Linux User Password Generator!")

    length = get_password_length()
    password = generate_password(length)

    print(f"Generate password: {password}")


if __name__ == "__main__":
    main()
