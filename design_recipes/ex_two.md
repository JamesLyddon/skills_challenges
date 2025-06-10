## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammar(text):
    """Checks text starts with a capital letter and ends with one of these {'.', '?', '!'}

    Parameters: (list all parameters and their types)
        text: a string of text to assess

    Returns: (state the return value and its type)
        True or False

    Side effects: (state any side effects)
        No side effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a None value
It throws an error
"""
check_grammar(None) throws an error

"""
Given a valid string
Returns True
"""
check_grammar('Hello.') => True

"""
Give string without capital first
Returns False
"""
check_grammar('hello.') => False

"""
Given a string without the correct ending punctution
Returns False
"""
check_grammar('Hello') => False

"""
Given a string without the correct ending punctution or capital letter at start
Returns False
"""
check_grammar('hello') => False
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
