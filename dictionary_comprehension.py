# Creating a dictionary with comprehension

# Matching students with their grades 

students = ['Alice', 'Bob', 'Charlie', 'David']
grades = ['B', 'A', 'C', 'B']

# using comprehension to create a dictionary

student_grades = {student: grade for student, grade in zip(students, grades)} 