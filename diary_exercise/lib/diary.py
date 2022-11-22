
from math import ceil

class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list

    def all(self):
        return self._entries
        

    def count_words(self):
        total_words = 0
        for entry in self._entries:
            total_words += entry.count_words()
        return total_words


    def reading_time(self, wpm):
        if self._entries == []:
            raise Exception("No entries added yet")
        word_count = self.count_words()
        return ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._entries == []:
            raise Exception("No entries added yet")
        words_user_could_read = wpm * minutes
        readable_entries = []
        for entry in self._entries:
            if entry.count_words() <= words_user_could_read:
                readable_entries.append(entry)
        readable_entries.sort(key = lambda x : x.count_words())
        if readable_entries == []:
            return None
        return readable_entries[-1]


# File: lib/diary_entry.py

