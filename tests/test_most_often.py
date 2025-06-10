import pytest
from lib.most_often import *


def test_initialisation():
    most_often = MostOften([])
    assert isinstance(most_often, MostOften)
    assert most_often.starting_list == []

def test_append_item():
    most_often = MostOften([])
    most_often.add_new(2)
    assert most_often.starting_list == [2]
    most_often.add_new(1)
    assert most_often.starting_list == [2, 1]

def test_get_most_often():
    most_often_1 = MostOften([1, 2, 2, 2, 3, 3])
    most_often_2 = MostOften([1, 2, 3])
    assert most_often_1.get_most_often() == 2
    assert most_often_2.get_most_often() == "no clear winner"

def test_get_most_often_type_error():
    with pytest.raises(TypeError):
        most_often = MostOften(None)
        most_often.get_most_often()
