from lib.design_class_program2 import TaskCompleter



'''
    Remove task from task_list:
'''

def test_remove_task_from_task_list():
    tc = TaskCompleter()
    tc.add_task("Get Milk")
    tc.add_task("Call Mum")
    tc.add_task("Go for run")
    tc.complete_task("Call Mum")
    result = tc.list_task()
    assert result == "Get Milk, Go for run"
