# range:(n) : 0.......(n-1)
# start:inclusive (start)
# end: exclusive (end -1)

# print odd numbers from 1 to 21
print("Java Style")

for i in range(22):
    if i % 2 !=0 :
        print(i, end=" ")
print()

# python style
print("Python Style")

for i in  range(1, 22, 2):
    print(i, end=" ")
print()