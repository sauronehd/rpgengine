from audioFuncs import *
import  pyttsx3

import sounddevice as sd

# Find device by name instead of index
def get_device_by_name(name):
    for i, dev in enumerate(sd.query_devices()):
        if name.lower() in dev['name'].lower():
            return i
    return None

device_index = get_device_by_name('Google')
print(f"Found at index: {device_index}")

sd.default.device = (device_index, device_index)
sd.default.samplerate = 48000
