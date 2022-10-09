import csv
with open('C:\\Users\\sornasree\\Desktop\\name_list.csv', mode ='r')as file:
	csvFile = csv.reader(file)
	for lines in csvFile:
			print(lines)