# importing encapsulated helpers
from classes import Channel
import dbcontrol

# the flask part of the app
import urllib.parse
from flask import *
app = Flask(__name__)

@app.context_processor
def context1():
	contextDict = {}
	contextDict['list']=list
	contextDict['quote']=urllib.parse.quote
	return contextDict

@app.route('/')
def index():
	history, video = request.cookies.get('history'), request.args.get('url')
	history, video = dbcontrol.recents(history, video)
	resp = make_response(render_template('home.html', vid = video, history = [Channel(i) for i in history.split(";")]))
	resp.set_cookie('history', history)
	return resp

@app.route('/menu/')
def menu():
	return render_template('menu.html', tagData=dbcontrol.channelsByTag())

@app.route('/blacklist/')
def blacklist():
	video = request.args.get('url')
	if video != "" or video != None:
		dbcontrol.delete(video)
	return redirect(request.referrer)

@app.route('/favorite/')
def favorite():
	video = request.args.get('url')
	if video != "" or video != None:
		dbcontrol.like(video)
	return redirect(request.referrer)


@app.route('/refresh/')
def refresh():
	dbcontrol.importm3u()
	return redirect(request.referrer)
