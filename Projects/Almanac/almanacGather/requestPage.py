# the main script. Accessed the schoology page and downloaded all the files and information

import requests, lxml.html, sys
import helper, imgDownload
import sqlite3 as lite
import crackgen
import urllib
import time

prefixes = # list of prefixes predetermined, masked via comments for privacy reasons


# read text file to determine username and password, password file not included for privacy reasons. The first line of the file is my username and the next line is my password
with open('pword.txt', 'r') as myfile:
	pwordData = myfile.read()
pwordDataList = pwordData.splitlines()
email = pwordDataList[0]
password = pwordDataList[1]
myfile.close()

# determine previous save
with open('save', 'r') as savefile:
	saveData = savefile.read()
saveDataList = saveData.splitlines()
try:
	saveLocSuffix = int(saveDataList[0])
except ValueError:
	saveLocSuffix = 0
try:
	saveLocPrefix = int(saveDataList[1])
except ValueError:
	saveLocPrefix = 0
print("Starting at {}({}),{}".format(saveLocPrefix,prefixes[saveLocPrefix], saveLocSuffix))
savefile.close()

# connect and configure database, which is present in the same directory as this script
con = lite.connect('almanac.db')
cur = con.cursor()

# this auto-save feature was written, because the process took days to run through, so it was useful to save the extent of my progress
def save(number):
	with open('save', 'w+') as savedfile:
		savedfile.write(number)

def getData(prefix,suffix):
	try:
		# uses the prefix and suffix to get the URL
		schoologyId = "{}{}".format(prefix,suffix)
		user = s.get("https://saschina.schoology.com/user/{}/info".format(schoologyId))

		# parses the webpage to locate data
		user_html = lxml.html.fromstring(user.text)
		if len(user_html.xpath(r'//h2/text()')) == 0:
			return {}
		print(user_html.xpath(r'//h2/text()')[0])
		if user_html.xpath(r'//h2/text()')[0] == "Oops! Page Not Found" or user_html.xpath(r'//h2/text()')[0]== "Private Access Only":
			return {}
		if user_html.xpath(r'//h2/text()')[0] == "Uh-oh! Too Many Requests":
			print("Sleeping...")
			time.sleep(6)
			getData(prefix,suffix)
			return {}
		name = user_html.xpath(r'//h2/text()')[0]
		try:
			gender = user_html.xpath(r'//table[@class="info-tab"]/tbody/tr/th[normalize-space(.) = "Gender"]/following-sibling::td[1]/text()')[0]
		except IndexError:
			gender = "NaN"
		try:
			email = user_html.xpath(r'//table[@class="info-tab"]/tbody/tr/td/span/a/text()')[0]
		except IndexError:
			email = "NaN"
		try:
			dataTableInfo = [name,gender,email,user_html.xpath(r'//span[@class="school-name"]/a/b/text()')[0]]
		except IndexError:
			print("Information not found...")
			return {}
		dataTableHeaders = ['name', 'gender', 'email', 'school']
		for i in range(len(dataTableInfo)):
			if dataTableInfo[i] == ' ':
				dataTableInfo[i] = "NaN"
		data = {dataTableHeaders[x]:dataTableInfo[x] for x in range(4)}
		data["id"]=schoologyId

		# parses the data to get useful information
		fullName = data['name']
		nameList = helper.nameParse(fullName)
		schoolMail = data['email']
		grade = helper.mailParse(schoolMail)
		fullSchool = data['school']
		schoolList = helper.schoolParse(fullSchool)

		# Downloads the profile photo
		imgurlelist = user_html.xpath(r'//div/div[@class="profile-picture"]/img')
		if len(imgurlelist) > 0:
			imgurle = imgurlelist[0]
			imgurl=imgurle.attrib["src"]
			imgDownload.url_to_image(imgurl, schoologyId)

		# compile data into list
		fullData = [schoologyId]
		fullData.extend(nameList)
		fullData.append(schoolMail)
		fullData.append(grade)
		fullData.append(data["gender"])
		fullData.extend(schoolList)

		# insert the data into the table if it isn't there already, and update the table if it is already present.
		try:
			with con:
				cur.execute("""INSERT INTO DATA (ID, FirstName, MiddleName, LastName, Email, Grade, Gender, Campus, SchoolLevel) VALUES ({idNo}, '{first}', '{middle}', "{last}", "{email}", {age}, "{gender}", "{campus}", "{schoolLevel}")""".format(idNo=fullData[0],first=fullData[1],middle=fullData[2],last=fullData[3],email=fullData[4],age=fullData[5],gender=fullData[6],campus=fullData[7],schoolLevel=fullData[8]))
		except lite.IntegrityError:
			print("Updating...")
			with con:
				cur.execute("""UPDATE DATA SET (FirstName, MiddleName, LastName, Email, Grade, Gender, Campus, SchoolLevel) = ("{first}", "{middle}", "{last}", "{email}", {age}, "{gender}", "{campus}", "{schoolLevel}") WHERE ID = {idNo}""".format(idNo=fullData[0],first=fullData[1],middle=fullData[2],last=fullData[3],email=fullData[4],age=fullData[5],gender=fullData[6],campus=fullData[7],schoolLevel=fullData[8]))
			return {}
	except (KeyboardInterrupt, SystemExit, ConnectionError):
		raise
def main(saveLocSuffix):
	# iterate through the prefixes and suffixes
	for x in range(saveLocPrefix,len(prefixes)):
		prefix=prefixes[x]
		print("Now on prefix {}".format(prefix))
		suffixes=crackgen.crackgen(4)
		suffixes.sort()
		for i in range(saveLocSuffix,len(suffixes)):
			try:
				suffix = suffixes[i]
				if i % 20 == 0:
					save("{}\n{}".format(suffix,x))
				print("Trying {}".format(suffix), end=" - ")
				getData(prefix,suffix)
			except (KeyboardInterrupt, SystemExit, ConnectionError):
				raise
		saveLocSuffix = 0
	print("Done.")

# sets up a session so that the code can enter
s = requests.session()
login = s.get('https://saschina.schoology.com/login/ldap?school=521082293')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
form['mail'] = email
form['pass'] = password
response = s.post('https://saschina.schoology.com/login/ldap?school=521082293', data=form)
if response.url=='https://saschina.schoology.com/login/ldap?school=521082293':
	print("ERROR 404: CAN NOT LOG IN")
	print("Check if your username or password is correct, or contact the System Administrator")
else:
	try:
		main(saveLocSuffix)
	# error handling
	except (KeyboardInterrupt, SystemExit):
		print("Exiting")