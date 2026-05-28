# '''Check whether password contains:

# Uppercase
# Lowercase
# Number
# Special character'''


# # def Password_strength(password):

# #     if 8 <= (len(password)) >= 12:
# #         for char in password:
# #             if any (char.upper) in password:
# #                 return "ok"
# #             elif any (char.lower) in password:
# #                 return "ok"
# #             elif any (char.isdigit )in password:
# #                 return "ok"
# #             elif any ("!@#$%^&*()_+=-<>?/\[]{}~:;") in password:
# #                 return "ok"
        
# #             print("Your Password is Strong")

# #         else:
# #             print ("Your Password miss something and I can't procced for futher")
# #             print ("Make it strong by including : print ( altleast ONE Uppercaseprint ( altleast ONE Lowercaseprint ( altleast ONE Numberprint ( altleast ONE Special character ")
# #     else:
# #         if len(password)<8 or len(password)>12:
# #             print ("Password must be contain character between 8 to 12")
            

# # password = input("Enter your password: ")
# # Password_strength(password)


def Password_strength(password):
    if 8<= (len(password)) <= 12:

        u = any(char.isupper() for char in password)
        l = any(char.islower() for char in password)
        n = any(char.isdigit() for char in password)
        s = any(char in "!@#$%^&*()_+=-[]{}:'/?.>,<\|" for char in password)

        if u and l and n and s:
            print ("Your Password is Strong")
        
        else:
            print ("Your Password miss something and I can't procced for futher")
            print ("Make it strong by including : ")
            print ( "--> altleast ONE Uppercase")
            print ( "--> altleast ONE Lowercase")
            print ( "--> altleast ONE Number")
            print ( "--> altleast ONE Special character ")
    else:
        print ("Password must be contain character between 8 to 12")

password = input("Enter your password: ")
Password_strength(password)


# # Create password
# saved_password = input("Create your password: ")

# attempts = 3

# while attempts > 0:

#     entered_password = input("\nEnter password: ")

#     if entered_password == saved_password:
#         print("✅ Access Granted")
#         break

#     else:
#         attempts -= 1
#         print("❌ Wrong Password")
#         print("Attempts left:", attempts)

# if attempts == 0:
#     print("\n🔒 Account Locked")