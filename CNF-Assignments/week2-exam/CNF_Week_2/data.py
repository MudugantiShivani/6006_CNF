import csv

with open('data.csv') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
    	data[row[0]]=[row[1], row[2]]

csvFile.close()