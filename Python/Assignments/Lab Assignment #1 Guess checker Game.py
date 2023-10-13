#Created By Ali Adnan
#CMP521A
#September 19th 2023
#This is a Guessing game that will check if the guessed number is corrrect.

#Variables & Imports

import time  #This adds the function to give the code a break between each line

target_number = 6  #The Number to be guessed
guess = False  #Check's if the guess is either correct or not.
loopcheck = 0  #Add's every attempt to break the loop once 5 is reached.
tries = 1  #Shows the user how many tries they have had.

#Code-----

print("Welcome to my Guessing Game!")
time.sleep(1)
print("")
print("Go ahead and guess a number between 1 - 20")
time.sleep(1)
print("")

while guess == False:  #This is the loop of the main game.
  num1 = input("What is your guess? \n ")

  if num1.isdigit():
    if int(num1) == target_number:
      guess = True
      print("Congratulations You Win!!")
      print("")
      print("Completed in", tries, "Attempts")
      break
    elif int(num1) >= 21 or int(num1) == 0:
      print("Number Not from 1-20")
    elif int(num1) >= target_number - 3 and int(num1) <= target_number + 3:
      guess = False
      print("You Are Super Close!")
      print("")
      print("Attempt", tries, "Of 5")
      loopcheck = loopcheck + 1
      tries = tries + 1
    elif int(num1) >= target_number - 6 and int(num1) <= target_number + 6:
      guess = False
      print("Somewhat Close")
      print("")
      print("Attempt", tries, "Of 5")
      loopcheck = loopcheck + 1
      tries = tries + 1
    else:
      guess = False
      print("You Are Way Off!!")
      print("")
      print("Attempt", tries, "Of 5")
      loopcheck = loopcheck + 1
      tries = tries + 1
  else:
    print("Invalid Entry.")
  if loopcheck == 5:
    break

if guess == True:  #If they won, shows a nicer message
  time.sleep(1)
  print("Thank you for playing!")
  exit()
if guess == False:  #If they lost, shows a "less" nicer message
  time.sleep(1)
  print("You lost!, Thank you for playing.")
  exit()


