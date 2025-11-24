"""
Password generator module using Object-Oriented Programming.

This module provides a PasswordGenerator class that creates customizable
random passwords based on user preferences for character types.
"""

import random
import string


class PasswordGenerator:
    """
    A class to generate random passwords with customizable character sets.

    Attributes:
        length (int): The desired length of the password.
        include_uppercase (bool): Include uppercase letters (A-Z).
        include_lowercase (bool): Include lowercase letters (a-z).
        include_digits (bool): Include digits (0-9).
        include_special_char (bool): Include special characters (!@#$...).

    Examples:
        >>> gen = PasswordGenerator(12, True, True, True, True)
        >>> password = gen.generate_password()
        >>> len(password)
        12
    """

    def __init__(self, length, include_uppercase, include_lowercase,
                 include_digits, include_special_char):
        """
        Initialize the PasswordGenerator.

        Args:
            length (int): Desired password length (must be positive).
            include_uppercase (bool): Whether to include uppercase letters.
            include_lowercase (bool): Whether to include lowercase letters.
            include_digits (bool): Whether to include digits.
            include_special_char (bool): Whether to include special chars.

        Raises:
            ValueError: If length is not positive or no character types
                       are selected.
        """

        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer")

        if not any([include_uppercase, include_lowercase,
                    include_digits, include_special_char]):
            raise ValueError(
                "At least one character type must be selected"
            )

        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_char = include_special_char

    def _build_character_set(self):
        """
        Build the character set based on selected options.

        Returns:
            str: String containing all allowed characters.

        Note:
            This is a private method (starts with _).
        """

        allowed_chars = ""

        if self.include_uppercase:
            allowed_chars += string.ascii_uppercase
        if self.include_lowercase:
            allowed_chars += string.ascii_lowercase
        if self.include_digits:
            allowed_chars += string.digits
        if self.include_special_char:
            allowed_chars += string.punctuation

        return allowed_chars

    def generate_password(self):
        """
        Generate a random password based on instance settings.

        Returns:
            str: Generated password of specified length.

        Examples:
            >>> gen = PasswordGenerator(10, True, True, False, False)
            >>> password = gen.generate_password()
            >>> len(password)
            10
            >>> password.isupper() or password.islower()
            False
        """

        allowed_chars = self._build_character_set()

        password_chars = []
        for i in range(self.length):
            random_char = random.choice(allowed_chars)
            password_chars.append(random_char)

        password = ''.join(password_chars)
        return password


def get_user_input():
    """
    Get password generation preferences from user.

    Returns:
        tuple: (length, uppercase, lowercase, digits, special_char)

    Raises:
        ValueError: If length input is not a valid positive integer.
    """

    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Please enter the desired password length: "))
            if length <= 0:
                print("Length must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    uppercase = input("Include uppercase? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase? y/n: ").lower() == 'y'
    digits = input("Include digits? y/n: ").lower() == 'y'
    special_char = input("Include special char? y/n: ").lower() == 'y'

    if not any([uppercase, lowercase, digits, special_char]):
        print("You must select at least one character type!")
        return get_user_input()

    return length, uppercase, lowercase, digits, special_char


def main():
    """Main function to run the password generator."""

    length, uppercase, lowercase, digits, special_char = get_user_input()

    try:
        generator = PasswordGenerator(
            length, uppercase, lowercase, digits, special_char)
        password = generator.generate_password()
        print(f"\nYour password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
