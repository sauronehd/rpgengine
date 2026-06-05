from detectiontools import *
from nodetree import *
from audioFuncs import *
import whisper
from pinCalls import *
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
currentNode = nodeTree.beginning
model = whisper.load_model("tiny")
os.environ['AUDIODEV'] = f'plughw:{card},0'
import  pyttsx3

engine = pyttsx3.init()
sd.default.samplerate = 48000

card = 2
sd.default.device = (3,1)


while True:
    time.sleep(3)
    outputCall(currentNode.outputs)
    print(currentNode.outputs)
    compSpeak(currentNode.prompt,card)

    #This is placed so that you will hear and experience the final outputs before the game ends
    if currentNode.children == {}:
        break

    response = record_transcribe(model)
    response = response.lower()
    print("The response is: ")
    print(response)
    #change evaluate choice
    if currentNode.children.keys().__len__() == 1:
        newnode = currentnode.children.get(currentNode.children.keys()[0])
    else:
        newnode = returnnode(currentNode.children,response)
        while newnode == False:
            compSpeak("Sorry, I didnt understand that",card)
            compSpeak("What would you like to do?",card)

            response = record_transcribe(model)
            print("The repsonse is: ")
            print(response)

            newnode = returnnode(currentNode.children,response)

    currentNode = newnode
    pinReset()

engine.stop()
GPIO.cleanup()
print("Goodbye")

