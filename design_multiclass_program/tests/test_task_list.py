from lib.task_list import TaskList

"""
initially task list is empty
"""
def test_initial_tasklist_is_empty():
    my_tasks=TaskList()
    assert my_tasks.tasklist==[]

"""
when multiple items are added, the tasklist is updated to include the new items
"""
def test_multiple_tasks_added_to_tasklist():
    my_tasks=TaskList()
    my_tasks.add_task('task 1')
    my_tasks.add_task('task 2')
    assert my_tasks.tasklist==['task 1','task 2']
