import pyttsx3
import numpy as np
import time

heads_count = 0
tails_count = 0

headsandtails = np.random.choice([0, 1], size=10, p=[0.5, 0.5])

engine = pyttsx3.init()

for i in range(len(headsandtails)):
    if headsandtails[i] == 0:
        engine.say("Heads")
        heads_count += 1
    else:
        engine.say("Tails")
        tails_count += 1

time_start = time.time()
engine.runAndWait()
time_taken = time.time() - time_start

print(headsandtails, '\n')
print("There are {} heads and {} tails".format(heads_count, tails_count))
print("It took ~{} seconds to voiceover them all".format(int(time_taken)))
