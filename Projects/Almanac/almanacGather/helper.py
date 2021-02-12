# TODO: edit nameParse
def nameParse(fullName):
	nameParts = fullName.split(" ")
	preferredNameList = [472,483]
	for i in range(len(nameParts)):
		namePart = nameParts[i]
		nameNumber = i
		if len(namePart) > 0:
			if (namePart[0]=="("):
				preferredNameStart = i
				preferredNameList[0] = preferredNameStart
			if (namePart[-1]==")"):
				preferredNameEnd = i+1
				try:
					preferredNameList[1] = preferredNameEnd
				except:
					preferredNameList = [472,483]
	if (preferredNameList[0] != 472 and preferredNameList[1] != 483):
		preferredNameSep = nameParts[preferredNameList[0]:preferredNameList[1]]
		preferredNameU = " ".join(preferredNameSep)
		preferredName = preferredNameU[1:-1]
		
		preferredNameDiff = preferredNameList[1] - preferredNameList[0]
		for i in range(preferredNameDiff):
			nameParts.pop(preferredNameList[0])
	lastName = (nameParts[-1])
	nameParts.pop(-1)
	firstNameArray = nameParts
	firstName = " ".join(firstNameArray)
	try:
		return [firstName,preferredName,lastName]
	except UnboundLocalError:
		return [firstName,"", lastName]

def mailParse(address):
	teacherDeterminant = address.count(".")
	if(teacherDeterminant == 2):
		role = "Teacher"
	else:
		role = "Student"
	emailParts = address.split("@")
	username = emailParts[0]
	if username == "firmansyah":
		role = "Teacher"
	if (role == "Student"):
		if (address != "NaN"):
			try:
				graduationYear = int(float(username[-4:]))
				yearsToGraduate = graduationYear - 2019
				grade = 12 - yearsToGraduate
			except ValueError:
				grade="404"
		else:
			grade = 0
	else:
		grade = 50
	return grade

def schoolParse(school):
	schoolParts = school.split(" ")
	if len(schoolParts) == 0:
		return ["NaN"]
	campus = schoolParts[0]
	if len(schoolParts) == 1:
		return [campus, "NaN"]
	schoolDeterminer = schoolParts[1]
	if schoolDeterminer == "Elementary":
		schoolLevel = "ES"
	elif schoolDeterminer == "Middle":
		schoolLevel = "MS"
	elif schoolDeterminer == "High":
		schoolLevel = "HS"
	else:
		schoolLevel = "NaN"
	return [campus, schoolLevel]