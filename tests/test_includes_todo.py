from lib.includes_todo import *

sample_notes = ["Book dentist appointment #TODO", "Work was good today, I met the big boss!", "Call mum #TODO", "Buy dog food #todo", "Willow didn't eat much this morning"]

"""
Give a single string with '#TODO' return True
It returns True
"""
# includes_todo("Book dentist appointment #TODO") => True
def test_valid_todo():
    td = includes_todo(sample_notes[0])
    assert td == True

"""
Given a single string without '#TODO' and return False
It returns False
"""
# includes_todo("Work was good today, I met the big boss!") => False
def test_invalid_string():
    td = includes_todo(sample_notes[1])
    assert td == False

"""
Given a single string with '#todo' and return True
It returns True
"""
# includes_todo("Buy dog food #todo") => False
def test_lowercase_todo():
    td = includes_todo(sample_notes[3])
    assert td == True

"""
Given an empty string return False
It returns False
"""
# includes_todo("") => False
def test_empty_string():
    td = includes_todo('')
    assert td == False
