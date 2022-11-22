# File: tests/test_music_library_integration.py
from lib.music_library import MusicLibrary
from lib.track import Track

'''
Test adds multiple tracks and lists them:
'''
def test_adds_multiple_tracks_and_lists_them():
    library = MusicLibrary()
    track_1 = Track("Surfing With The Alien", "Joe Satriani")
    track_2 = Track("For The Love Of God", "Steve Vai")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Surfing With The Alien") == [track_1]

'''
Given I add 2 tracks
If I search for part of the title of one of the tracks
I get that track back in the results
'''


def test_searches_by_part_of_title():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Hard") == [track_1]


'''
Initially, searching for tracks gets an empty list:
'''

def test_initial_search_gets_an_empty_list():
    library = MusicLibrary()
    assert library.search_by_title("Checker") == []