# track_my_tasks_if_includes_todo

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def track_my_tasks_if_includes_todo(text):

"""
Paramater: 'text' of type is string

Return value: Boolean True/False
    Empty string will return error msg 'Not a valid entry'

Side effects:
"""

## 3. Create Examples as Tests

"""
Check string exists 'text' and if not return error  TODO 
"""

    text_string_is_empty('') => 'Not a valid entry'

"""
Check string 'text' includes TODO 
"""

def check_text_includes_todo ():

    text_includes_todo_item('#TODO Take out the rubbish') => True


"""
Check string 'text' does not include TODO 
"""

    text_does_not_include_todo_item('Take out the rubbish') => False

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!