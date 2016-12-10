"""Kata Square(n) Sum."""


def square_sum(numbers):
    """Return sum of every squared number in the list."""
    return sum(map(lambda x: x**2, numbers))
