from audioFuncs import *
import pyttsx3
#foce push
import whisper

model = whisper.load_model("base")

print("Text is:"+record_transcribe(model))
