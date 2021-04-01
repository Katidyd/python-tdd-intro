import tdd_intro

def test_tests_run():
    """Validates that the tests run"""
    assert True
    # Arrange
    # Act
    # Assert

def test_empty_string_returns_false():
    """If a user enters a string with nothing in it, return false"""
    result = tdd_intro.validate.validatetodo("")
    assert result == False
    # Arrange
    # Act
    # Assert