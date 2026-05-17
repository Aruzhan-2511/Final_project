# Student Database System

## Project Overview

The Student Database System is a Python-based application developed for the Introduction to Programming 2 final project.

The system helps manage student information, including:
- student registration
- grade management
- attendance tracking
- report card generation
- JSON data storage
- CSV report exporting

The project follows a modular architecture using Object-Oriented Programming (OOP), file handling, decorators, generators, regex validation, and unit testing.

---

# Features

- Add new students
- Display all students
- Search students by ID
- Add grades for subjects
- Track attendance
- Generate report cards
- Save student data to JSON
- Export reports to CSV
- Display passing students using generators
- Display honor students using lambda and filter
- Validate names using regex
- Log actions using decorators

---

# Project Structure

```text
Final_project/
│
├── main.py
├── README.md
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── student.py
│   ├── attendance.py
│   └── report_card.py
│
├── services/
│   ├── __init__.py
│   └── student_manager.py
│
├── utils/
│   ├── __init__.py
│   ├── decorators.py
│   ├── validator.py
│   └── file_handler.py
│
├── tests/
│   ├── __init__.py
│   ├── test_student.py
│   └── test_manager.py
│
├── data/
│   ├── students.json
│   ├── attendance.csv
│   └── reports.csv
│
└── screenshots/
    └── diagram.png
```

---

# System Architecture

The following diagram shows the relationships between the classes and modules used in the system.

<img width="522" height="342" alt="diagram" src="https://github.com/user-attachments/assets/7a467447-9e78-4016-9b48-27366dafbb15" />


---

# OOP Concepts Used

## 1. Inheritance

The `Student` class inherits from the `Person` class.

```python
class Student(Person):
```

The parent class stores:
- ID
- name
- age

The child class stores:
- grades
- attendance
- report card

---

## 2. Association

The classes work together using association relationships:

- `StudentManager` manages `Student`
- `Student` contains `Attendance`
- `Student` contains `ReportCard`

This allows different classes to interact inside the system.

---

## 3. Polymorphism

Different classes implement the same method:

```python
display_info()
```

Examples:
- `Person.display_info()`
- `Student.display_info()`
- `Attendance.display_info()`
- `ReportCard.display_info()`

Each class displays different information.

---

## 4. Encapsulation

Student data is stored inside class attributes and managed through methods.

---

# Functional Programming

The project uses functional programming concepts such as:

- lambda expressions
- filter()
- map()
- generators

Examples:
- passing students generator
- honor students filtering

---

# Decorators

A custom decorator was implemented:

```python
@log_action
```

The decorator logs important system actions.

---

# Generator

A generator is used to display passing students efficiently.

```python
yield student
```

---

# Regex Validation

The project uses the `re` module to validate user input.

Example:
- student name validation

```python
pattern = r"^[A-Za-z ]+$"
```

---

# File Handling

## JSON

Student data is saved into:

```text
students.json
```

## CSV

Attendance and reports are exported into:

```text
attendance.csv
reports.csv
```

The project uses:
- `json`
- `csv`
- `os`

modules for file handling and data persistence.

---

# Error Handling

The system uses:
- `try/except`
- input validation
- conditional checks

to prevent runtime errors.

---

# Unit Testing

The project includes unit tests using Python `unittest`.

Tested features:
- adding students
- searching students
- adding grades
- attendance tracking
- report generation
- generators

---

# Technologies Used

- Python 3
- JSON
- CSV
- Regex (`re`)
- unittest

---

# Example Output

```text
===== STUDENT DATABASE SYSTEM =====

1. Add Student
2. Show Students
3. Search Student
4. Add Grade
5. Mark Attendance
6. Generate Report
7. Save Data to JSON
8. Export Reports to CSV
9. Show Passing Students
10. Show Honor Students
11. Exit
```

---

# How to Run the Project

Run the following command:

```bash
python main.py
```

---

# Team Contributions

- Member 1 — Models and OOP structure
- Member 2 — Student management system
- Member 3 — File handling and validation
- Member 4 — Testing and documentation

---

# Future Improvements

Possible future improvements:
- graphical user interface (GUI)
- database integration
- parent email notifications
- advanced student analytics

---

# Conclusion

This project demonstrates the application of Python programming fundamentals, object-oriented programming principles, modular architecture, file handling, decorators, generators, regex validation, and testing techniques in a real-world student management system.
