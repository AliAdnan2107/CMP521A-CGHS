import matplotlib.pyplot as plt
import csv

path="skateboard_data.csv"
file=open(path, newline="")
reader=csv.reader(file, delimiter=",")
header=next(reader)
data=[row for row in reader]

for a in range (len(data)):
    genre=data[a][5]


plt.pie(genre)
plt.show()
