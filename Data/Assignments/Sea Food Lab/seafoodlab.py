#Created By Ali Adnan
#CMP521A
#January 12th 2024
#This Program will take the Seafood .csv file and format, graph and display at as per user's choice.

#Variables & Libraries

import matplotlib.pyplot as plt
import csv

check=True
data=[]
x=[]
y=[]
x1=[]
y1=[]
a=0
i=0
path="Seafoodbuying2009.csv"

#Code

file=open(path, newline="")
reader=csv.reader(file)
header=next(reader)
data=[row for row in reader]

for a in range (len(data)):
    col1=data[a][0]
    col2=data[a][1]
    col3=data[a][2]
    col4=data[a][3]
    x.append(col1)
    y.append(col2)
    x1.append(col3)
    y1.append(col4)

for i in range (len(x)):
    print (x[i],y[i])

print("Welcome, This program is sorting the 'SeafoodBuying2009.csv' File.")
while check==True:

    print("Please pick a menu option")
    print(" 1 - Display all data")
    print(" 2 - Format Data")
    print(" 3 - Select Data & Graph")
    print(" 4 - Quit")
    inp=input("Please select a menu option : ")

    if inp=="1":
        print("")
        print("Here is the whole set of data (Unsorted)")
        print(data)
    if inp=="2":
        print("")
        print("Here is your formatted data")
        for i in range (len(x)):
         print (x[i],y[i],x1[i],y1[i])
    if inp=="3":
        print("")
        rowinp=int(input("Please type in the row number for the first seafood : "))
        rowinp1=int(input("Please type in the row number for the second seafood : "))
        print ("")
        print (data[rowinp])
        print (data[rowinp1])
        label=(data[rowinp][0])
        label2=(data[rowinp][3])
        label3=(data[rowinp1][0])
        label4=(data[rowinp1][3])
        print ("")
        print("")
        plt.plot(label,label2)
        plt.plot(label3,label4)
        plt.xlabel("Year")
        plt.ylabel("Number of Licenses")
        plt.title("Sea Food Buying List")
        plt.show()
    if inp=="4":
        exit()
        

        