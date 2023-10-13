#Created By Ali Adnan
#CMP521A


#Variables & Imports

import random
import time

#Code---------------

def randomtest():
    for i in range(11):
        print (random.randrange(33,116,2))
        time.sleep (.3)
    time.sleep (2)
    for i in range(1):
        print (random.choice(["Volleyball", "swimming", "hockey", "soccer", "basketball", "badminton", "cross country", "rugby", "football", "cycling", "motor cross"]))
        time.sleep (.3) 