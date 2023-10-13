#Created By Ali Adnan
#CMP521A


#Variables

rps=["Rock","Paper","Scissors"]
reattempt=""
check=True
playerinp=""

#Libraries

import random

#Code
print ("BEAT THE AIIIIII")

while check==True:
    print ("Pick Rock Paper, Or Scissors.")
    playerinp=input("What is your choice? \n")
    if playerinp.lower()=="rock":
        print ("")
        print ("Computer Picks")
        rpspicks=random.choice(rps)
        print (rpspicks)
        print("")
        if rpspicks=="Paper":
            print ("You Lose!")
        elif rpspicks=="Scissors":
            print("You Win!")
        elif rpspicks=="Rock":
            print ("Tie!")

    elif playerinp.lower()=="paper":
        print ("")
        print ("Computer Picks")
        rpspicks=random.choice(rps)
        print (rpspicks)
        print("")
        if rpspicks=="Paper":
            print ("Tie!")
        elif rpspicks=="Scissors":
            print("You Lose!")
        elif rpspicks=="Rock":
            print ("You Win!")


    elif playerinp.lower()=="scissors":
        print ("")
        print ("Computer Picks")
        rpspicks=random.choice(rps)
        print (rpspicks)
        print("")
        if rpspicks=="Paper":
            print ("You Win!")
        elif rpspicks=="Scissors":
            print("Tie!")
        elif rpspicks=="Rock":
            print ("You Lose!")

    reattempt=input("Would you like to play again? y/n \n")
    if reattempt.lower()=="y":
        check=True
    elif reattempt.lower()=="n":
        check=False
        print ("Thanks for playing!")
        break