# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        # Parameters:
        self.title = title
        self.artist = artist

    def format(self):
        return f"{self.title} by {self.artist}"
