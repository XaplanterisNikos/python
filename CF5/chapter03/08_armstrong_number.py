def is_armstrong_number(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return n == total


def main():
    # Example : 371 = 3^3 + 7^3 + 1^3
    num = int(input("Enter a number: "))

    if is_armstrong_number(num):
        print("The number is an armstrong.")
    else:
        print("The number is not an armstrong.")


if __name__ == '__main__':
    main()
