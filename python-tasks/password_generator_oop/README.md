# Password Generator OOP Project

Object-Oriented password generator with customizable character sets.

## Project Structure
```
password_generator_oop/
├── password_generator_oop.py      # Main OOP module
├── test_password_generator_oop.py # Unit tests
├── requirements.txt               # Dependencies
├── README.md                      # This file
└── venv/                          # Virtual environment
```

## Features

- Object-Oriented Design (PasswordGenerator class)
- Customizable character sets:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (!@#$...)
- Input validation
- Comprehensive unit tests (18 tests)

## Setup Instructions (macOS)

### 1. Create virtual environment
```bash
python3 -m venv venv
```

### 2. Activate virtual environment
```bash
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip3 install -r requirements.txt
```

## Usage

### Interactive Mode
```bash
python3 password_generator_oop.py
```

**Example:**
```
Welcome to the Password Generator!
Please enter the desired password length: 16
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y

Your password: aB3$xY9zK2mN5pQ7
```

### Programmatic Usage
```python
from password_generator_oop import PasswordGenerator

# Create generator
gen = PasswordGenerator(
    length=16,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_special_char=True
)

# Generate password
password = gen.generate_password()
print(password)
```

## Running Tests

### Run all tests
```bash
python3 -m unittest test_password_generator_oop.py -v
```

### Run specific test class
```bash
python3 -m unittest test_password_generator_oop.TestPasswordGeneratorInit -v
```

## Code Quality
```bash
python3 -m flake8 password_generator_oop.py test_password_generator_oop.py
```

## Test Coverage

- **TestPasswordGeneratorInit**: 5 tests
- **TestPasswordGeneratorGenerate**: 10 tests  
- **TestPasswordGeneratorBuildCharacterSet**: 3 tests

**Total: 18 tests** ✅

## Requirements

- Python 3.7+
- pip3

## Author

DevOps Student - Homework Assignment

## Version

1.0.0