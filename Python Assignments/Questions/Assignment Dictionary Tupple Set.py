# Question 1: Counting Occurrences of Characters in a String and Storing in a Dictionary

def count_characters(string):
    """
    Design a Python function named `count_characters` to count the occurrences of each character in a string and store the counts in a dictionary.

    Parameters:
    - string: Input string (str)

    Returns:
    - Dictionary containing counts of each character (dict)

    Test Cases:
    Test Case 1:
    assert count_characters("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    Test Case 2:
    assert count_characters("hello world") == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 2: Merging Two Lists into a Dictionary

def merge_lists_to_dictionary(keys, values):
    """
    Design a Python function named `merge_lists_to_dictionary` to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.

    Parameters:
    - keys: List of keys (list)
    - values: List of values (list)

    Returns:
    - Dictionary containing merged key-value pairs (dict)

    Test Cases:
    Test Case 1:
    assert merge_lists_to_dictionary(['a', 'b', 'c'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}

    Test Case 2:
    assert merge_lists_to_dictionary(['x', 'y', 'z'], [10, 20, 30]) == {'x': 10, 'y': 20, 'z': 30}

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 3: Removing Duplicates from a List and Converting to Tuple

def remove_duplicates_and_convert_to_tuple(lst):
    """
    Design a Python function named `remove_duplicates_and_convert_to_tuple` to remove duplicates from a list, and then convert it into a tuple.

    Parameters:
    - lst: Input list (list)

    Returns:
    - Tuple containing unique elements from the input list (tuple)

    Test Cases:
    Test Case 1:
    assert remove_duplicates_and_convert_to_tuple([1, 2, 2, 3, 4, 4, 5]) == (1, 2, 3, 4, 5)

    Test Case 2:
    assert remove_duplicates_and_convert_to_tuple(['a', 'b', 'a', 'c', 'd', 'b']) == ('a', 'b', 'c', 'd')

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 4: Checking Subset Relationship Between Sets

def is_subset(set1, set2):
    """
    Design a Python function named `is_subset` to check if one set is a subset of another.

    Parameters:
    - set1: First set (set)
    - set2: Second set (set)

    Returns:
    - True if set1 is a subset of set2, False otherwise (bool)

    Test Cases:
    Test Case 1:
    assert is_subset({1, 2, 3}, {1, 2, 3, 4, 5}) == True

    Test Case 2:
    assert is_subset({'a', 'b', 'c'}, {'a', 'b', 'c', 'd', 'e'}) == True

    Test Case 3:
    assert is_subset({1, 2, 3}, {4, 5, 6}) == False

    Test Case 4:
    assert is_subset({'x', 'y', 'z'}, {'a', 'b', 'c'}) == False

    Test Case 5:
    assert is_subset({'a', 'b', 'c'}, {'c', 'b', 'a'}) == True

    Test Case 6:
    assert is_subset(set(), {1, 2, 3}) == True

    Test Case 7:
    assert is_subset({1, 2, 3}, set()) == False

    Test Case 8:
    assert is_subset(set(), set()) == True

    Test Case 9:
    # Additional test cases can be added here
    pass


# Question 5: Merging Multiple Dictionaries into One

def merge_multiple_dictionaries(*dicts):
    """
    Design a Python function named `merge_multiple_dictionaries` to merge multiple dictionaries into one.

    Parameters:
    - dicts: Variable number of dictionaries (dict)

    Returns:
    - Merged dictionary containing all key-value pairs from input dictionaries (dict)

    Test Cases:
    Test Case 1:
    assert merge_multiple_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    Test Case 2:
    assert merge_multiple_dictionaries({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50}) == {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 6: Finding Intersection of Multiple Sets

def find_intersection_of_sets(*sets):
    """
    Design a Python function named `find_intersection_of_sets` to find the intersection of multiple sets.

    Parameters:
    - sets: Variable number of sets (set)

    Returns:
    - Set containing common elements present in all input sets (set)

    Test Cases:
    Test Case 1:
    assert find_intersection_of_sets({1, 2, 3}, {2, 3, 4}, {3, 4, 5}) == {3}

    Test Case 2:
    assert find_intersection_of_sets({'a', 'b', 'c'}, {'b', 'c', 'd'}, {'c', 'd', 'e'}) == {'c'}

    Test Case 3:
    assert find_intersection_of_sets({1, 2, 3}, {4, 5, 6}) == set()

    Test Case 4:
    assert find_intersection_of_sets({'x', 'y', 'z'}, {'a', 'b', 'c'}, {'m', 'n', 'o'}) == set()

    Test Case 5:
    # Additional test cases can be added here
    pass


# Question 7: Counting Frequency of Words in a Sentence

def count_word_frequency(sentence):
    """
    Design a Python function named `count_word_frequency` to count the frequency of words in a sentence and store the counts in a dictionary.

    Parameters:
    - sentence: Input sentence (str)

    Returns:
    - Dictionary containing word frequencies (dict)

    Test Cases:
    Test Case 1:
    assert count_word_frequency("hello world hello") == {'hello': 2, 'world': 1}

    Test Case 2:
    assert count_word_frequency("the quick brown fox jumps over the lazy dog") == {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 8: Checking for Palindromic Tuples

def is_palindromic_tuple(tup):
    """
    Design a Python function named `is_palindromic_tuple` to check if a tuple is palindromic (reads the same forwards and backwards).

    Parameters:
    - tup: Input tuple (tuple)

    Returns:
    - True if the tuple is palindromic, False otherwise (bool)

    Test Cases:
    Test Case 1:
    assert is_palindromic_tuple((1, 2, 3, 2, 1)) == True

    Test Case 2:
    assert is_palindromic_tuple(('a', 'b', 'c', 'b', 'a')) == True

    Test Case 3:
    assert is_palindromic_tuple((1, 2, 3, 4, 5)) == False

    Test Case 4:
    assert is_palindromic_tuple(('x', 'y', 'z', 'x')) == False

    Test Case 5:
    assert is_palindromic_tuple(('a',)) == True

    Test Case 6:
    # Additional test cases can be added here
    pass


# Question 9: Implementing a Function to Merge Dictionaries with Overlapping Keys

def merge_dicts_with_overlapping_keys(dicts):
    """
    Design a Python function named `merge_dicts_with_overlapping_keys` to merge dictionaries with overlapping keys by summing their values.

    Parameters:
    - dicts: List of dictionaries (list)

    Returns:
    - Merged dictionary with summed values for overlapping keys (dict)

    Test Cases:
    Test Case 1:
    assert merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]) == {'a': 1, 'b': 5, 'c': 9, 'd': 6}

    Test Case 2:
    assert merge_dicts_with_overlapping_keys([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]) == {'x': 70, 'y': 50, 'z': 90}

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 10: Implementing a Function to Check if All Values in a Dictionary are Unique

def are_values_unique(dictionary):
    """
    Design a Python function named `are_values_unique` to check if all values in a dictionary are unique.

    Parameters:
    - dictionary: Input dictionary (dict)

    Returns:
    - True if all values are unique, False otherwise (bool)

    Test Cases:
    Test Case 1:
    assert are_values_unique({'a': 1, 'b': 2, 'c': 3}) == True

    Test Case 2:
    assert are_values_unique({'x': 1, 'y': 2, 'z': 2}) == False

    Test Case 3:
    # Additional test cases can be added here
    pass

