def is_armstrong(number):
    # Armstrong numbers cannot be negative.
    if number < 0:
        return False

    # Convert the number into a string to process its digits.
    digits = str(number)
    power = len(digits)

    # Calculate the sum of each digit raised to the number of digits.
    total = 0
    for digit in digits:
        total += int(digit) ** power

    # Return True if the sum equals the original number.
    return total == number


if __name__ == "__main__":
    number = int(input("Enter a number: "))

    if is_armstrong(number):
        print(number, "is an Armstrong number.")
    else:
        print(number, "is not an Armstrong number.")
