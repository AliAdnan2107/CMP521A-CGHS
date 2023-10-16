#CMP521A
#October 26th 2018
#To show how built in functions for lists work.
#This program will demonstrate how print row by row in a 2D list.


#Variables---------------------------------------------
dataList=[]  #Creates a list

#-----------------------------------------------------------

#MAIN PROGRAM----------------------------------
#NOTE:  In order to create a table  we must use a list of lists
dataList=[
				['Name','Age'],
				['Mr. MacDougald','43'],
				['Mr. Cole','65']
	   ]

print(dataList)  #NOTE: It will look like one row

dataList.append(['Mr.MacAdam','34'])  #Inserts a new row

dataList[0].append('Favorite Team') #adds a new column
dataList[1].append('Oilers') 
dataList[2].append('Maple Leafs')
dataList[3].append('Bruins')

print(dataList)  #NOTE: It still looks like one row

i=0
for i in range(len(dataList)):
	print(dataList[i])
