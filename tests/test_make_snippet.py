from lib.make_snippet import *

sample_text = 'one two three four five six seven'

def test_empty_str_arg():
    result = make_snippet('')
    assert result == ''

def test_no_argument_provided():
    result = make_snippet()
    assert result == ''

def test_result_end_in_ellipses():
    result = make_snippet(sample_text)
    assert result[-3:]

def test_result_includes_first_five_words():
    result = make_snippet(sample_text)
    assert 'one' in result
    assert 'two' in result
    assert 'three' in result
    assert 'four' in result
    assert 'five' in result

def test_extra_words_removed():
    result = make_snippet(sample_text)
    assert 'six' not in result
    assert 'seven' not in result

# test exact match
def test_exact_match():
    result = make_snippet(sample_text)
    assert result == 'one two three four five...'