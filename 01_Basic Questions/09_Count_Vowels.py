""" I use AI for learning and understanding codes; 
you should use AI too, as it makes learning and understanding easier."""

string = input ("Enter a string: ")

vowels = "aeiou"
count = 0 

for char in string :
    if char.lower() in vowels :
        count += 1

print (f"The number of vowels in the string is {count}")

# Modified by using Function
def count_vowels(string):

    vowels = "aeiou"
    count = 0 

    for char in string :
        if char.lower() in vowels :
            count += 1

    return f"The number of vowels in the string is {count}"

string = input ("Enter a string: ")
print(count_vowels(string))


# By using List Comprehension Method:

s = input ("Enter your string: ")
v = "aeiou"
c = [char for char in s if char.lower() in v]
print(len(c))