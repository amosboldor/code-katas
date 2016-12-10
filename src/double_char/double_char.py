"""Kata double_char."""


def double_char(s):
    """Return a string with double the letters based on the string given."""
    string = ''
    for letter in s:
        string += letter * 2
    return string
