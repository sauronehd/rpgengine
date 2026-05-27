from audioFuncs import *
import  pyttsx3
import sounddevice as sd
import numpy as np

# Find device by name instead of index

import os
import subprocess

def get_alsa_card_number(name):
    result = subprocess.run(['aplay', '-l'], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if name.lower() in line.lower():
            # extract card number
            card_num = line.split(':')[0].replace('card', '').strip()
            return card_num
    return None

card = get_alsa_card_number('google')
os.environ['AUDIODEV'] = f'plughw:{card},0'

engine = pyttsx3.init()
sd.default.samplerate = 48000



device_index = get_device_by_name('Google')
sd.default.device = (device_index, device_index)

# Generate a tone
t = np.linspace(0, 2, int(48000 * 2))
tone = (np.sin(2 * np.pi * 440 * t) * 0.5).astype('float32')

print(f"Playing to device {device_index}...")
sd.play(tone, samplerate=48000, device=device_index)
sd.wait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[69].id)
engine.setProperty('rate', 125)
compSpeak(engine,"")
compSpeak(engine,"Hello World")