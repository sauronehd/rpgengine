from detectiontools import *
from nodeTree import *
from pinCalls import *
from audioFuncs import *

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

while True:
    #replac with pinCalls functions
    print(currentNode.outputs)

    #replace with tts code
    print(currentNode.prompt)

    #This is placed so that you will hear and experience the final outputs before the game ends
    if getattr(currentNode, 'left', None) is None and getattr(currentNode, 'right', None) is None:
        break

    #replace with tts code
    print("What would you like to do?")

    #replace with mike stt input
    response = record_transcribe()

    path = evaluateChoice(currentNode.leftKey,currentNode.rightKey,response)
    while path == choice.unknown:
        #replace with tts output
        print("Sorry, I didn't understand that.")
        print("What would you like to do?")

        #replace with stt input mike
        response = record_transcribe()

        path = evaluateChoice(currentNode.leftKey,currentNode.rightKey,response)

    if path == choice.left:
        currentNode = currentNode.left
    elif path == choice.right:
        currentNode = currentNode.right
    else:
        print("Error: Choice is extraneous value:")
        print(path)




print("Goodbye")

