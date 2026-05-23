from audioFuncs import *
import pyttsx3
compSpeak(engine,"")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[69].id)
engine.setProperty('rate', 125)
compSpeak(engine,"Hello it's me")
