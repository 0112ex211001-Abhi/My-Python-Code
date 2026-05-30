""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""

a = int (input ("Enter number a: "))
b = int (input ("Enter number b: "))

if a > b:
    print (f"{a} is the largest number.")
elif b> a:
    print (f"{b} is the largest number.")
else:
    print ("Both numbers are equal.")   


# Modified by using Function
def largest_num():
    
    a = int (input ("Enter number a: "))
    b = int (input ("Enter number b: "))

    result = f"{a if a>b else b if b>a else 'Both are Equal'} {'is the largest number.'if a!= b else''}"
    print(result)

largest_num()