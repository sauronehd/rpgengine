from audioFuncs import *
import whisper
model = whisper.load_model("tiny")

repsonse =  record_transcribe(model)
print(repsonse)