"""
Unit tests for password generator module.

This module contains tests for password validation and generation functions.
"""

import unittest
import string
from passwd_gen import validate_password_length, generate_password


class TestValidatePasswordLength(unittest.TestCase):
    """Test cases for validate_password_length function."""

    def test_valid_length(self):
        """Test valid password length."""

        result = validate_password_length("16")
        self.assertEqual(result, 16)

    def test_length_too_short(self):
        """Test length less than 8."""

        result = validate_password_length("5")
        self.assertIsNone(result)

    def test_length_too_long(self):
        """Test length more than 128."""

        result = validate_password_length("130")
        self.assertIsNone(result)

    def test_not_a_number(self):
        """Test non-numeric input."""

        result = validate_password_length("abc")
        self.assertIsNone(result)

    def test_empty_string(self):
        """Test empty string input."""

        result = validate_password_length("")
        self.assertIsNone(result)

    def test_minimum_valid_length(self):
        """Test minimum valid length (8)."""

        result = validate_password_length("8")
        self.assertEqual(result, 8)

    def test_maximum_valid_length(self):
        """Test maximum valid length (128)."""

        result = validate_password_length("128")
        self.assertEqual(result, 128)


class TestGeneratePassword(unittest.TestCase):
    """Test cases for generate_password function."""

    def test_password_length(self):
        """Test that generated password has correct length."""

        password = generate_password(16)
        self.assertEqual(len(password), 16)

    def test_password_contains_lowercase(self):
        """Test password contains at least one lowercase letter."""

        password = generate_password(16)
        self.assertTrue(any(c.islower() for c in password))

    def test_password_contains_uppercase(self):
        """Test password contains at least one uppercase letter."""

        password = generate_password(20)
        self.assertTrue(any(c.isupper() for c in password))

    def test_password_contains_digit(self):
        """Test password contains at least one digit."""

        password = generate_password(12)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_password_contains_special_character(self):
        """Test password contains at least one special character."""

        password = generate_password(16)
        punctuation = string.punctuation
        self.assertTrue(any(c in punctuation for c in password))

    def test_invalid_length_too_short(self):
        """Test that length < 8 raises ValueError."""

        with self.assertRaises(ValueError):
            generate_password(5)

    def test_invalid_length_too_long(self):
        """Test that length > 128 raises ValueError."""

        with self.assertRaises(ValueError):
            generate_password(130)

    def test_minimum_length_password(self):
        """Test password generation with minimum length (8)."""

        password = generate_password(8)
        self.assertEqual(len(password), 8)

    def test_maximum_length_password(self):
        """Test password generation with maximum length (128)."""

        password = generate_password(128)
        self.assertEqual(len(password), 128)

    def test_invalid_type(self):
        """Test that non-integer type raises ValueError."""

        with self.assertRaises(ValueError):
            generate_password("16")


if __name__ == "__main__":
    unittest.main()
