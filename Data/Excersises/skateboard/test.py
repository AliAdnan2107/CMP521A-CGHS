import matplotlib.pyplot as plt
import csv

path = "skateboard_data.csv"
file = open(path, newline="")
reader = csv.reader(file, delimiter=",")
header = next(reader)
data = [row for row in reader]

# Assuming the genre data is in the 5th column
genres = [row[5] for row in data]

# Counting the occurrences of each genre
genre_counts = {}
for genre in genres:
    if genre in genre_counts:
        genre_counts[genre] += 1
    else:
        genre_counts[genre] = 1

# Creating the pie chart
plt.pie(genre_counts.values(), labels=genre_counts.keys(), autopct='%1.1f%%')
plt.show()