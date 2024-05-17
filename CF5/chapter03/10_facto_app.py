def calculate_factorial(n):
    # Factorial (n): 1*2*3*4*....*n
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    n = int(input('Enter a number: '))
    print(f'Factorial of {n} is {calculate_factorial(n)}')


if __name__ == '__main__':
    main()
