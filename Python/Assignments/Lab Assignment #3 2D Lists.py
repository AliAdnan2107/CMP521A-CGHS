#Created By Ali Adnan
#CMP521A
#October 18th 2023
#This Program will adjust a 2D List


#Variables

mainlist=[ #The List That Holds All Information
    ["Name","Age","Job","Interest"],
    ["Agam","16","Unemployed","Soccer"],
    ["Ali","16","Bingo Worker","Computers"],
    ["Min","16","Unemployed","Math"],
    ["Alan","16","Tech Support","Computers"],
    ["Alex","16","Unknown","Volleyball"],
    ["Noah","16","Unemployed","Computers"],
    ["Jayden","16","Unemployed","Education"]
]

splitlist=[]
check=True
choice=0
rowappend=""
columnappend=""
rowinp=0
colinp=0
inc=0

#Code

print ("Welcome to my program!")
while check is True: #Main Loop of program
    print ("Please Pick an option")
    print ("1 - Add A Row Of Data")
    print ("2- Add A Column Of Data")
    print ("3- Print A Specific Data Point")
    print ("4- Print The Entire List")
    print ("5- Quit")
    print ("")
    choice=input("What is your pick? : ")
    if choice.isdigit():
        if int(choice) == 1: #Row Of Data Code
            splitlist=input("What would you like to add to your row of data? Make sure your data has a space and comma between information \n")
            rowappend=splitlist.split(", ")
            mainlist.append(rowappend)
        elif int(choice) ==2: #Column Of Data Code
            for i in range (len(mainlist)):
             columnappend=input("What would you like to add to your column of data? This will affect every row \n")
             mainlist[i].append(columnappend)
        elif int(choice) ==3: #Print A Specific Data Point
            rowinp=int(input("Please type in the row number : "))
            colinp=int(input("Please type in the column number : "))
            print ("")
            print (mainlist[rowinp][colinp])
            print ("")
        elif int(choice) ==4: #Print The Entire List
            print ("")
            for x in range (len(mainlist)):
                print (mainlist[x])
            print ("")
        elif int(choice) ==5: #Quit
            print ("Thank you for using my program!")
            break
        else: #Safeguard for any number above or under 1-5
            print ("Number from 1-5 Please.")
            print ("")
    else: #Safeguard for anyone who inputs a string instead of an integer
        print ("Numbers only.")
        print ("")
