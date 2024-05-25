# Question 1: Implementing a Function to Remove Duplicates from a List

def remove_duplicates(lst):
    """
    Design a Python function named `remove_duplicates` to remove duplicates from a list.

    Parameters:
    - lst: Input list (list)

    Returns:
    - List containing unique elements (list)

    Test Cases:
    Test Case 1:
    assert remove_duplicates([1, 2, 3, 2, 4, 3, 5]) == [1, 2, 3, 4, 5]

    Test Case 2:
    assert remove_duplicates(['a', 'b', 'c', 'a', 'd', 'b']) == ['a', 'b', 'c', 'd']

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 2: Implementing a Function to Flatten a Nested List

def flatten_list(nested_lst):
    """
    Design a Python function named `flatten_list` to flatten a nested list into a single list.

    Parameters:
    - nested_lst: Nested list (list)

    Returns:
    - Flattened list (list)

    Test Cases:
    Test Case 1:
    assert flatten_list([[1, 2, 3], [4, 5], [6, 7, 8]]) == [1, 2, 3, 4, 5, 6, 7, 8]

    Test Case 2:
    assert flatten_list([[1, 2], [3, [4, 5]], [6], [7, 8, [9, 10]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 3: Implementing a Function to Split a List into Even and Odd Elements

def split_even_odd(lst):
    """
    Design a Python function named `split_even_odd` to split a list into two lists containing even and odd elements respectively.

    Parameters:
    - lst: Input list (list)

    Returns:
    - Tuple containing two lists - one with even elements and one with odd elements (tuple)

    Test Cases:
    Test Case 1:
    assert split_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

    Test Case 2:
    assert split_even_odd([11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == ([22, 44, 66, 88, 100], [11, 33, 55, 77, 99])

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 4: Implementing a Function to Rotate a List

def rotate_list(lst, k):
    """
    Design a Python function named `rotate_list` to rotate a list to the right by k steps.

    Parameters:
    - lst: Input list (list)
    - k: Number of steps to rotate (int)

    Returns:
    - Rotated list (list)

    Test Cases:
    Test Case 1:
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

    Test Case 2:
    assert rotate_list(['a', 'b', 'c', 'd', 'e'], 3) == ['c', 'd', 'e', 'a', 'b']

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 5: Implementing a Function to Merge Two Sorted Lists

def merge_sorted_lists(lst1, lst2):
    """
    Design a Python function named `merge_sorted_lists` to merge two sorted lists into a single sorted list.

    Parameters:
    - lst1: First sorted list (list)
    - lst2: Second sorted list (list)

    Returns:
    - Merged sorted list (list)

    Test Cases:
    Test Case 1:
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    Test Case 2:
    assert merge_sorted_lists(['a', 'c', 'e'], ['b', 'd', 'f']) == ['a', 'b', 'c', 'd', 'e', 'f']

    Test Case 3:
    # Additional test cases can be added here
    pass




# Question 6: Implementing a Function to Remove Consecutive Duplicates from a List

def remove_consecutive_duplicates(lst):
    """
    Design a Python function named `remove_consecutive_duplicates` to remove consecutive duplicates from a list.

    Parameters:
    - lst: Input list (list)

    Returns:
    - List with consecutive duplicates removed (list)

    Test Cases:
    Test Case 1:
    assert remove_consecutive_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == [1, 2, 3, 4]

    Test Case 2:
    assert remove_consecutive_duplicates(['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'e', 'e']) == ['a', 'b', 'c', 'd', 'e']

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 7: Implementing a Function to Shuffle a List

import random

def shuffle_list(lst):
    """
    Design a Python function named `shuffle_list` to shuffle the elements of a list.

    Parameters:
    - lst: Input list (list)

    Returns:
    - Shuffled list (list)

    Test Cases:
    Test Case 1:
    assert shuffle_list([1, 2, 3, 4, 5]) != [1, 2, 3, 4, 5]

    Test Case 2:
    assert shuffle_list(['a', 'b', 'c', 'd', 'e']) != ['a', 'b', 'c', 'd', 'e']

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 8: Implementing a Function to Partition a List into Sublists of Given Size

def partition_list(lst, size):
    """
    Design a Python function named `partition_list` to partition a list into sublists of a given size.

    Parameters:
    - lst: Input list (list)
    - size: Size of each sublist (int)

    Returns:
    - List of sublists (list)

    Test Cases:
    Test Case 1:
    assert partition_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    Test Case 2:
    assert partition_list(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2) == [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g']]

    Test Case 3:
    # Additional test cases can be added here
    pass


# Question 9: Implementing a Function to Check if a List is Palindromic

def is_palindromic_list(lst):
    """
    Design a Python function named `is_palindromic_list` to check if a list is palindromic (reads the same forwards and backwards).

    Parameters:
    - lst: Input list (list)

    Returns:
    - True if the list is palindromic, False otherwise (bool)

    Test Cases:
    Test Case 1:
    assert is_palindromic_list([1, 2, 3, 2, 1]) == True

    Test Case 2:
    assert is_palindromic_list(['a', 'b', 'c', 'b', 'a']) == True

    Test Case 3:
    assert is_palindromic_list([1, 2, 3, 4, 5]) == False

    Test Case 4:
    assert is_palindromic_list(['x', 'y', 'z', 'x']) == False

    Test Case 5:
    assert is_palindromic_list(['a']) == True

    Test Case 6:
    # Additional test cases can be added here
    pass


# Question 10: Implementing a Function to Remove Items at Even Indices

def remove_items_at_even_indices(lst):
    """
    Design a Python function named `remove_items_at_even_indices` to remove items at even indices from a list.

    Parameters:
    - lst: Input list (list)

    Returns:
    - List with items at even indices removed (list)

    Test Cases:
    Test Case 1:
    assert remove_items_at_even_indices([1, 2, 3, 4, 5]) == [2, 4]

    Test Case 2:
    assert remove_items_at_even_indices(['a', 'b', 'c', 'd', 'e', 'f']) == ['b', 'd', 'f']

    Test Case 3:
    # Additional test cases can be added here
    pass

