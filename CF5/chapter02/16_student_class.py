class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


def main():
    p = Student('Bob', 'M.')
    print(p.firstname)
    print(p.lastname)


if __name__ == '__main__':
    main()
