#Created By Ali Adnan
#CMP521A


#Variables

i=0
datalist=[
    ["Name1","Age1"],
    ["Name2","Age2"],
    ["Name3","Age3"],
    ["Name4","Age4"]
]

#Code

datalist.append(["Name5","Age5"])
datalist.append(["Name6","Age6"])
datalist.append(["Name7","Age7"])
datalist.append(["Name8","Age8"])

datalist[0].append("Citizen1")
datalist[1].append("Citizen2")
datalist[2].append("Citizen3")
datalist[3].append("Citizen4")
datalist[4].append("Citizen5")
datalist[5].append("Citizen6")
datalist[6].append("Citizen7")
datalist[7].append("Citizen8")




for i in range (len(datalist)):
    print (datalist[i])