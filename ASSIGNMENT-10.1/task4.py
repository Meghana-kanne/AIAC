def welcome_student(name: str) -> None:
    """Print a welcome message for a student.

    Args:
        name (str): The name of the student.
    """
    print("Welcome", name)

students = ["Alice", "Bob", "Charlie"]

for student in students:
    welcome_student(student)