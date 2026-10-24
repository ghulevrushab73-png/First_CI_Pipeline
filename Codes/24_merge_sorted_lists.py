def merge_sorted_lists(list1, list2):
    # Create an empty list to store the merged result.
    result = []

    # Use two indexes to track elements in both lists.
    i = 0
    j = 0

    # Compare elements and add the smaller one first.
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Add any remaining elements from the first list.
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # Add any remaining elements from the second list.
    while j < len(list2):
        result.append(list2[j])
        j += 1

    # Return the merged sorted list.
    return result


if __name__ == "__main__":
    first = [1, 3, 5]
    second = [2, 4, 6]

    print("Merged list:", merge_sorted_lists(first, second))
