from audioFuncs import *
sd.default.device = (1,1)
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[69].id)
engine.setProperty('rate', 125)
compSpeak(engine, "Hello World")