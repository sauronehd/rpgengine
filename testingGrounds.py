from audioFuncs import *
import  pyttsx3
import sounddevice as sd
import numpy as np

# Find device by name instead of index

def get_device_by_name(name):
    for i, dev in enumerate(sd.query_devices()):
        if name.lower() in dev['name'].lower():
            return i
    return None

device_index = get_device_by_name('Google')
print(f"Found at index: {device_index}")
print(sd.query_devices(device_index))

sd.default.device = (device_index, device_index)
sd.default.samplerate = 48000



device_index = get_device_by_name('Google')

# Generate a tone
t = np.linspace(0, 2, int(48000 * 2))
tone = (np.sin(2 * np.pi * 440 * t) * 0.5).astype('float32')

print(f"Playing to device {device_index}...")
sd.play(tone, samplerate=48000, device=device_index)
sd.wait()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[69].id)
# engine.setProperty('rate', 125)
# compSpeak(engine,"")
# compSpeak(engine,"Hello World")