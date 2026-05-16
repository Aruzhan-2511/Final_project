"""Report card model module."""


class ReportCard:
    """Stores final report card information for a student."""

    def __init__(self, student_id, average, status):
        self.student_id = student_id
        self.average = average
        self.status = status

    def display_info(self):
        """Display report card summary."""
        return (
            f"Student ID: {self.student_id}, "
            f"Average: {self.average:.2f}, "
            f"Status: {self.status}"
        )