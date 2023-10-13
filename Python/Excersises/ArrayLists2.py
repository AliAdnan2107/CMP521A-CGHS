#Created by ALi Adnan
#CMP521A


#Variables

list=["Nissan","Toyota","Honda","Hyundai","Kia"]
check=True
choice=""

#Code

while check==True:
    print (list)
    choice=input("Please add another make of cars into the list or type done \n")
    if choice.lower()=="done":
       print(list)
       break
    else:
        list.append(choice)
        print(list)
        print("")
