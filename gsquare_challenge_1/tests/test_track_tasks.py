from lib.track_tasks import *

"""
Check string exists 'text' and if not return error  TODO 
"""

import pytest

def test_text_string_is_empty():
    with pytest.raises(Exception) as e:
        track_my_tasks_if_includes_todo('')
    error_message = str(e.value)
    assert error_message == 'Not a valid entry'

"""
Check string 'text' includes TODO 
"""

def test_check_text_includes_todo():
    result = track_my_tasks_if_includes_todo('#TODO Take out the rubbish')
    assert result == True

"""
Check string 'text' does not include TODO 
"""

def test_text_does_not_include_todo():
    result = track_my_tasks_if_includes_todo('Take out the rubbish')
    assert result == False