import pandas as pd

readPath=r"C:\Users\OP7050\Documents\zoomus_users.csv"
writePath=r"C:\Users\OP7050\Documents\studentEmails.txt"

# saves Email and User Group columns to dataframe
df=pd.read_csv(readPath, usecols=['Email','User Group'])

# dataframe to array
array=df[['Email','User Group']].to_numpy()

rows=0
f=open(writePath,"w")

while rows<len(array):
    if(array[rows,1]=='Students'):
        print(array[rows,0])
        f.write(array[rows,0]+"\n")
    rows+=1

f.close()