from lib.track import Track
# File: lib/track.py

'''
When we create a new track
we get the title and artist back
'''

def test_create_track_and_get_title_and_artist():
    tr = Track("Flying in a Blue Dream", "Joe Satriani")
    assert tr.title == "Flying in a Blue Dream"
    assert tr.artist == "Joe Satriani"

'''
Returns a nicer human readable 
sentence when
'''

def test_formats_title_and_artist():
    tr = Track("Bad Horsie", "Joe Satriani")
    assert tr.format() == "Bad Horsie by Joe Satriani"
    