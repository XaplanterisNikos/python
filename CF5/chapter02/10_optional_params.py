def get_formatted_date(day=1, month=1, year=2000):
    return f'{day:02d}/{month:02d}/{year:4d}'


def main():
    print(get_formatted_date())
    print(get_formatted_date(10))
    print(get_formatted_date(10, 5))
    print(get_formatted_date(10, 5, 2015))
    print(get_formatted_date(month=10, day=25))


if __name__ == '__main__':
    main()
