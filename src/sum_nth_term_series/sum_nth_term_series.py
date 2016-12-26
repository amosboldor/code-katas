"""Kata Sum of the first nth term of Series."""


def series_sum(n):
    """Return the sum of following series upto nth term(parameter)."""
    # seq = []
    # for x in range(n):
    #     seq.append(1.00 / (1 + x * 3))
    seq = [1.00 / (1 + x * 3) for x in range(n)]
    return '%.2f' % sum(seq)
