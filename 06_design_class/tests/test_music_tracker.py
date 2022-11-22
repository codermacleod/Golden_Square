from lib.music_tracker import MusicTracker

"""
Add a track to the track_list
which is held in __init__:
"""
def test_adds_track_to_track_list():
    mt = MusicTracker()
    mt.add_track("Dignity")
    result = mt.track_list
    assert result == ["Dignity"]
    

"""
See a list of tracks from track_list
which is held in __init__:
"""

def test_see_track_list():
    mt = MusicTracker()
    mt.add_track("Dignity1")
    mt.add_track("Dignity2")
    mt.add_track("Dignity3")
    result = mt.see_track_list()
    assert result == ["Dignity1","Dignity2","Dignity3"]
    