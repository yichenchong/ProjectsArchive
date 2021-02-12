# simple test to generate a searchable HTML file from the data folder
# this data crawl was done by my friend, and so did not have a very usable format
# and did not contain a lot of information
# I built a web crawler after this to do it better

# the images in the data folder have the following naming format:
# Yi Chen Chong_yichen01px2019@saschina.org_PX High School_3283

import os
import sys
# setup
f = []
schoolLevels = 0
html = ""
currentPath = sys.path[0]
pathToData = os.path.join(currentPath,"data")
for (dirpath, dirnames, filenames) in os.walk(pathToData):
	f.extend(filenames) # places filenames in array "f"
	a = dirpath # finding the directory of the pictures in case the directory changes
	break
count = 0

# data extraction
for i in range(len(f)):
	preferredName = ""
	pictureAddress = os.path.join("./data", f[i]) # joins the directory to the pictureName
	pictureName = f[i] # isolates the picture name for further analysis
	if (pictureName != ".DS_Store"):
		attributes = pictureName.split("_") # splits name into its attributes
		fullName = attributes[0]
		email = attributes[1]
		school = attributes[2]
		numberExtension = attributes[3]
		
		# name parsing
		nameParts = fullName.split(" ")
		preferredNameNumber = 472
		for i in range(len(nameParts)):
			namePart = nameParts[i]
			nameNumber = i
			if (namePart[0]=="("):
				preferredNameEnd = len(namePart) - 1
				preferredName = namePart[1:preferredNameEnd]
				preferredNameNumber = nameNumber
		if (preferredNameNumber != 472):
			nameParts.pop(preferredNameNumber)
		lastName = (nameParts[len(nameParts) - 1])
		nameParts.pop(len(nameParts) - 1)
		firstNameArray = nameParts
		firstName = " ".join(firstNameArray)
		
		#numberExtension parsing
		numberEnd = len(numberExtension) - 4
		studentNumber = numberExtension[0:numberEnd]

		#email parsing
		teacherDeterminer = email.count(".")
		if(teacherDeterminer == 2):
			role = "Teacher"
		else:
			role = "Student"
		emailParts = email.split("@")
		username = emailParts[0]
		if username == "firmansyah":
			role = "Teacher"
		if (role == "Student"):
			if (email != ""):
				graduationYearStart = len(username) - 4
				graduationYearEnd = graduationYearStart + 4
				graduationYearString = email[graduationYearStart:graduationYearEnd]
				graduationYear = int(float(graduationYearString))
				yearsToGraduate = graduationYear - 2018
				grade = 12 - yearsToGraduate
				grade = str(grade)
			else:
				grade = "Small"
		else:
			grade = " Teacher"
		
		#school parsing
		schoolParts = school.split(" ")
		campus = schoolParts[0]
		schoolDeterminer = schoolParts[1]
		if (schoolDeterminer == "Elementary"):
			schoolLevel = "ES"
		elif (schoolDeterminer == "Middle"):
			schoolLevel = "MS"
		elif (schoolDeterminer == "High"):
			schoolLevel = "HS"

		# at this point, we have created the following pieces of data:
		# pictureAddress: The path to the picture
		# pictureName: The name of the picture
		# firstName, lastName, preferredName, email, grade: self-explanatory
		# school: e.g. PX High School
		# role: Teacher or Student
		# campus: PX/PD
		# schoolLevel : HS/MS/ES
		# studentNumber: last 4 digits of schoology number
		htmlBreak = """</td><td>"""
		html = html + """<tr class="row"><td>""" + firstName + htmlBreak + lastName + htmlBreak + preferredName + htmlBreak + email + htmlBreak + grade + htmlBreak + studentNumber + htmlBreak + campus + htmlBreak + schoolLevel + htmlBreak + """<img src=" """ + pictureAddress + """ " height="200" class="schoologyPhoto"></td></tr>"""
		if grade == "10":
			if campus == "PD":
				count = count + 1

print(html)






