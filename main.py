"""Student Database System - Basic CLI menu."""

students = {}


def add_student():
    """Add a new student to the database."""
    try:
        student_id = len(students) + 1

        name = input("Enter student name: ").strip()
        age = int(input("Enter student age: "))

        if not name:
            print("Name cannot be empty.")
            return

        students[student_id] = {
            "name": name,
            "age": age,
            "grades": {},
            "attendance": []
        }

        print("Student added successfully!")

    except ValueError:
        print("Age must be a number.")


def show_students():
    """Display all students in the database."""
    if not students:
        print("No students found.")
        return

    print("\n--- Student List ---")
    for student_id, info in students.items():
        print(f"ID: {student_id} | Name: {info['name']} | Age: {info['age']}")


def search_student():
    """Search for a student by ID."""
    try:
        student_id = int(input("Enter student ID: "))

        if student_id in students:
            student = students[student_id]

            print("\n--- Student Found ---")
            print(f"ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {student['grades']}")
            print(f"Attendance: {student['attendance']}")
        else:
            print("Student not found.")

    except ValueError:
        print("Invalid ID. Please enter a number.")


def main_menu():
    """Run the main menu of the Student Database System."""
    while True:
        print("""
===== STUDENT DATABASE SYSTEM =====

1. Add Student
2. Show Students
3. Search Student
4. Exit
""")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose from 1 to 4.")


if __name__ == "__main__":
    main_menu()