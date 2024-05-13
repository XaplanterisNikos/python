# input demo

name = input("Please enter your name : ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
is_student = input("Are you student? (yes/no)").lower() == 'yes'

print("Hello {}!".format(name))

if is_student:
    print("You are a student")
else:
    print("You are not student")

print("Your age is {}, and your height is {:.2f}".format(age,height))