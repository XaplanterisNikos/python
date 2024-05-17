# Fibonachi Sequence
# 0 , 1 , 1, 2 , 3 , 5 , 8 , 13 , 21
def main():
    n = int(input("Enter a number: "))
    a = 0
    b = 1
    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b

    print(f"The {n}th Fibonacci number is: {b}")


if __name__ == '__main__':
    main()
