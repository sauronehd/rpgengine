from audioFuncs import *
import whisper
model = whisper.load_model("tiny")
import sounddevice as sd
print(sd.query_devices())
sd.default.device = (3,1)
repsonse =  record_transcribe(model)
print(repsonse)
#forcre psy