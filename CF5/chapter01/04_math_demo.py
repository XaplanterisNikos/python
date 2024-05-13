import math

name = "Alice"
age = 20

print("Cf")
print("PI =",math.pi)

print("String concat")

# print(name + " is" + age + " years old") # TypeError
print(name + " is " + str(age) + " years old")


#Pyhton 2 style
print("Python 2 style")
print("PI= %6.2f" %math.pi)
print("%s is %d years old" %(name,age))
print("-----------")

#python 3 style using string format
print("Python 3 style using format")
print("Age is {0:2d}".format(age))
print("Pi = {0:.3f}".format(math.pi))
print("Pi = {0:.3f} and age = {1}".format(math.pi,age), end='')
print(" years old.")

print("{0:*^10}:{1:>20}".format(name,age))

# Python 3 style using f_strings and variables interpolation
print(f"{name} us {age} tears old.")
