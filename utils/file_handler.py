"""File handling utilities for JSON and CSV files."""

import csv
import json
import os


def ensure_data_folder():
    """Create data folder if it does not exist."""
    os.makedirs("data", exist_ok=True)


def save_students_to_json(students, filename="data/students.json"):
    """Save students data to JSON file."""
    ensure_data_folder()

    data = {}

    for student_id, student in students.items():
        data[student_id] = {
            "id": student.person_id,
            "name": student.name,
            "age": student.age,
            "grades": student.grades,
            "attendance": [
                {
                    "date": record.date,
                    "status": record.status
                }
                for record in student.attendance
            ]
        }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def export_reports_to_csv(students, filename="data/reports.csv"):
    """Export student report cards to CSV file."""
    ensure_data_folder()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Student ID", "Name", "Average", "Status"])

        for student in students.values():
            if student.report_card:
                writer.writerow([
                    student.person_id,
                    student.name,
                    student.report_card.average,
                    student.report_card.status
                ])