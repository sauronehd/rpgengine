from audioFuncs import *

import whisper

model = whisper.loadModel("base")

record_transcribe(model)



