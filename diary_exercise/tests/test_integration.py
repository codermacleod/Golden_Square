from lib.diary import Diary
from lib.diary_entry import DiaryEntry

'''
Given 2 diary entries
I see them back in the list
'''

def test_two_diary_entries_given_are_shown_in_list():
    d = Diary()
    de1 = DiaryEntry("School Run","Picked up dinner on way to school")
    de2 = DiaryEntry("Run","Felt a lot more energetic today")
    d.add(de1)
    d.add(de2)
    assert d.all() == [de1,de2]

'''
Given I add 2 diary entries
I count each word from the contentes of both entries
'''

def test_given_two_entries_return_number_of_words_from_both():
    d = Diary()
    de1 = DiaryEntry("School Run","Picked up dinner on way to school")
    de2 = DiaryEntry("Run","Felt a lot more energetic today")
    d.add(de1)
    d.add(de2)
    
    assert d.count_words() == 13


'''
Given I add two entries with a total length of 5
And I call reading time of a wpm of 2
Then the total reading time should be 13/2. 6.5 Rounded to 7
'''

def test_reading_time_returns_time_to_read_all_entries():
    d = Diary()
    de1 = DiaryEntry("School Run","Picked up dinner on way to school")
    de2 = DiaryEntry("Run","Felt a lot more energetic today")
    d.add(de1)
    d.add(de2)
    assert d.reading_time(2) == 7


'''
Given I add two diary entries, one long and one short,
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can only read the short one
Then #find_best_entry_for_reading_time returns the shorter one
'''

def test_find_best_entry_for_reading_time_returns_suitable_entry():
    d = Diary()
    de1 = DiaryEntry("No1","one two three")
    de2 = DiaryEntry("No2","one two three four five six seven")
    d.add(de1)
    d.add(de2)
    assert d.find_best_entry_for_reading_time(2,3) == de1

'''
Given I add a diary entry 
And I call #find_best_entry_for_reading_time
with a wpm and minutes that means I cannot read that entry
Then #find_best_entry_for_reading_time returns None
'''

def test_find_best_entry_for_reading_time_returns_none():
    d = Diary()
    de2 = DiaryEntry("No2","one two three four five six seven")
    d.add(de2)
    assert d.find_best_entry_for_reading_time(2,3) == None

'''
Given I add 2 entries
And I call #find_best_entry_for_reading_time
And both are suitable
Then #find_best_entry_for_reading_time returns longer one
'''

def test_find_best_entry_for_reading_time_returns_longest():
    d = Diary()
    de1 = DiaryEntry("No1","one two three four five six seven eight nine ten")
    de2 = DiaryEntry("No2","one two three four five six seven")
    d.add(de1)
    d.add(de2)
    assert d.find_best_entry_for_reading_time(2,5) == de1


