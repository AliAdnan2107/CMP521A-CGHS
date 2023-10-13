#Created by Ali Adnan
#CMP521A


#Variables

numlist=[]
check=True
numinp=0

#Code

def NumTimes(numlist):
    result = {}
    for i in range(1, 11):
        count = numlist.count(i)
        result[i] = count
    return result

while check==True:
    numinp=input ("Please Enter a number to add to your list or type Done to exit \n")
    if numinp=="Done":
        print(numlist)
        print("")
        result = NumTimes(numlist)
        print("The Amount of times you inputed a number are as follows")
        for i in range(1, 11):
            print(f"{i} was entered {result[i]} times")
        break
    else:
        numlist.append(int(numinp))
        print(numlist)
        print("")