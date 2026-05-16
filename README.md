# Student Database System

## Project Overview

The Student Database System is a Python-based application developed for the Introduction to Programming 2 final project.

The system helps manage student information, including:
- student registration
- grade management
- attendance tracking
- report card generation
- data export and storage

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
- Validate names using regex
- Log actions using decorators

---

# Project Structure

```text
Final_project/
│
├── main.py
│
├── models/
│   ├── person.py
│   ├── student.py
│   ├── attendance.py
│   └── report_card.py
│
├── services/
│   └── student_manager.py
│
├── utils/
│   ├── decorators.py
│   ├── validator.py
│   └── file_handler.py
│
├── tests/
│   ├── test_manager.py
│   └── test_student.py
│
└── data/
    ├── students.json
    ├── attendance.csv
    └── reports.csv
```

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
- `Student.display_info()` shows full student information
- `ReportCard.display_info()` shows report summary

---

## 4. Encapsulation

Student data is stored inside class attributes and managed through methods.

---

# Functional Programming

The project uses functional programming concepts such as:

- generators
- lambda expressions
- filter()

Example:
- passing students generator

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
- report generation

---

# Technologies Used

- Python 3
- JSON
- CSV
- Regex (`re`)
- unittest

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
- email notifications for parents
- advanced student analytics

---

# Conclusion

This project demonstrates the application of Python programming fundamentals, object-oriented programming principles, modular architecture, file handling, decorators, generators, regex validation, and testing techniques in a real-world student management system.
