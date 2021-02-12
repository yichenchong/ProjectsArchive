# simple program to search for the number of occurrences of a word within any given webpage.
# built for my brother's sentiment analysis project, so that he could check through 500 news articles for the word count of a
# preset list of words, to determine emotional bias in the description.

import requests
from bs4 import BeautifulSoup

keywords = input("List the keywords, separated by commas (without spaces).\n").split(",")

while True:
	page = input("Input the website URL: ")
	txt = BeautifulSoup(requests.get(page).text, features="lxml").get_text().upper()
	for i in keywords:
		print(i + ": " + str(txt.count(i.upper())))