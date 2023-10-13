#Created By Ali Adnan
#CMP521A
#Variables

MainList=[]
check=True
InputMain=0

#Code

while check==True:
    InputMain=input("Please input a number or type Done : ")
    if InputMain=="Done" or InputMain == "done":
        print ("The Length Was" ,len(MainList))
        print ("The Highest Number is", max(MainList))
        print ("The Lowest Number is" , min(MainList))
        print ("The Sum of The List is" , sum(MainList))
        MainList.sort()
        print ("Your sorted List is" , MainList)
        MainListCopy=MainList
        MainListCopy.reverse()
        print ("Your Reversed List Is" ,MainListCopy)
        break
    else:
        MainList.append(int(InputMain))
        print (MainList)