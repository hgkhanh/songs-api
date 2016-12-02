from flask import json

class Songs(object):
    TEST_FILE = 'songs.json'
    songs = []
    
    '''
    Class for handling our songs library. All songs are read from a JSON
    file which is given in the constructor.
    '''

    def __init__(self, data_file):
        '''
        Songs library constructor. All songs are read from the given file.

        @param data_file - Path to the JSON file containing the song definitions.
        '''

        # Read JSON from file
        songs_obj = json.load(open(data_file))['songs']

        # Sort by released
        songs_obj.sort(key=lambda x:x['released'], reverse=True)

        self.songs = songs_obj

    def get_songs(self, skip=0, count=20):
        '''
        List the songs in release date order (newest first).

        @param skip - Number of skipped songs from the beginning.
        @param count - Maximum number of songs returned.

        @return - songs array in JSON format
        '''

        # calculate skip and count to first and last index
        first = skip
        last = skip + count
        
        return self.songs[first:last]

    def get_average_difficulty(self):
        '''
        Calculates the average difficulty of all songs.
        @return - average song difficulty with two decimals in JSON format.
            For example: {"avg_difficulty": 10.01}
        '''

        if(len(self.songs) > 0):
            avg_difficulty = sum((song['difficulty']) for song in self.songs) / len(self.songs)

        formatted_avg_difficulty = float("{0:.2f}".format(avg_difficulty,2))

        result = {}
        result['avg_difficulty'] = formatted_avg_difficulty
        return result

    def search_songs(self, phrase):
        '''
        Searches for songs. Search should take into account song's artist and title.

        @param phrase - Search phrase to be used (case insensitive).

        @return - songs in release date order (newest first) in JSON format (songs
            that matched the search)
        '''

        result = []

        for song in self.songs:
            if (phrase.lower() in song['title'].lower()) or (phrase.lower() in song['artist'].lower()):
                result.append(song)

        return result