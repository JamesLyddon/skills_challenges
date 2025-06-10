import pytest
from lib.check_grammar import *

"""
Given a None value
It throws an error
"""
# check_grammar(None) throws an error
def test_argument_is_none():
    with pytest.raises(Exception) as e:
        check_grammar(None)
    err_msg = str(e.value)
    assert err_msg == 'please include a string to check'

"""
Given a valid string
Returns True
"""
# check_grammar('Hello.') => True
def test_valid_string():
    result1 = check_grammar('Hello.')
    result2 = check_grammar('Hello!')
    result3 = check_grammar('Hello?')
    assert result1
    assert result2
    assert result3


"""
Give string without capital first
Returns False
"""
# check_grammar('hello.') => False
def test_no_capital_at_start():
    result = check_grammar("hello.")
    assert result == False


"""
Given a string without the correct ending punctution
Returns False
"""
# check_grammar('Hello') => False
def test_no_ending_punctuation():
    result = check_grammar("Hello")
    assert result == False

"""
Given a string without the correct ending punctution or capital letter at start
Returns False
"""
# check_grammar('hello') => False
def test_no_ending_punctuation_or_capital():
    result = check_grammar("hello")
    assert result == False