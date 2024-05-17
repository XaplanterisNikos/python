def calculate_sum_and_product(upper_bound):
    total_sum = 0
    total_product = 1

    for i in range(1, upper_bound + 1):
        total_sum += i
        total_product *= i

    return total_sum, total_product


def main():
    upper_bound = int(input("Enter upper bound of numbers: "))
    total_sum, total_product = calculate_sum_and_product(upper_bound)
    print(f"Total sum: {total_sum}")
    print(f"Total product: {total_product}")


if __name__ == '__main__':
    main()