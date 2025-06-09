import pytest
from lib.reading_time import *

"""
Give a 200 word passage
Returns 1 minute as the float 1.0
"""
def test_200_words():
    result = reading_time(200)
    assert result == 1

"""
Given a 400 word passage
Returns 2 minutes as the float 2.0
"""
def test_400_words():
    result = reading_time(400)
    assert result == 2

"""
Given a 100 word passage
Returns 0.5 minutes as the float 0.5
"""
def test_100_words():
    result = reading_time(100)
    assert result == 0.5

"""
Given a None value
It throws an error
"""
def test_none_arg():
    with pytest.raises(Exception) as e:
        reading_time(None)
    err_msg = str(e.value)
    assert err_msg == "please provide a passage"