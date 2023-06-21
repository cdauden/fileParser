import csv

readPath=r""
writePath=r""

f=open(writePath,"w")

# Opens and closes file with encoding cp='437' to decode all characters in file
with open(readPath, mode='r', encoding='cp437')as file:
    csvReader=csv.reader(file, delimiter=",")
    for row in csvReader:
        # row[6] is the User Group column
        if row[6]=='Students':
            # row[0] is the Email column
            f.write(row[0]+'\n')
            print(row[0])
f.close()