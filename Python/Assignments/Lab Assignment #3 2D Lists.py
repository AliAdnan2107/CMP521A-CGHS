#Created By Ali Adnan
#CMP521A
#October 18th 2023
#This Program will adjust a 2D List


#Variables

mainlist=[
    ["Name","Age","Job","Interest"],
    ["Agam","16","Unemployed","Soccer"],
    ["Ali","16","Bingo Worker","Computers"],
    ["Min","16","Unemployed","Math"],
    ["Alan","16","Tech Support","Computers"],
    ["Alex","16","Unknown","Volleyball"],
    ["Noah","16","Unemployed","Computers"],
    ["Jayden","16","Unemployed","Education"]
]

check=True
choice=0
rowappend=""
columnappend=""

#Libraries



#Code

print ("Welcome to my program!")
while check==True:
    print ("Please Pick an option")
    print ("1 - Add A Row Of Data")
    print ("2- Add A Column Of Data")
    print ("3- Print A Specific Data Point")
    print ("4- Print The Entire List")
    print ("5- Quit")
    choice=int(input("What is your pick? : "))
    if choice == 1:
        rowappend=input("What would you like to add to your row of data? \n")
        mainlist.append(rowappend)
    elif choice ==2:
        columnappend=input("What would you like to add to your column of data? \n")
        




