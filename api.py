from flask import Flask, request, session, render_template, redirect, url_for
import json
from songs import Songs


#Start the API
app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('get_all_songs'))

@app.route('/songs', methods=['GET'])
def get_all_songs():
    skip = int(request.args.get('skip', 0))
    count = int(request.args.get('count', 20))

    songs_library = Songs(Songs.TEST_FILE)
    songs = songs_library.get_songs(skip, count)
    return render_template("pages/songs.html", songs=songs)


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

    return json.dumps(session)

@app.route('/songs/<id>/meta', methods=['GET'])
def get_songs_meta_by_id(id):
    meta = session.get('songs_meta', {}).get(id, {})
    return json.dumps(meta)

@app.route('/songs/<id>/meta', methods=['POST'])
def set_songs_meta_by_id(id): 
    meta = session.get('songs_meta', {})
    meta.update({
        id : {
        'Clicked': True
        }
    })    
    session['songs_meta'] = meta
    return json.dumps(session['songs_meta'])

app.secret_key = 'our_secret!'
#app.config['SESSION_TYPE'] = 'filesystem'
app.run(port=5005, debug=True, threaded=True)
