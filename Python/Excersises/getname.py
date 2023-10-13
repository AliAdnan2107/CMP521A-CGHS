#Created By Ali Adnan
#CMP521A

#Variables

import time
a=""

#Functions

def GetName():
    a=input("What's Your Name? \n")
    time.sleep(.5)
    print("")
    print (a)

#Code

print ("Welcome to my program!")
time.sleep(1)
GetName()
print ("Thank you for using my program!")