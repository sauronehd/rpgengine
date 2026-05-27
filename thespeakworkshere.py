from audioFuncs import *
import sounddevice as sd
import numpy as np

# Find device by name instead of index

import os
import subprocess
def get_device_by_name(name):
    for i, dev in enumerate(sd.query_devices()):
        if name.lower() in dev['name'].lower():
            return i
    return None
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
import  pyttsx3

engine = pyttsx3.init()
sd.default.samplerate = 48000

card = get_alsa_card_number('google')
compSpeak(engine, "Hello World", card)