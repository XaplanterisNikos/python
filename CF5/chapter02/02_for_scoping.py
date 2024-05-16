# understanding range() function

# range(start,stop,step)
# defaults (start = 0, step=1)

a = range(0,10,1)
print(f"a:{a}") # range(0,10)
print(f"type(a): {type(a)}")

# Basic loop 0 to 9 
print("Basic loop from 0 to 9")
for i in range(10):
    print(i,end=' ')
print('\n')

# Loop with a break statment
print("Loop with a break statment")
for i in range(10):
    if i ==5:
        break
    print(i,end=' ')
print('\n')

# Loop with a continue statment
print("Loop with a continue statment")
for i in range(10):
    if i == 5:
        continue
    print(i,end=' ')
print('\n')

# Loop with a break statment and else block
print("Loop with a break statment and else block")
for i in range(10):
    if i == 5:
        break
    print(i,end=' ')
else:
    print("Loop ended normally")
print('\n')

# Nested loops example
print("Nested loops")
for i in range(1,4):
    for j in range(1,4):
        print(f"{i} * {j} = {i*j}", end=' | ')
    print()
print()

# Using range with negative step
print("Using range with negative step")
for i in range(10,0,-2):
    print(i,end=' ')
print('\n')