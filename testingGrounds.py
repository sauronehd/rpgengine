from audioFuncs import *
import  pyttsx3
sd.default.device.output = (1,1)
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[69].id)
engine.setProperty('rate', 125)
compSpeak(engine,"")
compSpeak(engine, "Hello World")