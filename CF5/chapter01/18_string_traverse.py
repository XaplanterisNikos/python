message = "Coding Factory"

#zero index
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

# immutable
# message[0] = 'c'

# len(): returns the lenght of the string
print(f"Number of letters in  {message}: {len(message)}")


# Enchanced for 
for char in message:
    print(char, end='\t')
print()

# range(n): returns 0 : n-1
for i in range(len(message)):
    print(message[i], end=" ")
print()
