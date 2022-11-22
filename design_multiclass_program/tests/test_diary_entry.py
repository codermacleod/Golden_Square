from lib.diary_entry import DiaryEntry

"""
Initial creation of DiaryEntry should assign title and diary entry properties to instance
"""
def test_initial_diary_entry():
    e1=DiaryEntry('entry 1','one two three')
    assert e1.title == 'entry 1'
    assert e1.contents == 'one two three'