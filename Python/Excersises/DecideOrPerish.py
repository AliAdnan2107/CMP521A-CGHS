#Test Code for Cross-Device Coding, Created by Ali Adnan
#"Decide Or Perish"
#CMP521A
#September 13th 2023
#This Is just a scrap .py file. and an attempt at a game of decisions.

#Variables

#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------

playername=input("What's your name? \n")
import time

#Code

print ("You wake up in a unfamiliar looking area, What do you do first",playername, "?")
time.sleep(3)
print ("A - Go back to sleep")
time.sleep(1)
print ("B - Try to discover the area.")
time.sleep(1)
print ("C - Panic.")
time.sleep(2)
decision1=input ("What's your decision? A, B or C \n")

if decision1=="A" and "C" or "a" and "c":
    print("You Lost! Thank you for playing", playername, ". :)")
    time.sleep(1)
    exit()
else:
    print ("")

if decision1=="B" and "b":
    print ("Correct! Doing Well so far", playername ,".")
time.sleep(3)
print ("As you proceed around the area, you end up in a pathway that leads to a left or a right.")
time.sleep(2)
print ("Left is dimmer and Right has a very bright light source")
time.sleep(2)
decision2=input ("What's Path do you take? Left or Right. \n")

if decision2=="Right" and "right":
    print("You Lost! Thank you for playing", playername, ". :)")
    time.sleep(1)
    exit()
else:
    print ("")

if decision2=="Left" and "left":
    print ("Correct! This also shows that looks can be decieving.")
    print ("End of game for now, Will be updated once learn more functions, Thanks for playing!", playername, ". :)")
    exit()