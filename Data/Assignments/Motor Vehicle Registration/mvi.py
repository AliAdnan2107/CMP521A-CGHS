#Created By Ali Adnan
#CMP521A
#January 17th 2024
#This program will take the vehicles registration and create a pie chart of the percentages of vehicles.

#Variables & Libraries
import csv
import matplotlib.pyplot as plt
check=True
AttributeList = []
YearList = []
ValueList = []
PopList = []
CarList = []
TrailerList = []
MotorcycleList = []
TruckList = []
TotalList = []


#Code
path="Motor Vehicle Registration.csv" #Read and open file
file = open(path, newline='')
reader=csv.reader(file)
header=next(reader)
data=[row for row in reader]

for a in range(len(data)):  #Convert all data from .csv and throw into a list
    Year=data[a][0]
    Attribute=data[a][1]
    Value=data[a][2]
    YearList.append((Year))  #Sort all into their own lists
    AttributeList.append((Attribute))
    ValueList.append(int(Value))

print("")
while check==True:
    choice = int(input("Please enter a year to index : "))  #Ask user to index a year
    print('')
    if choice > 2017:
        print("Index Out Of range, Please try again")
    elif choice < 1918:
        print("Index Out Of range, Please try again")
    else:
        break

choice2 = choice + 1  #Add one to the choice to get the range

YearChoice = str(f"{choice}-{choice2}") 
print('')
print("Years you picked")
print(YearChoice)

for i in range(len(YearList)):  #Main Loop of sorting

    if YearList[i] == YearChoice: 

        if AttributeList[i] == "Population": #Population Sorting
            PopList.append(YearList[i])
            PopList.append(AttributeList[i])
            PopList.append(ValueList[i])
            print('')
            print(f"In the years", choice, "-", choice2, "the population was") 
            print(PopList[2])

        if AttributeList[i] == "Cars":  #Car Sorting
            CarList.append(YearList[i])
            CarList.append(AttributeList[i])
            CarList.append(ValueList[i])

            TotalList.append(ValueList[i]) 
            print('')
            print(f"In the years", choice, "-", choice2, "there were") 
            print(CarList[2], "Cars")

        if AttributeList[i] == "Trucks": #Truck Sorting
            TruckList.append(YearList[i])
            TruckList.append(AttributeList[i])
            TruckList.append(ValueList[i])

            TotalList.append(ValueList[i]) 

            print('')
            print(f"In the years", choice, "-", choice2, "there were") 
            print(TruckList[2], "Trucks")

        if AttributeList[i] == "Trailers":  #Trailer Sorting
            TrailerList.append(YearList[i])
            TrailerList.append(AttributeList[i])
            TrailerList.append(ValueList[i])

            TotalList.append(ValueList[i])

            print('')
            print(f"In the years", choice, "-", choice2, "there were") 
            print(TrailerList[2], "Trailers")

        if AttributeList[i] == "Motorcycles": #Motorcycle Sorting
            MotorcycleList.append(YearList[i])
            MotorcycleList.append(AttributeList[i])
            MotorcycleList.append(ValueList[i])

            TotalList.append(ValueList[i]) 

            print('')
            print(f"In the years", choice, "-", choice2, "there were") 
            print(MotorcycleList[2],"Motorcycles") 



if len(TotalList) == 4: #Post 2000 (Trailer Era)
    Vehicles1 = ["Cars", "Trucks", "Trailers", "Motorcycles"]
    plt.pie(TotalList, labels=Vehicles1, autopct='%1.1f%%')  #Create Pie Chart
    plt.title('Motor Vehicle Registration Index')
    plt.show()
else: #Pre 2000 (No Trailer Era)
    Vehicles2 = ["Cars", "Trucks", "Motorcycles"]
    plt.pie(TotalList, labels=Vehicles2, autopct='%1.1f%%')  #Create Pie Chart
    plt.title('Motor Vehicle Registration Index')
    plt.show()