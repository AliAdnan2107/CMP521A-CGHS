#Created By Ali Adnan
#CMP521A
#January 12th 2024
#This Program will take the Seafood .csv file and format, graph and display at as per user's choice.

#Variables & Libraries

import matplotlib.pyplot as plt
import csv
import time

yearlist = [] #List Of Years
loblist = [] #Licensed Lobsters
groundlist = [] #Licensed Groundfish

#Code

path="Seafoodbuying2009.csv" 
file=open(path, newline="") #Open .csv and read / import data
reader=csv.reader(file)
header=next(reader)
data=[row for row in reader]

for a in range (len(data)): #Create lists based of .csv
    year = data[a][0]
    type = data[a][2]
    num = data[a][3]

    yearlist.append(int(year))
    if type == "Lobster":
        loblist.append(int(num))
    if type == "Groundfish":
        groundlist.append(int(num))

yearlist = list(set(yearlist))   #Sort Year list
yearlist.sort()

print("Number of years")
print(yearlist)
print("Number of Lobsters Licensed")
print(loblist)
print("Number of Groundfish Licensed")
print(groundlist)

#Plot Licensed Lobster and Groundlist vs Years.
plt.plot(yearlist, loblist, color = "r", label = "Lobsters")
plt.plot(yearlist, groundlist, color = "b", label = "Groundfish")
plt.title("Number of Licensed\nFish Vs Years")
plt.legend()
plt.show()