import lxml.html

prefixes = []

def main(fileopen):

	with open(fileopen, 'r') as myfile:
		user = myfile.read()

	# parses the data on the webpage to locate information
	user_html = lxml.html.fromstring(user)
	memberList = user_html.xpath(r'//table[@role="presentation"]/tbody/tr')
	memberIds = [x.attrib["id"] for x in memberList]
	prefixesTemp = list(set([x for x in memberIds]))
	for i in prefixesTemp:
		if int(i) % 2 == 1:
			prefixesTemp.remove(i)
		else:
			print(i)

main('memberfile1.html')
main('memberfile2.html')
main('memberfile3.html')
main('memberfile4.html')
main('memberfile5.html')
main('memberfile6.html')

print(set(prefixes))