from audioFuncs import *

import whisper

model = whisper.load_model("base")

print("Text is:"+record_transcribe(model))



