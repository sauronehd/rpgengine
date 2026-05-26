from xml.dom.expatbuilder import theDOMImplementation

from audioFuncs import *
import pyttsx3
import sounddevice as sd

# List all devices
print(sd.query_devices())

# Show just the current default input/output
print("Outputs are:")
print(sd.query_devices(kind='output'))
print("Inputs are:")
print(sd.query_devices(kind='input'))
device = input("Choose a Device:")
sd.default.device.output = device

engine = pyttsx3.init()
voices = engine.getProperty('voices')
compSpeak(engine,"")
engine.setProperty('voice', voices[69].id)
engine.setProperty('rate', 125)
compSpeak(engine,"Hello it's me")
