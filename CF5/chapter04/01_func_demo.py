# Type Annotations for Parameters (a: float | int)
# Return type Annotation (-> float | int)
def my_add(a: float | int, b: float | int) -> float | int:
    """
    Adds two numbers and returns the result
    Parameters
    ----------
    a (int, float): The first number to add
    b (int, float): The second number to add

    Returns
    -------
    int | float : The sum of two numbers

    Raises:
    TypeError : If `a` or `b` are not integers
    """
    if not (isinstance(a, (int,float)) and (isinstance(b, (int,float)))):
        raise TypeError("Both a nad b must intereger of floats")
    return a + b


def main():
    # Testing my function
    print(my_add(10, 20))
    print(my_add(5, 8.3))

    try:
        my_add("hello","cf")
    except TypeError as e:
        print(e)

    print("Annotations :" , my_add.__annotations__)
    print("Docs: ", my_add.__doc__)
    print("----------------")
    help(my_add)


if __name__ == '__main__':
    main()
