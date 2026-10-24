import importlib

# Import Program 28.
module = importlib.import_module("28_set_intersection")

# Get the function to test.
set_intersection = module.set_intersection


# Test 1: Find common elements in two lists.
def test_common_elements():
    assert set_intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


# Test 2: No common elements.
def test_no_common_elements():
    assert set_intersection([1, 2], [3, 4]) == []


# Test 3: Both lists are empty.
def test_both_lists_empty():
    assert set_intersection([], []) == []


# Test 4: Find common elements when one list is empty.
def test_one_list_empty():
    assert set_intersection([1, 2, 3], []) == []


# Test 5: Avoid duplicate common elements.
def test_duplicate_elements():
    assert set_intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3]
