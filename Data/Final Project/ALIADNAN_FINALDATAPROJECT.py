#Created By Ali Adnan
#CMP521A
#January 19th 2024
#Final Data Project that will sort through a spotify most listened songs .csv


'''
TODO-
COMPLETE!
'''

#Libraries
import matplotlib.pyplot as plt
import locale
import csv
import random
#Variables
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
        if indexinp is 1: #Track Name 
            track_name = input("Please enter the name of your Track (SOME CHARACTERS ARENT RECOGNIZED) : ").lower()
            print("")
            print (', '.join(header1)) #Print Header
            for row in data:
                if row[0].lower() == track_name: #If data is found, print data.
                    print(', '.join(row[:6]))
        elif indexinp is 2: #Artist Name
            artist_name = input("Please enter the name of the Artist (SOME CHARACTERS ARENT RECOGNIZED) : ").lower()
            print("")
            print (', '.join(header1)) #Print Header
            for row in data:
                if artist_name in row[1].lower(): #If data is found, print data.
                    print(', '.join(row[:6]))
        elif indexinp is 3: #Released Year
            released_year = int(input("Please enter the released year: "))
            print("")
            print (', '.join(header1)) #Print Header
            for row in data:
                if int(row[3]) == released_year: #if Year is found, print data.
                    print(', '.join(row[:6]))
        else:
            print("")
            print ("Invalid Entry, Try again")

#Sorting-------------------
    elif userinp is 2:
        print ("What data would you like to sort")
        print (" 1 - Track Name")
        print (" 2 - Artist Name")
        print (" 3 - Released Year")
        sortinp=int(input("Please pick a sorting option : "))
        if sortinp == 1: #Track Name
            sortinp2=int(input("Alphabetical Order (1) or Reversed Alphabetical Order (2) : ")) #Pick order
            if sortinp2 is 1: #If Alphabetical
                sorted_data = sorted(data[1:], key=lambda x: x[0], reverse=False)  # Sort Track Name
                for row in sorted_data:
                    print (row)
                    sorted_track_names.append(row[0])
                    print ("")
                print ("All data sorted into a list.")
            elif sortinp2 is 2:  #If Reversed Alphabetical
                sorted_data = sorted(data[1:], key=lambda x: x[0], reverse=True)  # Sort Track Name Reversed
                for row in sorted_data:
                    print (row)
                    sorted_track_names.append(row[0])
                    print ("")
                print ("All data sorted into a list.")
        elif sortinp == 2: #Artist Name
            sortinp2=int(input("Alphabetical Order (1) or Reversed Alphabetical Order (2) : "))
            if sortinp2 is 1: #If Alphabetical
                sorted_data = sorted(data[1:], key=lambda x: x[1], reverse=False)  # Sort Track Name
                for row in sorted_data:
                    print (row)
                    sorted_artist_names.append(row[0])
                    print ("")
                print ("All data sorted into a list.")
            elif sortinp2 is 2: #If Reversed Alphabetical
                sorted_data = sorted(data[1:], key=lambda x: x[1], reverse=True)  # Sort Track Name Reversed
                for row in sorted_data:
                    print (row)
                    sorted_artist_names.append(row[0])
                    print ("")
                print ("All data sorted into a list.")
        elif sortinp == 3: #Released Year
            sortinp2=int(input("Least to Greatest (1) or Greatest to least? (2) : "))
            if sortinp2 is 1: #If Least To Greatest
                sorted_data = sorted(data[1:], key=lambda x: (int(x[3]), int(x[4])), reverse=True)  # Sort Released Year
                for row in sorted_data:
                    print(row)
                    sorted_released_years.append(row[3])
                    print ("")
                print ("All data sorted into a list.")
            elif sortinp2 is 2: #If Greatest To Least
                sorted_data = sorted(data[1:], key=lambda x: (int(x[3]), int(x[4])), reverse=False)  # Sort Released Year Reversed
                for row in sorted_data:
                    print(row)
                    sorted_released_years.append(row[3])
                    print ("")
                print ("All data sorted into a list.")
        else:
            print("Invalid Entry, Please try again.")


#Graphing--------------------------------------
    elif userinp is 3:
        print("What data would you like to graph? (MUST SORT FIRST, IF NOT SORTED TYPE 4)")
        print(" 1 - 10 Random Songs vs Released Year")
        print(" 2 - 10 Random Artists vs Highest Streamed Song")
        print(" 3 - Released Year vs Artist Count")
        graphinp = int(input("Please pick a graphing option : "))  
        if graphinp == 1: #10 Random songs Vs Released Year
            num_tracks = len(sorted_track_names)
            random_indices = random.sample(range(num_tracks), 10) #Pick 10 Random
            plt.figure(figsize=(10, 6))
            for i in random_indices:
                x_value = i + 1
                y_value = sorted_released_years[i]
                plt.scatter(x_value, y_value, label=sorted_track_names[i]) #Scatter over plot
            plt.xlabel('Track')
            plt.ylabel('Released Year')
            plt.title('Randomly Selected 10 Tracks vs Released Year')
            plt.legend()
            plt.show()
        elif graphinp == 2: #10 Random Artists vs Highest Streamed Songs
            random_artists = random.sample(sorted_data, 10) #10 Random
            max_streams = max(int(row[8]) for row in sorted_data[:10]) #Find Highest Streams
            step_size = max_streams // 10 if max_streams % 10 == 0 else max_streams // 10 + 1
            y_ticks = [locale.format_string("%d", i, grouping=True) for i in range(0, max_streams + 1, step_size)]
            plt.figure(figsize=(10, 6))
            plt.bar([row[1] for row in random_artists], [int(row[8]) for row in random_artists])
            plt.xlabel('Artist Name')
            plt.ylabel('Streams')
            plt.title('10 Random Artists vs Highest Streamed Song')
            plt.xticks(rotation=45)
            locale.setlocale(locale.LC_ALL, '')
            plt.yticks(range(0, max_streams + 1, step_size), y_ticks)  # Adjust the range and step based on your data
            plt.show()
        elif graphinp is 3: #Released Year vs Artist Count
            plt.figure(figsize=(10, 6))
            plt.plot([int(row[3]) for row in sorted_data], [int(row[2]) for row in sorted_data]) #Plot sorted data
            plt.xlabel('Released Year')
            plt.ylabel('Artist Count')
            plt.title('Released Year vs Artist Count')
            plt.xticks(rotation=45)
            plt.show()
    
        else:
            print("Invalid Entry, Please try again.")


#Quit and Failsafe-------------------------------
    elif userinp is 4:
        print ("Thank you for using my program!")
        break
    else:
        print("Invalid Entry, Try again")