#Created By Ali Adnan
#CMP521A


#Variables

listofnames=[]
check=True
i=""

#Code

while check==True:
   i=input ("Please enter a name or type done. \n") 
   if i.lower()== "done":
       print (listofnames)
       print("")
       break
   else:
       print("")
       listofnames.append(i)
       print (listofnames)
