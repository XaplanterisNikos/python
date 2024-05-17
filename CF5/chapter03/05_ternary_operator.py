def compare_integers(a, b):
    if a == b:
        print("The numbers are equal")
    elif a > b:
        print("The first number is greater than the second number")
    else:
        print("The second number is greater than the first number")


def main():
    a = 10
    b = 20

    compare_integers(a, b)

    # 1. Ternary operator (simple example)
    result = "Positive" if a > 0 else "Non-positive"
    print(result)

    # 2.Ternary operator (full example)
    result = (
        "The numbers are equal" if a == b else
        "The first number is greater than the second number" if a > b else
        "The second number is greater than the first number"
    )
    print(result)


if __name__ == "__main__":
    main()
