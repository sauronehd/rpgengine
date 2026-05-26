from audioFuncs import *
import pyttsx3
import sounddevice as sd

# List all devices
print(sd.query_devices())

# Show just the current default input/output
print(sd.query_devices(kind='output'))
print(sd.query_devices(kind='input'))
sd.default.device.output = 3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
compSpeak(engine,"")
engine.setProperty('voice', voices[69].id)
engine.setProperty('rate', 125)
compSpeak(engine,"Hello it's me")
