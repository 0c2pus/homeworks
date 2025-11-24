# Calculator Project

Simple calculator with unit tests for DevOps course.

## Project Structure
```
calculator/
├── calculator.py          # Main calculator module
├── test_calculator.py     # Unit tests
├── requirements.txt       # Dependencies
├── venv/                  # Virtual environment (not included in submission)
└── README.md             # This file
```

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

## Running the Calculator
```bash
python3 calculator.py
```

Example:
```
Welcome to the Calculator Program!
Please enter the first number: 10
Please enter the second number: 5

Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter your choice (1-4): 1
The result of Addition is: 15.0
```

## Running Tests

Run all tests:
```bash
python3 -m unittest test_calculator.py -v
```

Run specific test class:
```bash
python3 -m unittest test_calculator.TestAddNumbers -v
```

## Code Quality Checks

Check code style with flake8:
```bash
python3 -m flake8 calculator.py test_calculator.py
```

Check code quality with pylint:
```bash
python3 -m pylint calculator.py
```

## Deactivate Virtual Environment
```bash
deactivate
```

## Test Coverage

- Addition: 4 tests ✓
- Subtraction: 4 tests ✓
- Multiplication: 4 tests ✓
- Division: 4 tests ✓

Total: 16 tests

## Requirements

- Python 3.7+
- pip3