# You have a record of n students. Each record contains the student's name, and their percent marks in Math, Physics and Chemistry.
# The marks can be floating values. You are required to save the record in a dictionary data type. Student’s name is the key. Marks stored in a list is the value.
# The user enters a student's name. Output the average percentage marks obtained by that student.

records = {}

n = int(input("Enter number of students: "))
for _ in range(n):
    name = input("Enter student's name: ")
    marks = list(map(float, input("Enter marks in Math, Physics, Chemistry separated by space: ").split()))
    records[name] = marks

query_name = input("Enter a name to search: ")
if query_name in records:
    average = sum(records[query_name]) / len(records[query_name])
    print("Average percentage mark:", round(average, 2))
else:
    print("Student not found.")
