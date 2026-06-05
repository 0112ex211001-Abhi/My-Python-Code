'''Store:

Name
Marks
Roll Number

Features:

Add student
Show students
Search student'''

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def store(self):
        print ("If you don't want to store data just Entered 'exit' in name, and you want to add data then use our features.")
        while True:
            name = input("\nEnter Your Name Here: ")
            if name.lower() == 'exit':
                break
            if not name.isalpha():
                print("Name should contain only letters!")
                continue
            roll_num = input("Enter Your Roll Number Here: ")
            if not roll_num.isalnum():
                print("Roll number should contain only numbers and letters ")
                continue
            while True:
                try:
                    n = int(input("Enter Your Total marks here: "))
                    if n <= 0:
                        print("Enter a valid number!")
                        continue
                    marks = float(input("Enter Your Obtained Marks Here: "))
                    if not 0 <= marks <= n:
                                    print(f"Enter your Obatain mark between 0 to {n} ")
                                    continue
                    break
                except ValueError:
                    print("Please enter valid Input!")

            self.students.append((name,roll_num,marks))
    
    def features(self):
        print("Welcome to Student Management System!")

        while True:
            print("\nChose the following features: ")
            print("1. Add Student")
            print("2. Show Students")
            print("3. Search Student")
            print("4. Exit")

            choise = input("Enter your choise: ")
            
            if choise == '1':
                self.store()
            elif choise == '2':
                if not self.students:
                    print("No students found, Enter some data first!")
                else:  
                    # print(*self.students, sep="\n") ## Output- ('Abhi', '101', 98.0)
                    for name,roll_num,marks in self.students:
                         result = f"Name: {name}, Roll number: {roll_num}, Mark: {marks}"
                         print(result)
            elif choise == '3':
                q_name = input("Enter the student name: ")

                found = False

                for student in self.students:
                    if student[0].lower() == q_name.lower():
                        print(student)
                        found = True
                if not found:
                    print("Not found, Please add first!")
            elif choise == '4':
                print("Thank-You for using Our system!")
                break
            else:
                print("Invalid Input!, Please select right option between 1 to 4")

sms = StudentManagementSystem()
sms.features()


