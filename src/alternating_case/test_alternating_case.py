"""Tests for to_alternating_case function."""


def test_to_alternating_case1():
    """Test if converts it string lowercase to uppercase and vice versa."""
    from alternating_case import to_alternating_case
    assert to_alternating_case('1a2b3c4d5e') == '1A2B3C4D5E'


def test_to_alternating_case2():
    """Test if converts it string lowercase to uppercase and vice versa."""
    from alternating_case import to_alternating_case
    assert to_alternating_case('amos') == 'AMOS'


def test_to_alternating_case3():
    """Test if converts it string lowercase to uppercase and vice versa."""
    from alternating_case import to_alternating_case
    assert to_alternating_case('DuDe') == 'dUdE'


def test_to_alternating_case4():
    """Test if converts it string lowercase to uppercase and vice versa."""
    from alternating_case import to_alternating_case
    assert to_alternating_case('Hello World') == 'hELLO wORLD'
