#Variables
import matplotlib.pyplot as plt 
import csv

#Code

data=[]
x=[]
y=[]
a=0
i=0
path="Collisions_from_1980.csv"
file=open(path,newline="")
reader=csv.reader(file)
header=next(reader)
data=[row for row in reader]


for a in range (len(data)):
    col1=data[a][0]
    col2=data[a][2]
    x.append(int(col1))
    y.append(int(col2))


for i in range (len(x)):
    print (x[i],y[i])

plt.plot(x,y)
plt.xlabel("Year")
plt.ylabel("Number of Injured")
plt.title("Number Of Injured Vs Year")
plt.legend()
plt.show()