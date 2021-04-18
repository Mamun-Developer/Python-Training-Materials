# with open("demo1.txt","rt") as file:
#     for x in file:
#         print(x)

import csv
csvRows = list()
with open("csvExampmle.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        csvRows.append(row)

targetCol = 1
for row in range(1,len(csvRows)):
    print(csvRows[row][targetCol-1])



# a. take a list
# b. insert a dictionary into that list with key (name,age,you)
# c. assign values to those key from csv data row
# d. go to b

csvList = list()
workingRow = 1
totalColum = len(csvRows[0])
for i in range(1,len(csvRows)):
    tempDictionary = dict()
    for j in range(0,totalColum):
        tempDictionary[csvRows[0][j]] = csvRows[i][j]
    csvList.append(tempDictionary)

print(csvList)
print(csvList[0]["name"])
print(csvList[1]["name"])