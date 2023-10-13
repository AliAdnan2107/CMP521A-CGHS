#Created By Ali Adnan
#CMP521A


#Variables

list=["volleyball", "cross country", "basketball", "hockey", "soccer", "football"]
check=True
copy_list1=list.copy()
copy_list2=list.copy()
choice=0
inplist=""
inplistdel=""

#Libraries

import time

#Code


print ("Welcome to my program.")
print ("")
time.sleep(1)
print("CURRENT LISTS ARE AS FOLLOWS")
print ("Original ")
print (list)
time.sleep(1)
print ("")
print("Copy")
print (copy_list1)
print("")
time.sleep(1)
while check==True:
    print ("Please pick the following menu options")
    print ("1- Add to original List")
    print ("2- Remove an element from original")
    print ("3- Copy the sportlist")
    print ("4- Display Lists")
    choice=int(input ("Please pick a number from 1-4 \n"))
    if choice==1:
        inplist=input ("Please enter what you would like to add to the original list \n")
        list.append(inplist)
        print ("Your New List is")
        print (list)
        print("")
    if choice==2:
        inplistdel=int(input ("Please enter the EXACT positioning of what you want to remove from the list \n"))
        if inplistdel>len(list):
            print ("Number is more than the length of list")
        elif inplistdel == 0:
            del list[inplistdel]
            print (list)
        elif inplistdel<len(list):
            print ("Number is less than the length of the list")
        else:
            del list[inplistdel]
            print (list)
    if choice==3:
        copy_list1=list.copy()
        print("The New Copied List is")
        print (copy_list1)
    if choice==4:
        print ("The Modified List is")
        print(list)
        print ("The Copied List is")
        print(copy_list1)
        print ("The Original List is")
        print (copy_list2)
    if choice==5:
        exit("Thank you for using my program!")
    if choice>=6:
        print ("sir. 1-4")
    if choice<=0:
        print ("why are you like this?")

