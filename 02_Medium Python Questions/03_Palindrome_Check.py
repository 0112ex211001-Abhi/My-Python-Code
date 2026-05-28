# a = input ("Enter a string or number: ")
# b = a[::-1]

# if a == b:
#     if a.isdigit():
#         print (f"{a} is a palindrome number.")
#     else:
#         print (f"{a} is a palindrome string.")
# else:
#     if a.isdigit():
#         print (f"{a} is not a palindrome number.")
#     else:
#         print (f"{a} is not a palindrome string.")




# a = input("Enter a string or number: ")

# if a == a[::-1]:
#     print(f"{a} is a palindrome {'number' if a.isdigit() else 'string'}.")
# else:
#     print(f"{a} is not a palindrome {'number' if a.isdigit() else 'string'}.")


def pali(a):
    if a == a[::-1]:
        return f"{a} is a palindrome {'number' if a.isdigit() else 'string'}."
    else:
        return f"{a} is not a palindrome {'number' if a.isdigit() else 'string'}."
    
a = input("Enter a string or number: ")
result = pali(a)
print(result)