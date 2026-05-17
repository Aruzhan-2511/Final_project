"""Unit tests for StudentManager."""

import unittest

from services.student_manager import StudentManager


class TestStudentManager(unittest.TestCase):
    """Tests for StudentManager."""

    def setUp(self):
        """Create manager before each test."""

        self.manager = StudentManager()

    def test_add_student(self):
        """Test adding student."""

        self.manager.add_student(
            1,
            "Bob",
            19
        )

        self.assertEqual(
            len(self.manager.students),
            1
        )

    def test_search_student(self):
        """Test searching student."""

        self.manager.add_student(
            1,
            "Bob",
            19
        )

        student = self.manager.search_student(1)

        self.assertIsNotNone(student)

    def test_add_grade(self):
        """Test adding grade."""

        self.manager.add_student(
            1,
            "Bob",
            19
        )

        self.manager.add_grade(
            1,
            "Math",
            90
        )

        student = self.manager.search_student(1)

        self.assertEqual(
            student.grades["Math"],
            90
        )

    def test_generate_report(self):
        """Test report generation."""

        self.manager.add_student(
            1,
            "Bob",
            19
        )

        self.manager.add_grade(
            1,
            "Math",
            90
        )

        self.manager.generate_report(1)

        student = self.manager.search_student(1)

        self.assertEqual(
            student.report_card.status,
            "Pass"
        )

    def test_generator(self):
        """Test passing students generator."""

        self.manager.add_student(
            1,
            "Bob",
            19
        )

        self.manager.add_grade(
            1,
            "Math",
            90
        )

        students = list(
            self.manager.passing_students_generator()
        )

        self.assertEqual(
            len(students),
            1
        )


if __name__ == "__main__":
    unittest.main()