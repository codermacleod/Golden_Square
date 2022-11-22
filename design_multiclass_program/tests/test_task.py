from lib.task import Task
"""
Initially, new task is created as 'incomplete':
"""

def test_new_task_created_as_incomplete():
    t = Task("Collect laundry")
    assert t.incomplete == True