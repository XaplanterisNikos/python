# import my_calculations

from my_calculations import my_add_function as my_add, num1

def main():

    num2 = 20
    res = my_add(num2,num1)
    print(f"res = {res}")

if __name__ == '__main__':
    main()