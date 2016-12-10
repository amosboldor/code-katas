"""Kata Sum without highest and lowest number."""


def sum_array(x):
    """Return sum of list min the lowest and highest numbers."""
    return 0 if type(x) != list else sum(x) - max(x) - min(x) if len(x) > 2 else 0
