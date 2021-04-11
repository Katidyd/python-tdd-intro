import tdd_intro


def test_empty_string_returns_false():
    """If a user enters a string with nothing in it, return false"""
    result = tdd_intro.validate.validatetodo("")
    assert result == False

def test_non_empty_string_returns_true():
    """If a user enters a character, return true"""
    result = tdd_intro.validate.validatetodo("A")
    assert result == True

def test_string_with_special_charcters_returns_true():
    """If a user enters letters and special characters together return true"""  
    result = tdd_intro.validate.validatetodo("write a test!")
    assert result == True
