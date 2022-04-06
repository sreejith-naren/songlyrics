from flask import Flask, render_template
import crawler
app = Flask(__name__)

@app.route("/")
def hello():
    artists = crawler.get_all_artist()
    return render_template("index.html", artists=artists)

@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs= crawler.get_all_songs(aid)
    singer= crawler.singer(aid)
    artists= crawler.get_all_artist()
    return render_template("songlist.html",artists=artists,songs=songs, singer=singer, current= aid)

@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid,aid):
    lyrics= crawler.get_lyrics(sid)
    songs= crawler.get_all_songs(aid)
    singer= crawler.singer(aid)
    artists= crawler.get_all_artist()
    return render_template("lyrics.html",lyrics=lyrics, artists=artists, songs=songs, singer=singer, current=aid, csong=sid)


if __name__=="__main__":
    app.run(debug=True)