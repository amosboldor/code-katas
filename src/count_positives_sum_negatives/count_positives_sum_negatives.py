"""Kata Count of Positives / Sum of Negatives."""


def count_positives_sum_negatives(arr):
    """Return list of count of positives numbers & sum of negative numbers."""
    if not len(arr):
        return []
    else:
        return [len([num for num in arr if num > 0]),
                sum([num for num in arr if num <= 0])]
