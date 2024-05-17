def process_character():
    ch = input("Please insert a char: ")

    while ch != "#":
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")

    print("Good bye!")


def process_character2():
    ch = input("Please insert a char: ")

    while True:
        ch = input("Please insert a char: ")
        if ch == "#":
            break
        print(ch, ":", ord(ch))

    print("Good bye!")
