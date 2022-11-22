# {{Task Completer}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskCompleter():
    def __init__(self):
        self.task_list = task_list

    def complete_task(self,task):
        self.task_list.remove(task)
        

    def list_task(self):
        # A list of tasks left to complete
        

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task of type string:
#remove_task from task_list.
"""
tc = TaskCompleter()
tc.complete_task("Get shopping") # => removes task
