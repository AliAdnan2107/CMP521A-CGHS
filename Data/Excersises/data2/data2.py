import matplotlib.pyplot as plt 
import csv
x=[]
y=[]
a=0
i=0

data=[]
path="gray.csv"
file = open(path,newline="")
reader=csv.reader(file)

header=next(reader)
data=[row for row in reader]

for a in range(len(data)):
    col1=data[a][0]
    col2=data[a][1]
    x.append(int(col1))
    y.append(int(col2))


for i in range(len(x)):
    print (x[i],y[i])

plt.bar(x,y)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title("Colonel Gray Population")
plt.show()
