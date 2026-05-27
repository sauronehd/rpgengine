from detectiontools import *
from nodetree import *
from audioFuncs import *
import whisper
from pinCalls import *
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
currentNode = nodeTree.beginning
model = whisper.load_model("tiny")
card = get_alsa_card_number('google')
os.environ['AUDIODEV'] = f'plughw:{card},0'
import  pyttsx3

engine = pyttsx3.init()
sd.default.samplerate = 48000

card = get_alsa_card_number('google')
sd.default.device = (1,1)


while True:
    outputCall(currentNode.outputs)
    print(currentNode.outputs)
    compSpeak(engine,currentNode.prompt,card)

    #This is placed so that you will hear and experience the final outputs before the game ends
    if currentNode.children == {}:
        break

    response = record_transcribe(model)
    response = response.lower()
    print("The repsonse is: ")
    print(response)
    #change evaluate choice
    if currentNode.children.keys().__len__() == 0:
        newnode = currentnode.children.get(currentNode.children.keys()[0])
    else:
        newnode = returnnode(currentNode.children,response)
        while newnode == False:
            #replace with tts output
            compSpeak(engine,"Sorry, I didnt understand that")
            compSpeak(engine,"What would you like to do?")

            #replace with stt input mike
            response = record_transcribe(model)
            print("The repsonse is: ")
            print(response)

            newnode = returnnode(currentNode.children,response)

    currentNode = newnode

engine.stop()
GPIO.cleanup()
print("Goodbye")

