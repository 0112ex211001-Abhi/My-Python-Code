""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""
# In Simple way
name = input("Enter your name: ")
print (f"My name is {name}")

# Modified by using Function
def name():
    n = input("Enter your name: ")
    b = n.upper() 
    # n.upper ye n ke sabhi character ko capital letter me convert kardega. 
    # Ex- n = abhishek  
    #     b = ABHISHEK
    return "My name is " + b

print (name())
#Output- My name is ABHISHEK



