#Created By Ali Adnan
#CMP521A
#September 13th 2023
#This Program will ask a user their age along with their town, and see if they are islanders. or 19-21 Years Old


#Variables
age= int(input("How Old Are You? \n"))
location= input("Where do you live? \n")

#Code

if age>18 and age<22:
    print ("Great! You're not Very Old.")
else:
    print ("Thats Too bad.")

if location=="Charlottetown" or location=="Summerside":
    print ("Great! You're an Islander.")
else:
    print ("That's Too bad.")