from lib.design_class_program import Todo



"""
#Given a task of type string:
#add_task adds the task to a task_list.
"""

def test_add_task_adds_task_to_list():
    td = Todo()
    result = td.add_task("Get shopping")
    assert result == "Get shopping"

"""
Given no task
#add_task returns "You haven't added a task..."
"""

def test_add_no_task_to_list_returns_you_havent_added():
    td = Todo()
    result = td.add_task()
    assert result == "You haven't added a task..."

"""
Given a number
#add_task returns "Please enter a string"
"""

def test_when_task_is_number_return_text_to_state():
    td = Todo()
    result = td.add_task(45)
    assert result == "Please enter a string"

"""
Given that the Todo list items >= 1,
#list_task shows a list of all tasks
"""
def test_task_list_holds_1_or_more_items_and_return_them():
    td = Todo()
    td.add_task("Task list item 1")
    td.add_task("Task list item 2")
    result = td.list_task() # => "Task list item 1, Task list item 2..."
    assert result == "Task list item 1, Task list item 2"

