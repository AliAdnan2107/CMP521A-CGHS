#CMP 521A Python Programming Test #2
#PINK SHEET TEST
#NAME: ALI ADNAN

choice=0
check= True

while check==True: #Mainloop
        
        print('1.  Numbers list')
        print('2.  2D list')
        print('3.  Number list')
        print('4.  Quit')

        choice=int(input('Enter your choice.\n'))


        if choice==1:
#All variables and work for choice 1 is show here-----------------
                words="Cat#Dog#Chair#Table#TV#Computer" #Main String that gets split into a list
                splitwords=words.split('#') #List of split words
                wordcount=(len(splitwords))
                print (splitwords)
                print (f"There are {wordcount} Words in the list")
                wordindex=input ("What is the word you wish to index? (Case Sensitive) : ") #Input to index a specific word
                indexedpos=splitwords.index(wordindex)
                print (f"{wordindex} is Located at {indexedpos}")
                print (f"The list without the word {wordindex} is")
                removedword=splitwords.copy() #Makes a copy to reset the data every rerun
                del removedword[indexedpos] #Deletes the specific indexed word
                print (removedword)


#End of work for choice 1-----------------------------------------
        
        if choice==2:
#Begin of work/variables for choice 2 -----------------------------                
                carlist=[  #Car List
                        ['Manufacturer','Year','Model'],
                        ['Ford','1978','Mustang'],
                        ['Dodge','2001','Charger'],
                        ['Honda','1999','Civic']
                ]

                carlistcopy=carlist.copy() #Makes a copy to reset the data every rerun

                for x in range (len(carlist)): #Prints every row individually
                        print (carlist[x])
                for i in range (len(carlist)):
                        coladd=input("Please enter the element of the new column \n") #Add's column's for each row
                        carlistcopy[i].append(coladd)
                for y in range (len(carlistcopy)): #Prints every row individually
                        print (carlistcopy[y])


#End of work for choice 2------------------------------------------
        
        if choice==3:
#Begin of work/variables for choice 3 -----------------------------                
                print ("CODE DOESN'T FULLY RUN, CHECK COMMENT'S FOR DETAILS")
                '''
                numberlist=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
                print (numberlist)
                numindexes=int(input("Enter the number you would like to index \n"))
                indexednums=numberlist.index(numindexes) #Only prints first Index rather than all index
                print (indexednums) 
                numlistcopy=numberlist.copy()
                print (numlistcopy)
                for a in range(len(numlistcopy)):
                        squarednum=(numlistcopy[a]**2) #Cannot figure out how to square the list individually
                        numlistcopy.clear()
                        numlistcopy.append(squarednum)
                '''


#End of work for choice 3------------------------------------------

        if choice==4:
                break

print('Thank you for using my program.')
