## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker:
    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   none
        self.tasks = []

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   f"{task} added"
        # Side-effects:
        #   adds task to self.tasks list
        pass # No code here yet
    
    def show_tasks(self):
        # Returns:
        #   A string showing all tasks left to do
        # Side-effects:
        #   if not tasks 'no tasks left!'
        pass # No code here yet
    
    def complete_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   prints to user f"{task} complete!"
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
add a new task
"""
tt = TaskTracker()
tt.add('walk the dog') # => 'walk the dog added'
tt.show_tasks() # => 'walk the dog'

"""
remove a task
"""
tt = TaskTracker()
tt.add('walk the dog')
tt.complete_task('walk the dog') # => 'walk the dog completed!'
tt.show_tasks() # => 'no tasks left!'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
