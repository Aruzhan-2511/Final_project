"""Custom decorators module."""


def log_action(func):
    """Decorator for logging system actions."""

    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Executing: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper