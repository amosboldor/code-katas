"""Kata Opposite number."""


def opposite(number):
    """Given a number return the opposite of that number."""
    return float(-number) if number > 0 else float(abs(number))
