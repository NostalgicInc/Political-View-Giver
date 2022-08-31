import random
import time
import tkinter

random.seed(int(round(time.time())))
rng1 = random.randint(0, 3)
rng2 = random.randint(0, 99)
if rng1 == 0:
    pol = "democratic party"
elif rng1 == 1:
    pol = "republican party"
elif rng1 == 2:
    pol = "libertarian party"
else:
    pol = "green party"

if rng2 > 80:
    level = "extremist"
elif (rng2 > 40) & (rng2 <= 80):
    level = "moderate"
else:
    level = "light"

lines = ["You are a " + level + " " + pol + " member", "don't @me its the truth"]
with open('READNOW.txt', 'w') as f:
    f.write('\n'.join(lines))