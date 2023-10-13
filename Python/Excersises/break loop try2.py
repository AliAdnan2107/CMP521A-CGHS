#Created By Ali Adnan
#Attempt 2

#Variables And Imports

import time
grade = ""
continue1 = "Y"


#Code

while continue1 == "Y" and "y":
    grade= int (input("What is your grade? \n"))
    if grade>=0 and grade<=49:
        print ("Sorry you failed :(")
    if grade>=50 and grade<=100:
        print ("Congratulations You Passed! :)")
    time.sleep (1)
    continue1= input ("Do You wish to continue? y/n \n")
    if continue1 == "n" and "N":
        print ("Thank you for using my program!")
        break
exit()