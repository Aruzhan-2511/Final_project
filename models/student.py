"""Student model module."""

from models.person import Person


class Student(Person):
    """Student class inherited from Person."""

    def __init__(self, person_id, name, age):
        super().__init__(person_id, name, age)
        self.grades = {}
        self.attendance = []
        self.report_card = None

    def add_grade(self, subject, grade):
        """Add or update a grade for a subject."""
        self.grades[subject] = grade

    def add_attendance(self, attendance):
        """Add attendance record."""
        self.attendance.append(attendance)

    def set_report_card(self, report_card):
        """Assign report card to student."""
        self.report_card = report_card

    def calculate_average(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_info(self):
        """Display full student information."""
        return (
            f"{super().display_info()}, "
            f"Grades: {self.grades}, "
            f"Attendance records: {len(self.attendance)}"
        )