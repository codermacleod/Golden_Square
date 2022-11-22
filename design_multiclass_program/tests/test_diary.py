from lib.diary import Diary

"""
Initial creation of Diary instance should return empty list of diary entries
"""
def test_initial_diary_creation_returns_empty_list():
    dans_diary=Diary()
    assert dans_diary.entries==[]