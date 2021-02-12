import sqlite3 as lite
from classes import *
import re, requests
import json


def delete(url):
	con = lite.connect("ipdb.db")
	cur = con.cursor()
	with con:
		cur.execute("DELETE FROM CHANNELS WHERE URL = ?", (video,))
		cur.execute("DELETE FROM TAGS WHERE URL = ?", (video,))
		cur.execute("INSERT OR IGNORE INTO BLACKLIST (URL) VALUES (?)" (video,))

# given the history cookie and the video to be played, returns new history cookie and video
def recents(history, video):
	if history == "":
		history = None
	if video == "":
		video = None
	# providing a video and history if none exist
	if video != None:
		video = unquote(video)
	if history == None and video == None:
		video = "http://ott-cdn.ucom.am/s24/index.m3u8?fluxustv.m3u8"
	print(video)
	if history == None:
		history = video
	history = history.split(";")
	if video == None:
		video = history[-1]
	# if video is in history already, move it to the back of the list, else set it to the back of the list
	history.append(history.pop(history.index(video)) if video in history else video)
	if len(history) > 22:
		history.pop(0)
	history = ";".join(history)
	return (history, video)

# fetches all the channels, and groups them by tag, from most popular to least
def channelsByTag():
	con = lite.connect("ipdb.db")
	cur = con.cursor()
	tagsData = {}
	with con:
		cur.execute("SELECT URL FROM TAGS WHERE TAG = 'FAVORITES'")
		favorites = [Channel(i[0]) for i in cur.fetchall()]
		tagsData['FAVORITES'] = favorites
		cur.execute("SELECT DISTINCT TAG FROM TAGS WHERE NOT TAG = 'FAVORITES' GROUP BY TAG ORDER BY COUNT(TAG) DESC")
		tags = [i[0] for i in cur.fetchall()]
		for i in tags:
			cur.execute("SELECT URL FROM TAGS WHERE TAG = ?", (i,))
			tagsData[i] = [Channel(j[0]) for j in cur.fetchall()]
	return tagsData

def tag(tag, url):
	con = lite.connect("ipdb.db")
	cur = con.cursor()
	tag = tag.lower().capitalize()
	with con:
		cur.execute("""INSERT OR IGNORE INTO TAGS (TAG, URL) VALUES (?, ?)""", (tag, url))


def like(url):
	tag('FAVORITES', url)

# searches for the url in the database, and outputs it, along with a name and a logo
def search(url):
	if url == None:
		return None, None, None
	con = lite.connect("ipdb.db")
	cur = con.cursor()
	with con:
		cur.execute("SELECT * FROM CHANNELS WHERE URL = ?", (url,))
	results = cur.fetchall()
	url, name, logo, *useless = (results[0]) if (len(results) > 0) else (None, None, None)
	return (url, name, logo)

# inserts a channel object into the database
def insert(c):
	if c.url != None:
		con = lite.connect("ipdb.db")
		cur = con.cursor()
		with con:
			cur.execute("""INSERT OR REPLACE INTO CHANNELS (URL, NAME, LOGO) VALUES (?, ?, ?)""", (c.url, c.name, c.logo))
		for j in c.tags:
			tag(j, c.url)

# gets the channels from the m3u file and loads them into the database
def importm3u(m3uFile="https://raw.githubusercontent.com/heckletstech/heckletstech1/master/heckletstech%20copy.m3u"):
	s = requests.session()
	text = s.get(m3uFile).text
	search = re.compile("#EXTINF:.*\n.*m3u8").findall(text)
	[insert(Channel(i)) for i in search]

def importjson(jsonfile="https://iptv-org.github.io/iptv/channels.json"):
	with open('save', 'r') as savefile:
		saveData = int(savefile.read().splitlines()[0])
	savefile.close()
	s = requests.session()
	text = s.get(jsonfile).text
	jsonfile = json.loads(text)[saveData:]
	print("FILE LOADED")
	for a, i in enumerate(jsonfile[saveData:]):
		if a%10==0:
			with open('save', 'w+') as savedfile:
				savedfile.write(str(a+saveData))
		c = Channel(i, tf="json")
		print(saveData+a, ". ", c.name)
		insert(c)


def newDb(name="ipdb.db"):
	con = lite.connect(name)
	cur = con.cursor()
	try:
		with con:
			cur.execute("CREATE TABLE CHANNELS(\nURL TEXT PRIMARY KEY,\nNAME TEXT NOT NULL,\nLOGO TEXT NOT NULL\n)")
			cur.execute("CREATE TABLE TAGS(\nTAG TEXT NOT NULL,\nURL TEXT NOT NULL\n)")
			cur.execute("CREATE TABLE BLACKLIST(\nURL TEXT NOT NULL\n)")
	except:
		pass