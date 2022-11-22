from lib.diary_entry import DiaryEntry

'''
When I initialise the diary entry with 
title and contents
I can get the title and contents back
'''

def test_builds_and_gets_title_and_contents_back():
    de = DiaryEntry("Music Listening", "Chumbawamba stuff is what I was doing")
    assert de.title == "Music Listening"
    assert de.contents == "Chumbawamba stuff is what I was doing"


'''
Given a diary entry
Return number of words in the entry contents
'''

def test_given_entry_returns_number_of_words_in_entry():
    de = DiaryEntry("School Run","Picked up dinner on way to school")
    number_of_words_in_contents = de.count_words()
    assert number_of_words_in_contents == 7


'''
When I initialise with a five-word contents
then #reading_time with a wpm of 2 should return 3
'''

def test_reading_time():
    de = DiaryEntry("No1","one two three four five")
    assert de.reading_time(2) == 3


'''
When I initialise with a five-word chunk
Then at first #reading_chunk should return the first chunk
readable in the time
'''

def test_readable_chunk_first_chunk():
    de = DiaryEntry("No1","one two three four five")
    assert de.reading_chunk(2,1) == "one two"

'''
When I initialise with a five-word chunk
Then secondly #reading_chunk should return the second chunk
readable in the time
'''

def test_readable_chunk_second_chunk():
    de = DiaryEntry("No1","one two three four five")
    de.reading_chunk(2,1) == "one two"
    assert de.reading_chunk(2,1) == "three four"

'''
When I initialise with a five-word contents
then on the third call
#reading_chunk should return the final partial chunk
'''

def test_readable_chunk_third_chunk():
    de = DiaryEntry("No1","one two three four five")
    de.reading_chunk(2,1)
    de.reading_chunk(2,1) 
    assert de.reading_chunk(2,1) == "five"

'''
When I initialise with a five-word contents
then on the fourth call
#reading_chunk should return to the beginning
'''

def test_readable_chunk_fourth_chunk():
    de = DiaryEntry("No1","one two three four five")
    de.reading_chunk(2,1)
    de.reading_chunk(2,1) 
    de.reading_chunk(2,1)
    assert de.reading_chunk(2,1) == "one two"

'''
When I initialise with a six-word contents
then on the fourth call
#reading_chunk should return to the beginning
'''

def test_readable_chunk_fourth_chunk():
    de = DiaryEntry("No1","one two three four five six")
    de.reading_chunk(2,1)
    de.reading_chunk(2,1) 
    de.reading_chunk(2,1)
    assert de.reading_chunk(2,1) == "one two"
