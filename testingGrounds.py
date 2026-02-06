import pyttsx3
from audioFuncs import *
engine = pyttsx3.init()
engine.setProperty('rate', 125)
compSpeak(engine,"") # this clear some lag
compSpeak(engine,"Hello, testing, testing")