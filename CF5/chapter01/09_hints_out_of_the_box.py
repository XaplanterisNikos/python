a = 10
b =20

result = a+b
print("result= ",result)

print("Type of a ",type(a))


# using the magic method __add__ to perform addition
magic_result = a.__add__(b)

print("magic result =" , magic_result)