from audioFuncs import *
import pyttsx3
#foce push
import whisper

model = whisper.load_model("base")

print("Text is:"+record_transcribe(model))


engine = pyttsx3.init()
engine.setProperty('voice', "en")
engine.setProperty('rate', 125)
compSpeak(engine,"") # this clear some lag
compSpeak(engine,"Hello")