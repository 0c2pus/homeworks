"""
Unit tests for chpasswd module.
"""

import unittest
from chpasswd import check_password_requirements


class TestPasswordRequirements(unittest.TestCase):
    """Test cases for check_password_requirements function."""

    def test_valid_password(self):
        """Test valid password meeting all requirements."""
        result = check_password_requirements("Abc123!@")
        self.assertTrue(result)

    def test_password_too_short(self):
        """Test password shorter than 8 characters."""
        result = check_password_requirements("Ab1!")
        self.assertFalse(result)

    def test_no_uppercase(self):
        """Test password without uppercase letter."""
        result = check_password_requirements("abc12345!")
        self.assertFalse(result)

    def test_no_lowercase(self):
        """Test password without lowercase letter."""
        result = check_password_requirements("ABC12345!")
        self.assertFalse(result)

    def test_no_digits(self):
        """Test password without digits."""
        result = check_password_requirements("Abcdefgh!")
        self.assertFalse(result)

    def test_no_special_chars(self):
        """Test password without special characters."""
        result = check_password_requirements("Abcd1234")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
