## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def reading_time(text):
    """takes a passage and returns an estimated time to read (at 200wpm) in minutes

    Parameters: (list all parameters and their types)
        text: a string containing a lot of words e.g. chapters of a book

    Returns: (state the return value and its type)
        a estimated time to read in minutes

    Side effects: (state any side effects)
        none
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Give a 200 word passage
Returns 1 minute as the float 1.0
"""
reading_time('200_word_sample') => 1

"""
Given a 400 word passage
Returns 2 minutes as the float 2.0
"""
reading_time('400_word_sample') => 2

"""
Given a 100 word passage
Returns 0.5 minutes as the float 0.5
"""
reading_time('100_word_sample') => 0.5

"""
Given a None value
It throws an error
"""
reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
