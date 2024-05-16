# List if fruits

fruits_lists = ["Banana","Orange","Mango","Grapes"] # List

# The fruits we want to check for
fruit_to_check = "Apple"

# Search for the fruit in the list
for fruit in fruits_lists:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list")
        break
else:
    print(f"{fruit_to_check} is not in the list")




# The fruits we want to check for
fruit_to_check = "Mango"

# Search for the fruit in the list
for fruit in fruits_lists:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list")
        break
else:
    print(f"{fruit_to_check} is not in the list")

# Pythonic and Powerful
print()
print("Why do Python deve never get lost?")
print("Beacause they always know where 'in' is!")
fruit_to_check = "Mango"
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits_lists else 'not in'} the list")

# simple approach
if fruit_to_check in fruit_to_check:
    print("Bingo!")