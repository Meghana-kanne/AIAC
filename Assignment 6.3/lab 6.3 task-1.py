def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 45:
        return 'D'
    else:
        return 'F'

def display_student_details(name, roll_no, marks):
    grade = get_grade(marks)
    print(f"Student Name: {name}")
    print(f"Roll No: {roll_no}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks: "))

display_student_details(name, roll_no, marks)