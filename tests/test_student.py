"""Unit tests for Student model."""

import unittest

from models.student import Student
from models.attendance import Attendance
from models.report_card import ReportCard


class TestStudent(unittest.TestCase):
    """Tests for Student class."""

    def setUp(self):
        """Create test student before each test."""

        self.student = Student(1, "Alice", 20)

    def test_add_grade(self):
        """Test adding a grade."""

        self.student.add_grade("Math", 95)

        self.assertEqual(
            self.student.grades["Math"],
            95
        )

    def test_calculate_average(self):
        """Test average grade calculation."""

        self.student.add_grade("Math", 90)
        self.student.add_grade("Python", 80)

        self.assertEqual(
            self.student.calculate_average(),
            85
        )

    def test_add_attendance(self):
        """Test attendance addition."""

        attendance = Attendance(
            "2025-05-10",
            True
        )

        self.student.add_attendance(attendance)

        self.assertEqual(
            len(self.student.attendance),
            1
        )

    def test_set_report_card(self):
        """Test assigning report card."""

        report = ReportCard(
            1,
            88,
            "Pass"
        )

        self.student.set_report_card(report)

        self.assertEqual(
            self.student.report_card.status,
            "Pass"
        )

    def test_display_info(self):
        """Test display information."""

        info = self.student.display_info()

        self.assertIn(
            "Alice",
            info
        )


if __name__ == "__main__":
    unittest.main()