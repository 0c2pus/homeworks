# Password Generator Project

Secure random password generator for Linux users with customizable length (8-128 characters).

## Project Structure
```
password_generator/
├── passwd_gen.py           # Main password generator module
├── test_passwd_gen.py      # Unit tests
├── requirements.txt        # Dependencies
├── README.md              # This file
└── venv/                  # Virtual environment (not in submission)
```

## Features

- Generate passwords from 8 to 128 characters
- Guarantees at least one of each:
  - Lowercase letter
  - Uppercase letter
  - Digit
  - Special character
- Input validation
- Comprehensive unit tests (17 tests)

## Setup Instructions (macOS)

### 1. Create virtual environment
```bash
python3 -m venv venv
```

### 2. Activate virtual environment
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Verify installation
```bash
pip3 list
```

## Usage

### Run the password generator
```bash
python3 passwd_gen.py
```

**Example:**
```
Welcome to the Linux User Password Generator!
Please type number from 8 to 128 range
Please enter the desired password length: 16
16 is valid
Generated password: aB3$xY9zK2mN5pQ7
```

## Running Tests

### Run all tests
```bash
python3 -m unittest test_passwd_gen.py -v
```

Expected output:
```
test_empty_string ... ok
test_length_too_long ... ok
test_length_too_short ... ok
...
Ran 17 tests in 0.005s

OK
```

### Run specific test class
```bash
python3 -m unittest test_passwd_gen.TestValidatePasswordLength -v
```

### Run specific test
```bash
python3 -m unittest test_passwd_gen.TestValidatePasswordLength.test_valid_length -v
```

## Code Quality Checks

### Check code style with flake8
```bash
python3 -m flake8 passwd_gen.py test_passwd_gen.py
```

No output means no style violations found.

### Auto-fix style issues
```bash
autopep8 --in-place --aggressive --aggressive passwd_gen.py
```

## Test Coverage

### TestValidatePasswordLength (7 tests)
- Valid length input
- Length too short (< 8)
- Length too long (> 128)
- Non-numeric input
- Empty string input
- Minimum valid length (8)
- Maximum valid length (128)

### TestGeneratePassword (10 tests)
- Correct password length
- Contains lowercase letter
- Contains uppercase letter
- Contains digit
- Contains special character
- Invalid length too short
- Invalid length too long
- Minimum length generation (8)
- Maximum length generation (128)
- Invalid type handling

**Total: 17 tests** ✅

## Deactivate Virtual Environment
```bash
deactivate
```

## Requirements

- Python 3.7+
- pip3

## Dependencies

- flake8 (for code linting)
- autopep8 (for auto-formatting)

## Author

DevOps Student - Homework Assignment

## Version

1.0.0