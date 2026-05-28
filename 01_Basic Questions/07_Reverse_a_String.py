string = input ("Enter a string: ")

rs = string [::-1]
print (rs)

for i in range(len(string)-1, -1, -1):
    print(string [i], end="")