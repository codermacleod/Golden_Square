# File: tests/test_music_library_integration.py
from lib.music_library import MusicLibrary

'''
    Iniitally there are no tracks:
'''

def test_initially_has_no_tracks():
    ml = MusicLibrary()
    assert ml.all() == []


