# {{Music Tracker}} Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class MusicTracker():
    #no class parameters.
    def __init__(self):
    #Add list to hold tracks (<type list>)
        pass

    def add_track(self, track):
        #add track to a track list.(<type string>)
        pass

    def see_track_list(self):
        #see list from __init__ method.
        #<type list>
        #possibly string.
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Add a track to the track_list
which is held in __init__:
"""
mt = MusicTracker()
mt.add_track(track)

"""
See a list of tracks from track_list
which is held in __init__:
"""
mt = MusicTracker()
mt.add_track(track1)
mt.add_track(track2)
mt.add_track(track3)
mt.see_track_list()

