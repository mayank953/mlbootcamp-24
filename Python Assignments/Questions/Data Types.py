def get_data_type(var):
    """
    Write a function that takes a variable as input and returns its data type.
    """
    pass

# Test cases
assert get_data_type(5) == int
assert get_data_type(5.0) == float
assert get_data_type("Hello") == str
assert get_data_type(True) == bool
assert get_data_type([1, 2, 3]) == list

def get_string_length(string):
    """
    Write a function that takes a string as input and returns its length.
    """
    pass

# Test cases
assert get_string_length("Hello") == 5
assert get_string_length("") == 0
assert get_string_length("Python") == 6
assert get_string_length("Data Science") == 12
assert get_string_length("12345") == 5

def is_even(num):
    """
    Write a function that takes a number as input and returns True if it is even, False otherwise.
    """
    pass

# Test cases
assert is_even(2) == True
assert is_even(3) == False
assert is_even(0) == True
assert is_even(100) == True
assert is_even(101) == False

def to_uppercase(string):
    """
    Write a function that takes a string as input and returns the string converted to uppercase.
    """
    pass

# Test cases
assert to_uppercase("hello") == "HELLO"
assert to_uppercase("Python") == "PYTHON"
assert to_uppercase("Data Science") == "DATA SCIENCE"
assert to_uppercase("") == ""

def get_last_element(lst):
    """
    Write a function that takes a list as input and returns the last element of the list.
    """
    pass

# Test cases
assert get_last_element([1, 2, 3, 4, 5]) == 5
assert get_last_element(["apple", "banana", "cherry"]) == "cherry"
assert get_last_element([]) == None

def is_prime(num):
    """
    Write a function that takes a number as input and returns True if it is a prime number, False otherwise.
    """
    pass

# Test cases
assert is_prime(2) == True
assert is_prime(3) == True
assert is_prime(4) == False
assert is_prime(5) == True
assert is_prime(6) == False

def is_palindrome(string):
    """
    Write a function that takes a string as input and returns True if it is a palindrome, False otherwise.
    """
    pass

# Test cases
assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert is_palindrome("madam") == True
assert is_palindrome("") == True

def sum_list(lst):
    """
    Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.
    """
    pass

# Test cases
assert sum_list([1, 2, 3, 4, 5]) == 15
assert sum_list([-1, 0, 1]) == 0
assert sum_list([]) == 0

def reverse_string(string):
    """
    Write a function that takes a string as input and returns the string reversed.
    """
    pass

# Test cases
assert reverse_string("hello") == "olleh"
assert reverse_string("Python") == "nohtyP"
assert reverse_string("") == ""

def filter_vowels(strings):
    """
    Write a function that takes a list of strings as input and returns a new list containing only the strings that start with a vowel.
    """
    pass

# Test cases
assert filter_vowels(["apple", "banana", "cherry", "orange", "pear"]) == ["apple", "orange"]
assert filter_vowels(["hello", "world"]) == []
assert filter_vowels([]) == []
