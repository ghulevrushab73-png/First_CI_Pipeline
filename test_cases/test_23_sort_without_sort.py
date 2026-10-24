import importlib

# Import the program.
module = importlib.import_module("23_sort_without_sort")

# Get the function to test.
bubble_sort = module.bubble_sort


# Test 1: Sort an ordinary list.
def test_sort_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


# Test 2: Sort an already sorted list.
def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


# Test 3: Sort an empty list.
def test_empty_list():
    assert bubble_sort([]) == []


# Test 4: Sort a list containing negative numbers.
def test_negative_numbers():
    assert bubble_sort([-3, 5, -1, 0]) == [-3, -1, 0, 5]


# Test 5: Check that the original list is unchanged.
def test_original_list_unchanged():
    numbers = [5, 2, 9, 1]
    bubble_sort(numbers)
    assert numbers == [5, 2, 9, 1]
