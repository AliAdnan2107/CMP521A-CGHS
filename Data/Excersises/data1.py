import matplotlib.pyplot as plt 

x=[1,2,3]
y=[3,2,1]
x2=[2,4,6]
y2=[6,4,2]
plt.scatter(x,y, label="This bar means something.", color="r", s=100, marker="D")
plt.scatter(x2,y2, Label="This bar also means something", color="b", s=100, marker="D")
plt.xlabel("idk what to type here")
plt.ylabel("send help!")
plt.title ("i love comp sci (optional)")
plt.legend()
plt.show()

'''
populationages=[22,44,11,13,15,17,21,42,85,93,13,53,16]

ids = [x for x in range (len(populationages))]

plt.bar(ids, populationages, color="rgb", label="Population")

plt.xlabel ("Average")
plt.ylabel ("Ages")
plt.title ("Average Population Age")
plt.legend()
plt.show()
'''