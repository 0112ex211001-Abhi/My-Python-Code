""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""


n = int (input ("Enter the number of terms: "))
a = 0 
b = 1 
print (a, b, end=" ")
for i in range (n):
    next_num = a+b
    print (next_num, end=" ")
    a, b = b, next_num