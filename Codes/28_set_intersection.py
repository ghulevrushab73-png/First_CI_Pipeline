def set_intersection(first, second):
    # Convert the second collection into a set for quick lookup.
    second_set = set(second)

    # Store common elements without duplicates.
    result = []

    # Find elements that appear in both collections.
    for item in first:
        if item in second_set and item not in result:
            result.append(item)

    # Return the common elements.
    return result


if __name__ == "__main__":
    first = [1, 2, 3, 4]
    second = [3, 4, 5, 6]

    print("Common elements:", set_intersection(first, second))
