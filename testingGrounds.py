import whisper
model = whisper.load_model("tiny")

import sounddevice as sd
import numpy as np
from audioFuncs import *
sd.default.device = (1, 1)
sd.default.samplerate = 48000

record_transcribe(model)
sd.wait()