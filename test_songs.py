import unittest, json
from songs import Songs

class SongsTests(unittest.TestCase):

    def test_get_songs(self):
        songs_library = Songs(Songs.TEST_FILE)
        songs = json.loads(songs_library.get_songs())
        #check the count
        self.assertEqual(6, len(songs))
        #check ordering
        self.assertEqual("Lycanthropic Metamorphosis", songs[0]['title'])
        self.assertEqual("The Yousicians", songs[0]['artist'])
        self.assertEqual("Wishing In The Night", songs[1]['title'])
        self.assertEqual("You've Got The Power", songs[2]['title'])
        self.assertEqual("Opa Opa Ta Bouzoukia", songs[3]['title'])
        self.assertEqual("Awaki-Waki", songs[4]['title'])
        self.assertEqual("Mr Fastfinger", songs[4]['artist'])
        self.assertEqual("A New Kennel", songs[5]['title'])

    def test_get_songs_paging(self):
        songs_library = Songs(Songs.TEST_FILE)
        songs = json.loads(songs_library.get_songs(skip=1, count=2))
        self.assertEqual(2, len(songs))
        self.assertEqual("Wishing In The Night", songs[0]['title'])
        self.assertEqual("You've Got The Power", songs[1]['title'])

        songs = json.loads(songs_library.get_songs(skip=5, count=2))
        self.assertEqual(1, len(songs))
        self.assertEqual("A New Kennel", songs[0]['title'])

        songs = json.loads(songs_library.get_songs(skip=6, count=20))
        self.assertEqual(0, len(songs))

        songs = json.loads(songs_library.get_songs(skip=0, count=0))
        self.assertEqual(0, len(songs))

    def test_get_average_difficulty(self):
        songs_library = Songs(Songs.TEST_FILE)
        avg_difficulty = json.loads(songs_library.get_average_difficulty())['avg_difficulty']
        self.assertEqual(12.93, avg_difficulty)

    def test_search(self):
        songs_library = Songs(Songs.TEST_FILE)
        songs = json.loads(songs_library.search_songs('Lycanthropic'))
        self.assertEqual("Lycanthropic Metamorphosis", songs[0]['title'])
        self.assertEqual(1, len(songs))
        results = json.loads(songs_library.search_songs('metamorphosis'))
        self.assertEqual(1, len(songs))
        self.assertEqual("Lycanthropic Metamorphosis", songs[0]['title'])

        songs = json.loads(songs_library.search_songs('The YOUsicians'))
        self.assertEqual(5, len(songs))
        self.assertEqual("Lycanthropic Metamorphosis", songs[0]['title'])
        self.assertEqual("Wishing In The Night", songs[1]['title'])
        self.assertEqual("You've Got The Power", songs[2]['title'])
        self.assertEqual("Opa Opa Ta Bouzoukia", songs[3]['title'])
        self.assertEqual("A New Kennel", songs[4]['title'])

        songs = json.loads(songs_library.search_songs('xx'))
        self.assertEqual(0, len(songs))

        songs = json.loads(songs_library.search_songs(''))
        self.assertEqual(6, len(songs))


#execute the tests
if __name__ == '__main__':
    unittest.main()
