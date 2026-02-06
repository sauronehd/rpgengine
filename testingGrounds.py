from audioFuncs import *
import whisper
model = whisper.load_model("base")
record_transcribe(model)