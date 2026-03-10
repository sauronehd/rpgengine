from audioFuncs import *
import pyttsx3
#foce push
import whisper

model = whisper.load_model("base")
print(sd.query_devices())
print(sd.query_devices(kind='input'))
print("Text is:"+record_transcribe(model))
