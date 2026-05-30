""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""

# using string slicing
string = input ("Enter a string: ")

rs = string [::-1]
print (rs)


# using for loop
string = input ("Enter a string: ")

for i in range(len(string)-1, -1, -1):
    print(string [i], end="")


# Modified by using Function
def reverse_string():
    s = input("Enter a string: ")
    rs = s[-1::-1]
    return rs

print(reverse_string())
