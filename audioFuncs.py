import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper

def record_transcribe():
    # Record audio
    duration = 3  # seconds
    sample_rate = 16000  # Hz
    model = whisper.load_model("base")

    print("Recording...")
    audio = sd.rec(int(duration * sample_rate),
                   samplerate=sample_rate,
                   channels=1,
                   dtype='int16')

    sd.wait()  # Wait until recording is finished
    print("Recording finished")

    write('output.wav', sample_rate, audio)

    result = model.transcribe("output.wav")
    return result["text"]
