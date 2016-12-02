from flask import Flask, request, session
import json
from songs import Songs


#Start the API
app = Flask(__name__)


@app.route('/')
def home():
    return "Home"

@app.route('/songs', methods=['GET'])
def get_all_songs():
    skip = int(request.args.get('skip', 0))
    count = int(request.args.get('count', 20))

    songs_library = Songs(Songs.TEST_FILE)
    return songs_library.get_songs(skip, count)


@app.route('/songs/avg/difficulty', methods=['GET'])
def get_songs_average_difficulty():
    songs_library = Songs(Songs.TEST_FILE)
    return songs_library.get_average_difficulty()


@app.route('/songs/search', methods=['GET'])
def search_songs():
    phrase = request.args.get('phrase', '')
    songs_library = Songs(Songs.TEST_FILE)
    return songs_library.search_songs(phrase)

@app.route('/songs/meta', methods=['GET'])
def get_songs_meta():
    meta = session.get('songs_meta', {})
    return json.dumps(meta)

@app.route('/songs/meta', methods=['POST'])
def set_songs_meta():
    meta = session.get('songs_meta', {})
    meta.update(request.json['meta'])
    session['songs_meta'] = meta

    return json.dumps(meta)

app.secret_key = 'our secret!'
#app.config['SESSION_TYPE'] = 'filesystem'
app.run(port=5005, debug=True, threaded=True)
