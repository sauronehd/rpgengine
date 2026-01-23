from detectiontools import *
from nodeTree import *
from audioFuncs import *
import whisper
import pyttsx3
from pinCalls import *

# Read the current node's output array.
# Perform the outputs needed.
# Take the prompt and convert to sound, then play
# If the node is a leaf, exit and end
# Else, Await response
# use detection tools to identify the path
# move to the currentnode.left or .right depending
# Restate the prompt if needed
# Move to appropriate node and return to beginnning of loop.

currentNode = nodeTree.beginning
model = whisper.load_model("tiny")
engine = pyttsx3.init()
engine.setProperty('rate', 125)
compSpeak(engine,"") # this clear some lag
pinSet = "u"
while pinSet == "u":
    _input = input("Are pins set up? Enter y or n.")
    if _input == "y":
        pinSet = "y"
    elif _input == "n":
        pinSet = "n"
    else:
        pinSet = "u"
        print("Invalid input. Please enter y or n.")


while True:
    #replac with pinCalls functions
    if pinSet == "y":
        outputCall(currentNode.outputs)
    elif pinSet == "n":
        print(currentNode.outputs)
    else:
        print("Error: Pinset unknown")

    compSpeak(engine,currentNode.prompt)

    #This is placed so that you will hear and experience the final outputs before the game ends
    if getattr(currentNode, 'left', None) is None and getattr(currentNode, 'right', None) is None:
        break

    response = record_transcribe(model)
    response = response.lower()
    print("The repsonse is: ")
    print(response)

    path = evaluateChoice(currentNode.leftKey,currentNode.rightKey,response)
    while path == choice.unknown:
        #replace with tts output
        compSpeak(engine,"Sorry, I didnt understand that")
        compSpeak(engine,"What would you like to do?")

        #replace with stt input mike
        response = record_transcribe(model)
        print("The repsonse is: ")
        print(response)

        path = evaluateChoice(currentNode.leftKey,currentNode.rightKey,response)

    if path == choice.left:
        currentNode = currentNode.left
    elif path == choice.right:
        currentNode = currentNode.right
    else:
        print("Error: Choice is extraneous value:")
        print(path)

engine.stop()
print("Goodbye")

