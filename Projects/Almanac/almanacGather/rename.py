import sqlite3 as lite
import shutil
import os

filesList = os.listdir("./img")
idList = []
for i in filesList:
	if i != ".DS_Store":
		idList.append(i[:-4])

con = lite.connect('almanac.db')
cur = con.cursor()

def sanitize(output):
	output = output.replace("/","")
	return output

def formatString(dataTuple):
	if(dataTuple[5]==50):
		grade="Teacher"
	else:
		grade="Grade-"+str(dataTuple[5])
	if dataTuple[2]!="":
		output = str(dataTuple[0])+" - "+dataTuple[1]+" "+dataTuple[3]+" ("+dataTuple[2]+")_"+dataTuple[4]+"_"+grade+" "+dataTuple[6]+" "+dataTuple[7]+" "+dataTuple[8]
	else:
		output = str(dataTuple[0])+" - "+dataTuple[1]+" "+dataTuple[3]+"_"+dataTuple[4]+"_"+grade+" "+dataTuple[6]+" "+dataTuple[7]+" "+dataTuple[8]
	sanOutput = sanitize(output)
	return sanOutput

for schid in idList:
	statement = """SELECT * FROM DATA WHERE ID = {}""".format(schid);
	cur.execute(statement)
	dataTuple = cur.fetchall()[0]
	dataString = formatString(dataTuple)
	shutil.move("./img/"+schid+".jpg","./img/"+dataString+".jpg")

