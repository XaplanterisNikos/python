import random


def get_user_quess():
    return int(input("Please insert an int: "))


def check_guess(secret, guess):
    if guess == secret:
        print("Bingo!! secret number : ", secret)
        return True
    elif abs(guess - secret) <= 5:
        print("Hot")
    else:
        print("Cold")
    return False


def main():
    secret_number = random.randint(1, 10)
    MAX_TRIES = 5
    tries = 1
    print("secret_number : ", secret_number)

    while tries < MAX_TRIES:
        guess = get_user_quess()
        if check_guess(secret_number, guess) :
            break
        tries += 1

        if tries == MAX_TRIES:
            print("You reached max tries!")

if __name__ == '__main__':
    main()
