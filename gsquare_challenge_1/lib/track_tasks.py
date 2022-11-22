def track_my_tasks_if_includes_todo(text):
    if text == '':
        raise Exception('Not a valid entry')
    if '#TODO' in text:
        return True
    else:
        return False