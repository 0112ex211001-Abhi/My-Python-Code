"""
Question: Finding the percentage

The provided code stub will read in a dictionary containing key/value pairs 
of name:[marks] for a list of students. Print the average of the marks array for 
the student name provided, showing 2 places after the decimal.
"""
print("*****_____Finding the percentage_____*****")
if __name__ == '__main__':
    n = int (input("Enter number of students:")) 

students = {}

for i in range(n):
    data = input("Enter name and marks of students: ").split()
    
    name = data[0]
    marks = list(map(float, data[1:]))
    
    students[name] = marks
# print(students) ##for cheaking

query_name = input("Enter the name of the student: ")

marklist = students[query_name]
# print (marklist)
average = sum(marklist)/ len(marklist)

print (f"The percentage of {query_name} is:{average:.2f}")