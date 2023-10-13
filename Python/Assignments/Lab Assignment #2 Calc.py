#Created By Ali Adnan
#CMP521A
#September 25th 2023
#This program will calculate sphere's S.A & Pick a random number aswell

#Variables & Import
calc = True
import math
import random
pi = math.pi
r=0
num1=int(0)
num2=int(0)

#Code

def calc_sur(r): #Calculates the surface area of a sphere when the radius is provided.
    if r.isdigit():
        print ("The surface area of the sphere is", 4*pi*float(r)**2)
        print ("")
    else:
        print ("Invalid Entry.")

def Rand_Num(num1,num2): #Takes two numbers picked by user then picks a random number in between them.
    if num1.isdigit() and num2.isdigit():
        if int(num1)<int(num2):
            print ("A Random Number Between", num1, "And", num2, "Is")
            print (random.randrange(int(num1),int(num2)+1))
            print ("")
        elif int(num2)<int(num1):
            print ("A Random Number Between", num1, "And", num2, "Is")
            print (random.randrange(int(num2),int(num1)+1))
            print ("")
    else:
        print ("Invalid Entry")

print ("Welcome to my program")
while calc == True: #The Main Loop of the program
    print ("Plese pick a number from 1 - 3")
    print ("1 - Function Mini Program (S.A Of Sphere)")
    print ("2 - Random Mini Program (Random Range Choice)")
    print ("3 - Quit")
    menucheck = input ("What's your Pick? \n")

    if menucheck.isdigit():
        if int(menucheck) == 1:
             r=input("Please enter the radius of a circle \n")
             calc_sur(r)
        if int(menucheck) == 2:
            num1=input ("Please Enter your starting number \n")
            print ("")
            num2=input ("Please Enter your ending number \n")
            Rand_Num(num1,num2)
        if int (menucheck) == 3:
            print ("Thank you for using my program")
            break
        if int (menucheck) >=4 or int(menucheck) <=0: #If num not 1-3 , print following
            print ("Invalid Choice")
            print ("")
    else: #If not num, print following
        print ("Invalid Choice, Pick a number from 1-3 ")
        print ("")
