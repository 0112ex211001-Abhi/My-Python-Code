num1 = int (input ("Enter first number: "))
num2 = int (input ("Enter second number: "))

operator = input ("Enter Operator (+, -, *, /): ")
if operator == "+":
    print (f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print (f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print (f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print (f"{num1} / {num2} = {round(num1 / num2, 2)}")
    else:
        print ("Error: Division by zero is not allowed.")
else:
    print ("Invalid operator. Please use +, -, *, or /.")

    