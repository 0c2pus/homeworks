"""
Unit tests for password generator OOP module.
"""

import unittest
import string
from pass_oop import PasswordGenerator


class TestPasswordGeneratorInit(unittest.TestCase):
    """Test cases for PasswordGenerator initialization."""

    def test_valid_initialization(self):
        """Test valid generator initialization."""

        gen = PasswordGenerator(10, True, True, True, True)

        self.assertEqual(gen.length, 10)
        self.assertTrue(gen.include_uppercase)
        self.assertTrue(gen.include_lowercase)
        self.assertTrue(gen.include_digits)
        self.assertTrue(gen.include_special_char)

    def test_invalid_length_zero(self):
        """Test that length of 0 raises ValueError."""

        with self.assertRaises(ValueError):
            PasswordGenerator(0, True, True, True, True)

    def test_invalid_length_negative(self):
        """Test that negative length raises ValueError."""

        with self.assertRaises(ValueError):
            PasswordGenerator(-10, True, True, True, True)

    def test_invalid_length_string(self):
        """Test that string length raises ValueError."""

        with self.assertRaises(ValueError):
            PasswordGenerator("10", True, True, True, True)

    def test_no_character_types_selected(self):
        """Test that no character types raises ValueError."""

        with self.assertRaises(ValueError):
            PasswordGenerator(10, False, False, False, False)


class TestPasswordGeneratorGenerate(unittest.TestCase):
    """Test cases for password generation."""

    def test_password_length(self):
        """Test generated password has correct length."""

        gen = PasswordGenerator(15, True, True, True, True)
        password = gen.generate_password()
        self.assertEqual(len(password), 15)

    def test_uppercase_only(self):
        """Test password with uppercase letters only."""

        gen = PasswordGenerator(20, True, False, False, False)
        password = gen.generate_password()

        self.assertEqual(len(password), 20)
        self.assertTrue(all(c.isupper() for c in password))

    def test_lowercase_only(self):
        """Test password with lowercase letters only."""

        gen = PasswordGenerator(20, False, True, False, False)
        password = gen.generate_password()

        self.assertEqual(len(password), 20)
        self.assertTrue(all(c.islower() for c in password))

    def test_digits_only(self):
        """Test password with digits only."""

        gen = PasswordGenerator(20, False, False, True, False)
        password = gen.generate_password()

        self.assertEqual(len(password), 20)
        self.assertTrue(all(c.isdigit() for c in password))

    def test_special_chars_only(self):
        """Test password with special characters only."""

        gen = PasswordGenerator(20, False, False, False, True)
        password = gen.generate_password()

        self.assertEqual(len(password), 20)
        self.assertTrue(all(c in string.punctuation for c in password))

    def test_mixed_character_types(self):
        """Test password with all character types."""
        gen = PasswordGenerator(100, True, True, True, True)
        password = gen.generate_password()

        self.assertEqual(len(password), 100)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))


if __name__ == "__main__":
    unittest.main()
