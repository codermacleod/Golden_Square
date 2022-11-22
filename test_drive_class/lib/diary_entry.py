class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
    def format(self):
        formatted_result = self.title + ": " + self.contents
        return formatted_result
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"

    def count_words(self):
        word_list = self.contents.split(" ")
        return len(word_list)
        # Returns:
        #   int: the number of words in the diary entry
        pass

    def reading_time(self, wpm):
        reading_time = self.count_words() / wpm
        return str(reading_time) + " minutes to read."
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.

    def reading_chunk(self, wpm, minutes):
        word_chunk = wpm * minutes
        original_word_list = self.contents.split(" ")
        final_chunk = original_word_list[0:word_chunk]
        return " ".join(final_chunk)
        
    
        # contents(300) / 200 wpm => reading time 1.5 minutes
        # minutes * wpm => = reading_chunk



        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass