from dbcontrol import *
import re
import requests
import json

class Channel:
	@staticmethod
	def ufChannel(uf):
		try:
			name = (re.compile(",(.*?)\n").findall(url))[0]
			logo = (re.compile('tvg-logo="(.*?)"').findall(url))[0]
			url = (re.compile("\nhttp.*m3u8")).findall(url)[0][1:]
		except:
			return (None, None, None)
		s = requests.session()
		text = s.get(url).text
		if len(re.compile('EXTINF:.*\n.*m3u8').findall(url)) < 1:
			return (None, None, None)
		search = re.compile('group-title="(.*?)",').findall(url)
		tags = (search[0]).split(";") if len(search) > 0 else []
		return (url, name, logo, tags)

	@staticmethod
	def jsonChannel(jsonfile):
		if isinstance(jsonfile, str):
			try:
				jsonfile = json.loads(jsonfile)
			except:
				return (None, None, None, None)
		name = jsonfile['name']
		logo = jsonfile['logo'] if jsonfile['logo'] != None else ""
		url = jsonfile['url']
		tags = []
		if name == "" or url == "" or name == None or url == None:
			return (None, None, None, None)
		s = requests.session()
		if url[-3:] != "m3u" and url[-4:] != "m3u8":
			return (None, None, None, None)
		try:
			text = s.get(url).text
		except:
			return (None, None, None, None)
		if len(re.compile('EXT').findall(text)) < 1:
			return (None, None, None, None)
		if jsonfile['category'] != None:
			tags.extend(jsonfile['category'])
		if jsonfile['country']['name'] != None:
			tags.extend(jsonfile['country']['name'])
		if tags == []:
			tags.append("Unsorted")
		return (url, name, logo, tags)


	def __init__(self, url, name=None, logo=None, tf="na"):
		self.tags=[]
		if tf == "json":
			self.url, self.name, self.logo, self.tags = Channel.jsonChannel(url) 
		elif name == None or logo == None:
			try:
				if re.compile("#EXTINF:.*\n.*m3u8").match(url):
					self.url, self.name, self.logo, self.tags = Channel.ufChannel(url)
				else:
					self.url, self.name, self.logo, *useless = search(url)
			except:
				self.url, self.name, self.logo = None, None, None
		else:
			self.url,self.name,self.logo=url,name,logo