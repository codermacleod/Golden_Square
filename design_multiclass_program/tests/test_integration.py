from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.task_list import TaskList
from lib.task import Task

"""
Adding an instance of DiaryEntry to Diary list 
"""
def test_initial_instance():
    dans_diary = Diary()
    e1 = DiaryEntry('entry 1', 'one two three')
    dans_diary.add(e1)
    assert dans_diary.entries == [e1] 

"""
Adding two instances of DiaryEntry to Diary list 
"""
def test_two_item_list_returned_when_two_instances_added():
    dans_diary = Diary()
    e1 = DiaryEntry('entry 1', 'ne two three')
    e2 = DiaryEntry('entry 2', 'four five six')
    dans_diary.add(e1)
    dans_diary.add(e2)
    assert dans_diary.read_all_entries() ==[e1,e2]

"""
Select diary entries to read based on time(t) and reading speed(rs)
"""
def test_reading_material_finder_returns_valid_entry_as_string():
    dans_diary=Diary()
    e1 = DiaryEntry('entry 1', 'one two three four')
    e2 = DiaryEntry('entry 2', 'four five six')
    e3 = DiaryEntry('entry 3', 'seven eight nine ten eleven')
    dans_diary.add(e1)
    dans_diary.add(e2)
    dans_diary.add(e3)
    assert dans_diary.reading_material_finder(2,2) == 'one two three four'

"""
get phone numbers method looks through all entries to return a list of phone numbers 
"""
def test_get_phone_numbers_returns_list_of_phone_numbers():
    dans_diary=Diary()
    e1 = DiaryEntry('entry 1', 'one two three 07800000000')
    e2 = DiaryEntry('entry 2', 'four 07800000001 five 07800000002 six')
    dans_diary.add(e1)
    dans_diary.add(e2)
    assert dans_diary.get_phone_numbers() == ['07800000000','07800000001','07800000002']

"""
Check completed tasks are returned when complete method called:
"""
def test_completed_tasks_returned_when_complete_method_called():
    tl = TaskList()
    task1= Task('Get laundry')
    tl.add_task(task1)
    task1.set_as_complete()
    assert tl.complete() == ['Get laundry'] 

    """
Check incomplete tasks are returned when incomplete method called:
"""
def test_incomplete_tasks_returned_when_incomplete_method_called():
    tl = TaskList()
    task1= Task('Get laundry')
    tl.add_task(task1)
    assert tl.incomplete() == ['Get laundry'] 

   







