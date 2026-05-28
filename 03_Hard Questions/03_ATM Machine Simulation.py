'''Features:

Check Balance
Withdraw
Deposit
Exit

Use loops and conditions.'''

print("=====> Welcome to the ATM <=====")
balance = 10000
while True:
    print ("\nChose your option: ")
    print("1. Check Balance")
    print("2. Withdrawing Amount")
    print("3. Deposit your Amount")
    print("4. Exit from ATM")

    choise = int(input("\nEnter your choise: "))

    if choise == 1:
        print (f"\nYour balance is : {balance}")
    elif choise == 2:
        amount = float(input("Enter your amount : "))

        if amount <= 0:
            print ("\nInvalid, Enter a valid amount ")
        elif amount > balance:
            print ("\nInsufficiant balance ")
        else:
            balance -= amount
            print(f"\nSucessfully Withdraw {amount}")
            print(f"\nRemaining balance is {balance} ")
    
    elif choise == 3:
        amount = float (input ("Enter your amount : "))

        if amount <= 0:
            print("\nInvalid, Enter a valid amount")
        else:
            balance += amount
            print (f"\nSuccessfully Deposite {amount}")
            print (f"\nYour balance now {balance}")

    elif choise == 4:
        print ("\nThank you for using ATM")
        break

    else:
        print ("\nInvalid Choise, Chose between 1 to 4")

