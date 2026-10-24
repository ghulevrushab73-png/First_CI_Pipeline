import importlib

# Import the Program 24 module.
module = importlib.import_module("24_merge_sorted_lists")

# Get the function to test.
merge_sorted_lists = module.merge_sorted_lists


# Test 1: Merge two ordinary sorted lists.
def test_merge_sorted_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


# Test 2: Merge when the first list is empty.
def test_first_list_empty():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


# Test 3: Merge when the second list is empty.
def test_second_list_empty():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


# Test 4: Merge two empty lists.
def test_both_lists_empty():
    assert merge_sorted_lists([], []) == []


# Test 5: Merge lists containing duplicate values.
def test_duplicate_values():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]
