import matplotlib.pyplot as plt 

days = [4,2,5,7,1]
eating = [5,6,2,1,7]
sleeping = [9,7,5,3,1]
playing = [5,7,8,1,2]
working = [6,8,1,2,3]
slices = [7,5,6,7]
activities = ["Eating", "Sleeping", "Playing", "Working"]

plt.pie(slices, labels=activities, startangle=180, shadow=True, explode=(0.1,0,0,0), autopct="%1.1f%%")

'''
plt.stackplot (days, eating, sleeping, playing, working, colors=["r","g","b","k","w"])
'''
plt.title ("idk what to call this")

plt.show()