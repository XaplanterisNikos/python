def print_cities(*cities, sep=", " , end='\n'):
    if not cities:
        print('No cities provided!')
    else:
        print('Cities:', sep.join(cities), end=end)


def main():
    print_cities("Athens", "Paris", "London")
    print_cities("London")
    print_cities()
    print("---------")
    print_cities("Athens", "Paris", "London",sep='\t',end='.')
    


if __name__ == '__main__':
    main()