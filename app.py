from flask import Flask, render_template, jsonify
import crawler
app = Flask(__name__)

@app.route("/")
def hello():
    #artists = crawler.get_all_artist()
    return render_template("base.html")

@app.route("/artist")
def get_artist():
    artists = crawler.get_all_artist()
    artist_array=[{"id":i[0], "name" : i[1]} for i in artists] 
    return jsonify(artist_array)   

@app.route("/songs/<int:aid>")
def list_all_songs(aid): 
    songs= crawler.get_all_songs(aid)
    singer= crawler.singer(aid)
    artists= crawler.get_all_artist()
    song_array=[{"song_id":i[1], "song_name" : i[0]} for i in songs]
    return jsonify(song_array)

@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid,aid):
    lyrics= crawler.get_lyrics(sid)
    songs= crawler.get_all_songs(aid)
    singer= crawler.singer(aid)
    artists= crawler.get_all_artist()
    return jsonify(lyrics)


if __name__=="__main__":
    app.run(debug=True)