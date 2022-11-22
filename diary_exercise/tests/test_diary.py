from lib.diary import Diary
import pytest


'''
Initially has an empty list of entries:
'''

def test_initially_has_empty_entries_list():
    d = Diary()
    assert d.all() == []

'''
Initially, word count is 0:
'''

def test_initially_word_count_is_zero():
    d = Diary()
    assert d.count_words() == 0

'''
Initially reading time should raise an error:
'''

def test_reading_time_raises_error():
    d = Diary()
    with pytest.raises(Exception) as e:
        d.reading_time(2)
    assert str(e.value) == "No entries added yet"


'''
Initially, #find_best_entry_for_reading_time_raises_error
'''

def test_find_best_entry_for_reading_time_raises_error():
    d = Diary()
    with pytest.raises(Exception) as e:
        d.find_best_entry_for_reading_time(2,4)
    assert str(e.value) == "No entries added yet"

