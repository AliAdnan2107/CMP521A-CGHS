#Created By Ali Adnan
#CMP521A
#January 19th 2024
#Final Data Project that will sort through a spotify most listened songs .csv


'''
TODO-
fix sorting/graphing to actually make sense
'''

#Variables & Libaries

import matplotlib.pyplot as plt
import csv
import time

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
print ("Welcome to my data sorting program")
print ("This program will sort through a 'Most listened to songs on Spotify' List")
while True:
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
            track_name = input("Please enter the name of your Track (SOME CHARACTERS ARENT RECOGNIZED): ")
            for row in data:
                if row[0] == track_name:
                    print(row)
                    
        elif indexinp is 2:
            print("")
            print ("Artist Name (TBC)")
        elif indexinp is 3:
            print("")
            print ("Released Year (TBC")
        else:
            print("")
            print ("Invalid Entry, Try again")

#Sorting
    elif userinp is 2:
        print ("How would you like to sort your data?")
        print (" 1 - By Track Name")
        print (" 2 - By Artist Name")
        print (" 3 - By Released Year")
        sortinp=int(input("Please pick a sorting option : "))
        if sortinp is 1:
            print ("Track Name (TBC)")
        elif sortinp is 2:
            print ("Artist Name (TBC)")
        elif sortinp is 3:
            print ("Released Year (TBC)")
        else:
            print ("Invalid Entry, Please try again.")

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
