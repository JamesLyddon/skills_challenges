from lib.TaskTracker import *

def test_initialises():
    tt = TaskTracker()
    assert isinstance(tt, TaskTracker)
    assert tt.tasks == []

def test_add_taskk():
    tt = TaskTracker()
    tt.add_task('walk the dog')
    assert tt.tasks[0] == 'walk the dog'

def test_show_tasks():
    tt = TaskTracker()
    tt.add_task('walk the dog')
    tt.add_task('feed the cat')
    assert tt.show_tasks() == ['walk the dog', 'feed the cat']

"""
remove a task
"""
def test_complete_task():
    tt = TaskTracker()
    tt.add_task('walk the dog')
    tt.add_task('feed the cat')
    assert tt.show_tasks() == ['walk the dog', 'feed the cat']
    tt.complete_task('walk the dog')
    assert tt.show_tasks() == ['feed the cat']
    tt.complete_task('feed the cat')
    assert tt.show_tasks() == []

"""
remove non-existant task
"""
def test_complete_nonexistant_task():
    tt = TaskTracker()
    result = tt.complete_task('walk the cat')
    assert result == None
