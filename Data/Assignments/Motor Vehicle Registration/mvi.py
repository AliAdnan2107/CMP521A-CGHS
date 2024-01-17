#Created By Ali Adnan
#CMP521A
#January 17th 2024
#This program will read through motor vehicle registrations and give user option's based on them.




from inspect import Attribute
import matplotlib.pyplot as plt
#Read Data
import csv
path="Motor Vehicle Registration.csv"
file=open(path, newline="")
#Store Data into a List
reader = csv.reader(file, delimiter=",")
header=next(reader)
data= [row for row in reader]
#Seperate and convert data
yearlist=[]
attributelist=[]
valuelist=[]
for a in range (len(data)):
    year = data[a][0]
    attribute = data[a][1]
    value = data[a][2]
    yearlist.append(year)
    attributelist.append(attribute)
    valuelist.append(value)
#Select Data / Input Data
yearinp=input("Please select a Fiscal year to look for : ")
yearArray=[]
attributeArray=[]
yearArray.append(int(year))
if attribute=="Population":
    attributeArray.append(int(value))
if attribute=="Cars":
    attributeArray.append(int(value))
if attribute=="Trucks":
    attributeArray.append(int(value))
if attribute=="Motorcycles":
    attributeArray.append(int(value))
if attribute=="Total Registrations":
    attributeArray.append(int(value))
        
         

