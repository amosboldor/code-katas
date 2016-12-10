"""Kata Jenny's Secret Message."""


def greet(name):
    """Return Hello, name unless name is Jonny then Hello, my love!."""
    return "Hello, my love!" if name == "Johnny" else "Hello, {}!".format(name)
