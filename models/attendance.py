"""Attendance model module."""


class Attendance:
    """Stores attendance information for a specific date."""

    def __init__(self, date, status):
        self.date = date
        self.status = status

    def display_info(self):
        """Display attendance information."""
        status_text = "Present" if self.status else "Absent"
        return f"Date: {self.date}, Status: {status_text}"