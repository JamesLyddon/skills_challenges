## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def includes_todo(single_note):
    """returns True if '#TODO' in a string

    Parameters: (list all parameters and their types)
        a string

    Returns: (state the return value and its type)
        True or False

    Side effects: (state any side effects)
        None
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Give a single string with '#TODO' return True
It returns True
"""
includes_todo("Book dentist appointment #TODO") => True

"""
Given a single string without '#TODO' and return False
It returns False
"""
includes_todo("Work was good today, I met the big boss!") => False

"""
Given a single string with '#todo' and return True
It returns True
"""
includes_todo("Buy dog food #todo") => False

"""
Given an empty string return False
It returns False
"""
includes_todo("") => False
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
