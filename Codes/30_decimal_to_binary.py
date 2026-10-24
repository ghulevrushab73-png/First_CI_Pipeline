def decimal_to_binary(number):
    # Handle zero separately.
    if number == 0:
        return "0"

    # Remember whether the number is negative.
    is_negative = number < 0
    number = abs(number)

    # Store binary digits in reverse order.
    binary = ""

    # Repeatedly divide the number by 2.
    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number //= 2

    # Add the negative sign if necessary.
    if is_negative:
        binary = "-" + binary

    # Return the binary representation as a string.
    return binary


if __name__ == "__main__":
    number = int(input("Enter a decimal number: "))
    print("Binary representation:", decimal_to_binary(number))
