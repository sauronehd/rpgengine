import sounddevice as sd
import numpy as np

sd.default.device = (1, 1)
sd.default.samplerate = 48000

audio = sd.rec(int(3 * 48000), channels=2, dtype='float32')
sd.wait()

print("Max amplitude:", np.max(np.abs(audio)))
print("Mean amplitude:", np.mean(np.abs(audio)))