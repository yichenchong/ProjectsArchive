import sys
import os
currentPath = sys.path[0]
pathToDictionary = os.path.join(currentPath,"corncob_lowercase.txt")
handle=open(pathToDictionary,'r+')
dictionaryText = handle.read()
wordList = dictionaryText.split("\n")

alphabet=" abcdefghijklmnopqrstuvwxyz"

for i in range(len(wordList)):
	alphabetSum=0
	word=wordList[i]
	for x in range(len(word)):
		alphabetSum+=alphabet.find(word[x])
	if alphabetSum==100:
		print(word)
