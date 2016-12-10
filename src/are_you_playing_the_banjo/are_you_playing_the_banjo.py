"""Kata Are You Playing Banjo?."""


def are_you_playing_banjo(name):
    """If first letter stars with r --> plays banjo otherwise not."""
    if name[0].lower() == 'r':
        return '{} plays banjo'.format(name)
    else:
        return '{} does not play banjo'.format(name)
