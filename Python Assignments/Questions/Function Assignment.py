# Question 1: Implementing a Function to Calculate the Sum of Numbers in a List

def calculate_sum(numbers):
    """
    Design a Python function named `calculate_sum` to calculate the sum of numbers in a list.

    Parameters:
    - numbers: List of numbers (list)

    Returns:
    - Sum of numbers in the list (int or float)

    Test Cases:
    Test Case 1:
    assert calculate_sum([1, 2, 3, 4, 5]) == 15

    Test Case 2:
    assert calculate_sum([0.5, 1.5, 2.5, 3.5]) == 8.0

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 2: Implementing a Function to Calculate the Factorial of a Number

def calculate_factorial(n):
    """
    Design a Python function named `calculate_factorial` to calculate the factorial of a number.

    Parameters:
    - n: Number (int)

    Returns:
    - Factorial of the number (int)

    Test Cases:
    Test Case 1:
    assert calculate_factorial(5) == 120

    Test Case 2:
    assert calculate_factorial(10) == 3628800

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 3: Implementing a Function to Convert Celsius to Fahrenheit and Vice Versa

def convert_temperature(value, from_unit="C", to_unit="F"):
    """
    Design a Python function named `convert_temperature` to convert temperature between Celsius and Fahrenheit.

    Parameters:
    - value: Temperature value (float)
    - from_unit: Unit of input temperature ("C" for Celsius, "F" for Fahrenheit, default: "C")
    - to_unit: Unit of output temperature ("C" for Celsius, "F" for Fahrenheit, default: "F")

    Returns:
    - Converted temperature value (float)

    Test Cases:
    Test Case 1:
    assert convert_temperature(0) == 32.0
    assert convert_temperature(32, "F", "C") == 0.0

    Test Case 2:
    assert convert_temperature(100, "C", "F") == 212.0
    assert convert_temperature(212) == 100.0

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 4: Implementing a Function to Calculate Simple Interest

def calculate_simple_interest(principal, rate, time):
    """
    Design a Python function named `calculate_simple_interest` to calculate simple interest.

    Parameters:
    - principal: Principal amount (float)
    - rate: Interest rate (float)
    - time: Time period (float)

    Returns:
    - Simple interest (float)

    Test Cases:
    Test Case 1:
    assert calculate_simple_interest(1000, 5, 2) == 100.0

    Test Case 2:
    assert calculate_simple_interest(2000, 3.5, 3.5) == 245.0

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 5: Implementing a Function to Check Prime Numbers in a Range

def is_prime(number):
    """
    Design a Python function named `is_prime` to check if a number is prime.

    Parameters:
    - number: Number to check (int)

    Returns:
    - True if the number is prime, False otherwise (bool)

    Test Cases:
    Test Case 1:
    assert is_prime(7) == True

    Test Case 2:
    assert is_prime(10) == False

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 6: Implementing a Function to Calculate Compound Interest

def calculate_compound_interest(principal, rate, time, frequency=1):
    """
    Design a Python function named `calculate_compound_interest` to calculate compound interest.

    Parameters:
    - principal: Principal amount (float)
    - rate: Interest rate (float)
    - time: Time period (float)
    - frequency: Number of times interest is compounded per unit time (int, default: 1)

    Returns:
    - Compound interest (float)

    Test Cases:
    Test Case 1:
    assert calculate_compound_interest(1000, 5, 2, 1) == 102.5

    Test Case 2:
    assert calculate_compound_interest(2000, 3.5, 3.5, 2) == 267.47623338672085

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 7: Implementing a Function to Find the Largest Number in a List

def find_largest_number(numbers):
    """
    Design a Python function named `find_largest_number` to find the largest number in a list.

    Parameters:
    - numbers: List of numbers (list)

    Returns:
    - Largest number in the list (int or float)

    Test Cases:
    Test Case 1:
    assert find_largest_number([1, 3, 5, 7, 9]) == 9

    Test Case 2:
    assert find_largest_number([0.5, 1.5, 2.5, 3.5]) == 3.5

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 8: Implementing a Function to Find the Smallest Number in a List

def find_smallest_number(numbers):
    """
    Design a Python function named `find_smallest_number` to find the smallest number in a list.

    Parameters:
    - numbers: List of numbers (list)

    Returns:
    - Smallest number in the list (int or float)

    Test Cases:
    Test Case 1:
    assert find_smallest_number([1, 3, 5, 7, 9]) == 1

    Test Case 2:
    assert find_smallest_number([0.5, 1.5, 2.5, 3.5]) == 0.5

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 9: Implementing a Function to Sort a List of Numbers

def sort_numbers(numbers):
    """
    Design a Python function named `sort_numbers` to sort a list of numbers in ascending order.

    Parameters:
    - numbers: List of numbers (list)

    Returns:
    - Sorted list of numbers (list)

    Test Cases:
    Test Case 1:
    assert sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    Test Case 2:
    assert sort_numbers([0.5, 1.5, 0.1, 2.5, 3.5]) == [0.1, 0.5, 1.5, 2.5, 3.5]

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 10: Implementing a Function to Find the Median of a List of Numbers

def find_median(numbers):
    """
    Design a Python function named `find_median` to find the median of a list of numbers.

    Parameters:
    - numbers: List of numbers (list)

    Returns:
    - Median of the list of numbers (float)

    Test Cases:
    Test Case 1:
    assert find_median([1, 2, 3, 4, 5]) == 3

    Test Case 2:
    assert find_median([1, 2, 3, 4, 5, 6]) == 3.5

    Test Case 3:
    # Additional test cases can be added here
    pass

