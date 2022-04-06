import requests
from bs4 import BeautifulSoup
import psycopg2

def get_artists(url):
    ret = []
    r = requests.get(url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklist = soup.find("table", {"class": "tracklist"})
    links = tracklist.find_all("a")
    for i in links:
        ret.append((i.text, i['href']))
    return ret

def get_songs(artist_url):
    songs=[]
    r = requests.get(artist_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    tracklists = soup.find("table", {"class" : "tracklist"})
    links=tracklists.find_all("a")
    for i in links:
        songs.append((i.text,i['href']))
    return songs

def get_lyrics(song_url):
    r = requests.get(song_url)
    body = r.content
    soup = BeautifulSoup(body, features="html.parser")
    lyrics_div = soup.find("p", {"id": "songLyricsDiv"})
    lyrics = lyrics_div.text
    return lyrics

def crawl():
    conn = psycopg2.connect("dbname=lyrics")
    cur = conn.cursor()
    artists= get_artists("https://www.songlyrics.com/a/")
    for name, link in artists[:10]:
        cur.execute("INSERT INTO artist (name) VALUES (%s);", (name,))
        # print(name, " : ",link)
        songs = get_songs(link)
        for song, song_link in songs[:10]:
                lyrics = get_lyrics(song_link)
                cur.execute("INSERT INTO song (artist, name, lyrics) VALUES ((select id from artist where name=%s),%s,%s);", (name,song,lyrics))    
    conn.commit()
    print("DONE")

def get_all_songs(aid):
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select song.name, song.id from song,artist where artist.id = song.artist and artist.id=%s",(aid,))  
    songs= cur.fetchall()
    return songs

def get_all_artist():
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select id,name from artist" )  
    artists= cur.fetchall()
    return artists

def get_lyrics(sid):
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select lyrics,name from song where id=%s",(sid,))
    lyric= cur.fetchone()
    return lyric

def singer(artistid):
    conn = psycopg2.connect("dbname=lyrics")
    cur=conn.cursor()
    cur.execute("select id,name from artist where artist.id=%s",(artistid,))  
    singer= cur.fetchone()
    return singer    



if __name__ == "__main__":
    crawl()
