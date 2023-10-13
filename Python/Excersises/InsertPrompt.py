#Created By Ali Adnan
#CMP521A


#Variables

dalist=["element1","element2","element3","element4","element5","element6","element7","element8"]
where=""
what=""
#Code

print (dalist)
what=input("What would you like to add? \n")
where=int(input("Where would you like to add this? Please pick a number \n"))
dalist.insert(int(where),what)
print (dalist)