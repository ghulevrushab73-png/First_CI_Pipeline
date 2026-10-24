def bubble_sort(numbers):
    # Create a copy so the original list remains unchanged.
    result = numbers.copy()

    # Compare adjacent elements and swap them if needed.
    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    # Return the new list in ascending order.
    return result


# Run the program directly.
if __name__ == "__main__":
    numbers = [5, 2, 9, 1]
    print("Original list:", numbers)
    print("Sorted list:", bubble_sort(numbers))
