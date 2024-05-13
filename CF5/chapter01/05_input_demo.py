# input() demo

name = input("Please insert your name:")
print("Hello ",name ,"!")

year_of_birth = int(input("Please enter the year of birth:"))
#year_of_birth = int(year_of_birth)

print(type(year_of_birth))

print("You are ", 2024 - year_of_birth , " years old")

height = float(input("Please enter your height in cm"))
print("You are ", height/100 , "meters tall")
