import pyttsx3

engine = pyttsx3.init()  # object creation

engine.setProperty('rate', 150)  # setting up new voice rate
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

voices = engine.getProperty('voices')       # getting details of current voice
engine.setProperty('voice', voices[0].id)   # changing index, changes voices. o for male,
# engine.setProperty('voice', voices[1].id)   # 1 for female
# engine.setProperty('voice', voices[2].id)   # 2 for russian female

with open('example.txt', 'r', encoding='utf8') as f:
    for line in f:
        engine.say(str(line))

engine.runAndWait()
engine.stop()
