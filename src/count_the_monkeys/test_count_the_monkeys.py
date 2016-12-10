"""Tests for monkey_count function."""


def test_monkey_count1():
    """Test that it returns list from 1 to num entered."""
    from count_the_monkeys import monkey_count
    assert monkey_count(1) == [1]


def test_monkey_count2():
    """Test that it returns list from 1 to num entered."""
    from count_the_monkeys import monkey_count
    assert monkey_count(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_monkey_count3():
    """Test that it returns list from 1 to num entered."""
    from count_the_monkeys import monkey_count
    assert monkey_count(3) == [1, 2, 3]


def test_monkey_count4():
    """Test that it returns list from 1 to num entered."""
    from count_the_monkeys import monkey_count
    assert monkey_count(5) == [1, 2, 3, 4, 5]
