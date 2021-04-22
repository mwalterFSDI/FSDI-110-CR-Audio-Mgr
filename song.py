"""
id, title, featured_artist, length, written_by
"""
class Song:
    id = 0
    title = ""
    featured_artist = ""
    length_of_song = ""
    written_by = ""

    def __init__ (self, id, title, featured_artist, length_of_song, written_by):
        self.id = id
        self.title = title
        self.featured_artist = featured_artist
        self.length_of_song = length_of_song
        self.written_by = written_by

