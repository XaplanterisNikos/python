# Challenge 1
# F
# aa    
# ccc    
# tttt  
# ooooo
# rrrrrr
# yyyyyyy

message = "Factory"

# solution 
for i in range (len(message)):
    print((i+1) * message[i])


# Challenge 2
# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy


# solution 
for i in range(len(message)):
    print((i + 1) * message[i], end="")
    print((len(message) - (i + 1)) * "*")


# solution 2
for i in range(len(message)):
    print(message[i] * (i+1), end="*" * (len(message)-i-1))
    print()


