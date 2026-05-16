"""Validation utilities using regex."""

import re


def validate_name(name):
    """Validate student name using regex."""
    pattern = r"^[A-Za-z ]+$"
    return bool(re.match(pattern, name))