class MusicTracker():
    #no class parameters.
    def __init__(self):
        self.track_list = []

    def add_track(self, track):
        self.track_list.append(track)
        


    def see_track_list(self):
        return self.track_list