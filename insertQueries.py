import csv

# stores each line from the csv file
eachLineList = []

# opening sql file where queries will be inserted to write to it
queryInserter = open('insert.sql', 'w+')

# opening the csv file to read from it
with open('Customers.csv', mode = "r") as csvFile:
    customerCsvFile = csv.reader(csvFile)

    # Ensuring no null values are entered in the Profession column
    for line in customerCsvFile:
        if line[5] == '':
            line[5] = 'NONE'
        print(line)
        eachLineList.append(line)

# Inserting the queries into the sql file
for line in eachLineList[1:]:
    print(line)
    
    value = "INSERT INTO Customers VALUES("+line[0].strip() + ',' + '"' + line[1].strip() + '"' + ',' + line[2].strip() + ',' + line[3].strip() + ',' + line[4].strip() + ','  + '"' + line[5].strip() + '"' + ','  + line[6].strip() + ','  + line[7].strip() + ");\n" 
    print(value)
    queryInserter.write(value)
    
csvFile.close()
queryInserter.close()

"""
csvReader = open('Customers.csv')
queryInserter = open('insert.sql', 'w+')
lines = csvReader.readlines()
eachLineList = []
for line in lines[1:]:
    eachLineList.append([line])
    print(eachLineList)
    s= "INSERT INTO CUSTOMERS VALUES("+line.strip()+");\n"
    queryInserter.write(s)
csvReader.close()
queryInserter.close()
"""