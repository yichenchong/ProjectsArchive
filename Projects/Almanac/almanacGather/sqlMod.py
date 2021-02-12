import os
import sqlite3 as lite

# sets up the sql
con = lite.connect('almanac.db')
cur = con.cursor()

# gets a list of all the schids in sql
cur.execute("""SELECT ID FROM DATA""")
sqlTuples = cur.fetchall()
sqlschids = []
for i in sqlTuples:
	sqlschids.append(str(i[0]))


# gets a list of all the schids in img
filesList = os.listdir("./img")
idList = []
for i in filesList:
	if i != ".DS_STORE":
		idList.append(i[:-4])

# creates a list of schids in sql not present in img
modList = []
for i in sqlschids:
	if not (i in idList):
		modList.append(i)

# deletes those schids from sql
for i in modList:
	statement = """DELETE FROM DATA WHERE ID = {}""".format(i)
	cur.execute(statement)

print(len(sqlschids))

cur.execute("""SELECT ID FROM DATA""")
sqlTuples = cur.fetchall()
sqlschids = []
for i in sqlTuples:
	sqlschids.append(str(i[0]))

print(len(sqlschids))
print(len(modList))

con.commit()