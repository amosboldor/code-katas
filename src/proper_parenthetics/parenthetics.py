"""Module that checks strings for Proper Parenthetics."""


def proper_parenthetics(string):
    """Function that checks if paranthetics are correct.

    Returns 1 for open parens that are not closed.
    Returns 0 for equal number of open and closed parentheses in the string.
    Returns -1 for closing parens has not been proceeded by one that opens.
    """
    from stack import Stack
    stack = Stack()
    for char in string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            try:
                stack.pop()
            except IndexError:
                return -1
    return 1 if stack._container.head else 0
