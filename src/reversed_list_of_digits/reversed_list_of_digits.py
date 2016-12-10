"""Kata Convert number to reversed array of digits."""


def digitize(n):
    """Given a number it return reversed array of digits."""
    return [int(x) for x in str(n)][::-1]
