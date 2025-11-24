# Linux User Password Checker

Python script that checks if a Linux user exists, validates or generates a password, and verifies it meets security requirements.

## Project Structure
```
password_change_linux/
├── chpasswd.py              # Main script
├── pass_oop.py              # PasswordGenerator class
├── test_chpasswd.py         # Unit tests
├── requirements.txt         # Dependencies
├── README.md               # This file
└── venv/                   # Virtual environment (not in submission)
```

## Features

- Check if Linux user exists in the system
- Prompt for password or auto-generate secure password
- Validate password against requirements:
  - Minimum 8 characters
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 digit
  - At least 1 special character
- Auto-generation uses 12-character passwords with all character types

## Setup Instructions (macOS)

### 1. Create virtual environment
```bash
python3 -m venv venv
```

### 2. Activate virtual environment
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal.

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Verify installation
```bash
pip3 list
```

## Usage

### Run the script
```bash
python3 chpasswd.py
```

**Example interaction:**
```
Type your user name: root
Welcome: root
Please enter your password: [press Enter for auto-generate]

User: root
Password: aB3$xY9zK2mN
Password is correct!
```

**Note:** If you press Enter without typing a password, a secure 12-character password will be auto-generated.

## Running Tests

### Run all tests
```bash
python3 -m unittest test_chpasswd.py -v
```

Expected output:
```
test_no_digits ... ok
test_no_lowercase ... ok
test_no_special_chars ... ok
test_no_uppercase ... ok
test_password_too_short ... ok
test_valid_password ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### Run specific test
```bash
python3 -m unittest test_chpasswd.TestPasswordRequirements.test_valid_password -v
```

## Code Quality Checks

### Check code style with flake8
```bash
python3 -m flake8 chpasswd.py pass_oop.py test_chpasswd.py
```

No output means no style violations.

### Auto-fix style issues
```bash
python3 -m autopep8 --in-place --aggressive --aggressive chpasswd.py
```

## Test Coverage

**TestPasswordRequirements:** 6 tests
- Valid password (all requirements met)
- Password too short (< 8 characters)
- Missing uppercase letter
- Missing lowercase letter
- Missing digits
- Missing special characters

## Password Requirements

- **Length:** Minimum 8 characters
- **Uppercase:** At least 1 uppercase letter (A-Z)
- **Lowercase:** At least 1 lowercase letter (a-z)
- **Digits:** At least 1 digit (0-9)
- **Special:** At least 1 special character (!@#$%^&*...)

## Deactivate Virtual Environment
```bash
deactivate
```

## Requirements

- Python 3.7+
- macOS or Linux
- User must exist in the system

## Dependencies

- flake8 (code linting)
- autopep8 (auto-formatting)

## Author

DevOps Student - Homework Assignment

## Version

1.0.0