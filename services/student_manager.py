"""Student manager module."""

from models.student import Student
from models.attendance import Attendance
from models.report_card import ReportCard


class StudentManager:
    """Main controller class for managing students."""

    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age):
        """Add a new student."""
        student = Student(student_id, name, age)
        self.students[student_id] = student

    def show_students(self):
        """Display all students."""
        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            print(student.display_info())

    def search_student(self, student_id):
        """Search student by ID."""
        return self.students.get(student_id)

    def add_grade(self, student_id, subject, grade):
        """Add grade to student."""
        student = self.search_student(student_id)

        if student:
            student.add_grade(subject, grade)
            print("Grade added successfully.")
        else:
            print("Student not found.")

    def mark_attendance(self, student_id, date, status):
        """Mark student attendance."""
        student = self.search_student(student_id)

        if student:
            attendance = Attendance(date, status)
            student.add_attendance(attendance)
            print("Attendance marked.")
        else:
            print("Student not found.")

    def generate_report(self, student_id):
        """Generate student report card."""
        student = self.search_student(student_id)

        if student:
            average = student.calculate_average()

            status = "Pass" if average >= 50 else "Fail"

            report = ReportCard(student_id, average, status)

            student.set_report_card(report)

            print(report.display_info())

        else:
            print("Student not found.")