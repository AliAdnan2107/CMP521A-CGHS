from re import X
from tokenize import Name


fname = input("First Name: ")
lname = input("Last Name: ")
intials = input("Initials: ")
spacer="_"

fname2 = input("First Name: ")

y=2
z=2
a="1"
b="1"
x=40

print ("Please Welcome " + fname, lname +" To The Computer Studies CMP521A Class!")
print (" ")
print (fname, ", Can you Answer the Following Question?")
print (" ")
print ("I'll Try!")
print (" ")
print ("What is 1+1")
print ("I think its", int(a)+int(b))
print ("Great Job! Mr.", lname)

print (spacer*X)
print (" ")
print ("How about you", fname2, "?")
print (" ")
print ("What's 2+2")
print ("I think its", str(y)+str(z) )
print ("You're Almost There!")