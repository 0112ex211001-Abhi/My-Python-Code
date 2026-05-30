""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""

a = int (input ("Enter number a: "))
b = int (input ("Enter number b: "))

sum = a + b 

print (f"The sum of {a} and {b} is {sum}")


# Modified by using Function
def add(a, b):
    a = int (input ("Enter number a: "))
    b = int (input ("Enter number b: "))
    sum = a + b
    return f"The sum of {a} and {b} is {sum}"

print(add(a, b))
result = add(a, b)
print (result)