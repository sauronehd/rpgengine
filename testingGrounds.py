import sounddevice as sd
import numpy as np

sd.default.device = (1, 1)
sd.default.samplerate = 48000

# Play a simple tone
duration = 2
freq = 440
t = np.linspace(0, duration, int(48000 * duration))
tone = (np.sin(2 * np.pi * freq * t) * 0.3).astype('float32')

sd.play(tone, samplerate=48000, device=1)
sd.wait()