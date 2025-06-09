from lib.count_words import *

def test_empty_str():
    result = count_words('')
    assert result == 0

def test_single_word():
    result = count_words('hello')
    assert result == 1

def test_two_words():
    result = count_words('hello there')
    assert result == 2

def test_three_words():
    result = count_words('hello there buddy')
    assert result == 3

def test_weird_spacing():
    result = count_words('  hi   how  are   you   ')
    assert result == 4