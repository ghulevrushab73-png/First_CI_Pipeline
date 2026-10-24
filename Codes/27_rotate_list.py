def rotate_list(items, k):
    # Return an empty list if there are no items.
    if not items:
        return []

    # Normalize k to handle rotations larger than the list.
    k = k % len(items)

    # Rotate the list to the right.
    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    k = 2

    print("Original list:", numbers)
    print("Rotated list:", rotate_list(numbers, k))
