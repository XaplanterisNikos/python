def get_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


def get_sum(num1, num2):
    return num1 + num2


def main():
    n1 = 10
    n2 = 20
    n3 = 30

    average = get_average(n1, n2, n3)
    print(average)

    my_sum = get_sum(n1,n2)
    print(my_sum)

    my_sum = get_sum("Hello ", " Friends")
    print(my_sum)


if __name__ == '__main__':
    main()
