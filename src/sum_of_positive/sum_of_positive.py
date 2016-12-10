"""Kata sum_of_positive."""


def positive_sum(arr):
    """Given a number return the sum of all of the positives ones."""
    return sum(number for number in arr if number > 0)
