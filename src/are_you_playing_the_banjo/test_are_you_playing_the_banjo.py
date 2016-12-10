"""Tests for are_you_playing_banjo function."""


def test_are_you_playing_banjo1():
    """Test if first letter stars with r --> plays banjo otherwise not."""
    from are_you_playing_the_banjo import are_you_playing_banjo
    assert are_you_playing_banjo('Amos') == 'Amos does not play banjo'


def test_are_you_playing_banjo2():
    """Test if first letter stars with r --> plays banjo otherwise not."""
    from are_you_playing_the_banjo import are_you_playing_banjo
    assert are_you_playing_banjo('Rick') == 'Rick plays banjo'


def test_are_you_playing_banjo3():
    """Test if first letter stars with r --> plays banjo otherwise not."""
    from are_you_playing_the_banjo import are_you_playing_banjo
    assert are_you_playing_banjo('Roland') == 'Roland plays banjo'


def test_are_you_playing_banjo4():
    """Test if first letter stars with r --> plays banjo otherwise not."""
    from are_you_playing_the_banjo import are_you_playing_banjo
    assert are_you_playing_banjo('Felix') == 'Felix does not play banjo'
