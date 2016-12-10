"""Kata Counting Sheep."""


def count_sheeps(sheep):
    """Return the amount of sheep are present."""
    return sum(x for x in sheep if x)
