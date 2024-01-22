#Created By Ali Adnan
#CMP521A
#January 19th 2024
#Final Data Project that will sort through a spotify most listened songs .csv


'''
TODO-
let graphing work
'''

#Variables & Libaries

import matplotlib.pyplot as plt
import csv
import time
header1=["Track Name","Artist Name","Artist Count","Released Year","Released Month","Released Day"]
sorted_track_names = []
sorted_artist_names = []
sorted_released_years = []

#Code

#Initializing------
path="spotify-2023.csv" #Read and open file
file = open(path, newline='')
reader=csv.reader(file)
header=next(reader)
data=[row for row in reader]

for a in range(len(data)):  #Convert all data from .csv and throw into a list
    TrackName=data[a][0]
    ArtistName=data[a][1]
    ArtistCount=data[a][2]
    ReleasedYear=data[a][3]
    ReleasedMonth=data[a][4]
    ReleasedDay=data[a][5]
    InSpotifyPlaylists=data[a][6]
    InSpotifyCharts=data[a][7]
    SpotifyStreams=data[a][8]
    InApplePlaylists=data[a][9]
    InAppleCharts=data[a][10]
    InDeezerPlaylists=data[a][11]
    InDeezerCharts=data[a][12]
    InShazamCharts=data[a][13]



#Menu---------
print ("")
print ("Welcome to my data sorting program")
print ("This program will sort through a 'Most listened to songs on Spotify' List")
while True:
    print("")
    print ("Menu")
    print(" 1 - Search Data ")
    print(" 2 - Sort Data ")
    print(" 3 - Graph Data ")
    print(" 4 - Quit ")
    userinp=int(input("Please Pick a Menu option : "))

#Searching-----
    if userinp is 1:
        print ("How would you prefer to index?")
        print (" 1 - By Track Name")
        print (" 2 - By Artist Name")
        print (" 3 - By Released Year")
        indexinp=int(input("Please pick a indexing option : "))
        if indexinp is 1:
            track_name = input("Please enter the name of your Track (SOME CHARACTERS ARENT RECOGNIZED) : ").lower()
            print("")
            print (', '.join(header1))
            for row in data:
                if row[0].lower() == track_name:
                    print(', '.join(row[:6]))
        elif indexinp is 2:
            artist_name = input("Please enter the name of the Artist (SOME CHARACTERS ARENT RECOGNIZED) : ").lower()
            print("")
            print (', '.join(header1))
            for row in data:
                if artist_name in row[1].lower():
                    print(', '.join(row[:6]))
        elif indexinp is 3:
            released_year = int(input("Please enter the released year: "))
            print("")
            print (', '.join(header1))
            for row in data:
                if int(row[3]) == released_year:
                    print(', '.join(row[:6]))
        else:
            print("")
            print ("Invalid Entry, Try again")

#Sorting
    elif userinp is 2:
        print ("How would you like to sort your data? (Alphabetical / Numerical Order)")
        print (" 1 - By Track Name")
        print (" 2 - By Artist Name")
        print (" 3 - By Released Year")
        sortinp=int(input("Please pick a sorting option : "))
        if sortinp == 1:
            sorted_data = sorted(data[1:], key=lambda x: x[0])  # Sort by Track Name
            for row in sorted_data:
                print (row)
                sorted_track_names.append(row[0])
                print ("")
            print ("All data sorted into a list.")
        elif sortinp == 2:
            sorted_data = sorted(data[1:], key=lambda x: x[1])  # Sort by Artist Name
            for row in sorted_data:
                print(row)
                sorted_artist_names.append(row[0])
                print ("")
            print ("All data sorted into a list.")
        elif sortinp == 3:
            sorted_data = sorted(data[1:], key=lambda x: (int(x[3]), int(x[4])))  # Sort by Released Year
            for row in sorted_data:
                print(row)
                sorted_released_years.append(row[0])
                print ("")
            print ("All data sorted into a list.")
        else:
            print("Invalid Entry, Please try again.")

#Graphing
    elif userinp is 3:
        print ("What data would you like to graph?")
        print (" 1 - Track Name")
        print (" 2 - Artist Name")
        print (" 3 - Released Year")
        graphinp=int(input("Please pick a graphing option : "))
        if graphinp is 1:
            print ("Track Name (TBC)")
        elif graphinp is 2:
            print ("Artist Name (TBC)")
        elif graphinp is 3:
            print ("Released Year (TBC)")
        else:
            print ("Invalid Entry, Please try again.")

#Quit and Failsafe
    elif userinp is 4:
        print ("Thank you for using my program!")
        break
    else:
        print("Invalid Entry, Try again")