from audioFuncs import *
import pyttsx3

import whisper

model = whisper.load_model("base")

print("Text is:"+record_transcribe(model))


engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)  # See what's available
engine.setProperty('voice', "en")
engine.setProperty('rate', 125)
compSpeak(engine,"") # this clear some lag
compSpeak(engine,"Hello")