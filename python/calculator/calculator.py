"""
Calculator module for basic arithmetic operations.

This module provides functions for addition, subtraction,
multiplication, and division.
"""


def add_numbers(a, b):
    """
    Returns the sum of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.

    Examples:
        >>> add_numbers(2, 3)
        5
        >>> add_numbers(-1, 1)
        0
    """
    return a + b


def subtract_numbers(a, b):
    """
    Returns the difference between two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a minus b.
    Examples:
        >>> subtract_numbers(10, 5)
        5
        >>> subtract_numbers(-1, 1)
        -2
    """
    return a - b


def multiply_numbers(a, b):
    """
    Returns the product of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a multiplied by b.
    Examples:
        >>> multiply_numbers(2, 2)
        4
        >>> multiply_numbers(-2, 2)
        -4
    """
    return a * b


def divide_numbers(a, b):
    """
    Returns the quotient of two numbers.
    If division by zero occurs, returns 'Error'.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float or str: The result of a divided by b, or 'Error' if b is zero.
     Examples:
        >>> divide_numbers(8, 2)
        4
        >>> divide_numbers(-8, 2)
        -4
    """
    if b == 0:
        return "Error"
    return a / b


def main():
    """
    Main function to run the calculator program.

    Handles user input for two numbers and the operation choice.
    Prints the result of the selected arithmetic operation.
    """
    print("Welcome to the Calculator Program!")

    try:
        num1 = float(input("Please enter the first number: "))
        num2 = float(input("Please enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        return

    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = add_numbers(num1, num2)
        print(f"The result of Addition is: {result}")
    elif choice == "2":
        result = subtract_numbers(num1, num2)
        print(f"The result of Subtraction is: {result}")
    elif choice == "3":
        result = multiply_numbers(num1, num2)
        print(f"The result of Multiplication is: {result}")
    elif choice == "4":
        result = divide_numbers(num1, num2)
        print(f"The result of Division is: {result}")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
