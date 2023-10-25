#Programming Test #1
#Name: Ali Adnan
#Date: October 4th 2023

#Variables for loop-----------
check=True
choice=0


#MAIN CODE--------------------
print('Welcome to my program!!')
print("")

while check == True:
    print('1. Username and Password ')
    print('2. Function Speed Converter ')
    print('3. Random Generator ')
    print('4. Quit ')

    choice=(input('Please enter your choice.\n'))

    #Variables for choice #1
    username="cmp"
    password="password"
   
   #Work for choice #1---------------------------
    if int(choice)==1:
        username=input ("Please enter your Username \n")
        password=input ("Please enter your Password \n")
        if username.lower()=="cmp" and password.lower()=="password":
            print ("Your Login Was succesful.")
            print ("")
        else:
            print ("Invalid Username and/or Password")
            print ("")

    #End of work for choice #1---------------------



    #Variables for choice #2  
    speed=0

    #Work for choice #2---------------------------
    def SpeedConv(speed):
        print ("Your speed in km/h is ", speed*3.6)

    
    
    if int(choice)==2:
        speed=input ("Please enter your speed in m/s \n")
        if speed.isdigit():
            SpeedConv (int(speed))
            print ("")
        else:
            print ("Invalid Entry.")
            print ("")

    #End of work for choice #2---------------------


    #Variables for choice #3   
    num1=0
    num2=0
    import random

    #Work for choice #3---------------------------
    if int(choice)==3:
        num1=input("Please pick your first number \n")
        print("")
        num2=input("Please pick your second number. \n")
        print ("")
        if num1.isdigit() and num2.isdigit():
            print ("The 10 random numbers are")
            for i in range(10):
                print (random.randrange(int(num1), (int)(num2)+1))
        else:
            print ("Invalid Entry.")
            print ("")

    #End of work for choice #3---------------------




    #Work for choice #4---------------------------
    if int(choice)==4:
        break
    #End of work for choice #4---------------------

    if int(choice)>4:
        print ("Invalid, Please pick a number from 1 - 3")
        print ("")
        
print ("Thank you for using my Program!")
