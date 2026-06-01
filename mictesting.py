from audioFuncs import *
import whisper
model = whisper.load_model("tiny")
import sounddevice as sd
print(sd.query_devices())
repsonse =  record_transcribe(model)
print(repsonse)