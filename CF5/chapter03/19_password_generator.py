# password generator
import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")


def generate_password():
    password_lenght = int(input("Enter the password length: "))
    random.shuffle(characters)
    password = [] # list

    for i in range(password_lenght):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print(f"Your password is: {password}")


def main():
    while True:
        option = input("Would you like to generate a password? [Y/N] ")

        if option.lower() == "y":
            generate_password()
        elif option.lower() == "n":
            print("Thank you!")
            break
        else:
            print("Please enter a valid option")


if __name__ == '__main__':
    main()
