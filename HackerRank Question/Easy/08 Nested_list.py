'''
Given the names and grades for each student in a class of "N" students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
'''
"""
Wrong code:
"""
# n = int (input ())
# records = []

# for i in range (n):
#     name = input()
#     grade = float (input())
#     records.append([name , grade])

# grades = []
# for record in records:
#     grades.append(record[1])


# sorted_grades = sorted(set(grades))
# second_lowest_grade = sorted_grades[1]

# names = []
# for record in records:
#     if record[1] == second_lowest_grade:
#     names.append(record[0])

# names.sort()
# for name in names:
#     print(name)
"""
Right code:
"""
n = int (input ())
records = []

for i in range (n):
    name = input()
    grade = float (input())
    records.append([name , grade])

grades = []
for record in records:
    grades.append(record[1])


sorted_grades = sorted(set(grades))
second_lowest_grade = sorted_grades[1]

names = []
for record in records:
    if record[1] == second_lowest_grade:
        names.append(record[0])

names.sort()
if __name__ == '__main__':
    for name in names:
        print(name)
        