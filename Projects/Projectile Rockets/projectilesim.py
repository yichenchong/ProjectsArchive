import projectilerocket
import csv

# creates results
results = []
for mass in [(i + 1) * 10 for i in range(1000)]:
	results.append((mass, projectilerocket.resultant(m = mass)[1]))

file = open("massvdistance.csv","w+")
csvWriter = csv.writer(file,delimiter=',')
csvWriter.writerows(results)
file.close()