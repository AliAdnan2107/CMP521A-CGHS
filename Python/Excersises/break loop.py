#Created By Ali Adnan


#Variables------

import time
grade = ""
continue1 = ""

#Code-----------

grade = int(input("What is your grade? \n"))

if grade>50 and grade<=100:
    print ("Congratulations You Passed! :)")
elif grade <50 and grade >=0:
    print ("Sorry you failed. :(")
else:
    print ("Possible Missinput.")

time.sleep (1)
while grade >0 and grade <100:
    continue1 = input ("Do You Wish to Continue? y / n \n")
    grade = int(input("What is your grade? \n"))
    if continue1== "n" and "N":
        print ("Thank you for using my program!")
        break

        
