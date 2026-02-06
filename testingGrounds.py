from audioFuncs import *
import whisper
model = whisper.load_model("base")
print(record_transcribe(model))