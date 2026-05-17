"""Main module for Student Database System."""

from services.student_manager import StudentManager
from utils.decorators import log_action
from utils.validator import validate_name


manager = StudentManager()


@log_action
def add_student_menu():
    """Handle adding a student from menu."""

    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ").strip()
        age = int(input("Enter student age: "))

        if not validate_name(name):
            print("Invalid name. Use only letters and spaces.")
            return

        manager.add_student(student_id, name, age)

        print("Student added successfully!")

    except ValueError:
        print("Invalid input.")


def main_menu():
    """Run the main menu."""

    while True:

        print("""
===== STUDENT DATABASE SYSTEM =====

1. Add Student
2. Show Students
3. Search Student
4. Add Grade
5. Mark Attendance
6. Generate Report
7. Save Data to JSON
8. Export Reports to CSV
9. Export Attendance to CSV
10. Show Passing Students
11. Exit
""")

        choice = input("Choose option: ").strip()

        if choice == "1":

            add_student_menu()

        elif choice == "2":

            manager.show_students()

        elif choice == "3":

            try:
                student_id = int(input("Enter student ID: "))

                student = manager.search_student(student_id)

                if student:
                    print(student.display_info())
                else:
                    print("Student not found.")

            except ValueError:
                print("Invalid ID.")

        elif choice == "4":

            try:
                student_id = int(input("Enter student ID: "))
                subject = input("Enter subject: ")
                grade = float(input("Enter grade: "))

                manager.add_grade(student_id, subject, grade)

            except ValueError:
                print("Invalid grade.")

        elif choice == "5":

            try:
                student_id = int(input("Enter student ID: "))
                date = input("Enter date: ")
                status_input = input("Present? (yes/no): ").lower()

                status = status_input == "yes"

                manager.mark_attendance(student_id, date, status)

            except ValueError:
                print("Invalid input.")

        elif choice == "6":

            try:
                student_id = int(input("Enter student ID: "))

                manager.generate_report(student_id)

            except ValueError:
                print("Invalid ID.")

        elif choice == "7":

            manager.save_data()

        elif choice == "8":

            manager.export_reports()

        elif choice == "9":

            manager.export_attendance()

        elif choice == "10":

            print("\n--- Passing Students ---")

            for student in manager.passing_students_generator():

                print(student.display_info())

        elif choice == "11":

            print("Exiting program...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()