def is_square(length, width):
    return length == width
    """
    Checks if a rectangle is a squar
    
    Args:
    lenght: The lenght of the ractangle.
    width: The width of the ractangle.
    
    Returns:
    bool:True if the rectangle is square , False otherwise.
    """


def main():
    lenght = int(input("Please enter the length of the rectangle : "))
    width = int(input("Please enter the width of the rectangle : "))

    if is_square(lenght, width):
        print("The rectangle is square")
    else:
        print("The rectangle is not square")


if __name__ == '__main__':
    main()