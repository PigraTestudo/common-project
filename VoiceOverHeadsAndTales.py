import pyttsx3
import numpy as np
import time

heads_count = 0
tales_count = 0

headsandtales = np.random.choice([0, 1], size=10, p=[0.5, 0.5])
print(headsandtales)

engine = pyttsx3.init()

for i in range(len(headsandtales)):
    if headsandtales[i] == 0:
        engine.say("Heads")
        heads_count += 1
    else:
        engine.say("Tales")
        tales_count += 1

time_start = time.time()
engine.runAndWait()
time_taken = time.time() - time_start
print("There are {} heads and {} tales".format(heads_count, tales_count))
print("It took ~{} seconds to voiceover them all".format(int(time_taken)))
