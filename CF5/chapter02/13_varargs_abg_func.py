def get_average(*numbers):
    if not numbers:
        return "No number provided!"

    average = sum(numbers) / len(numbers)
    return average


def main():
    list_of_nums = [10, 20, 15]
    print(f"The average is: {get_average(*list_of_nums)}")


if __name__ == '__main__':
    main()
