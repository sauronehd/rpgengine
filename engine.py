from detectiontools import *
from nodeTree import *

currentNode = nodeTree.beginning

#while True:
print(currentNode.prompt)
print("What would you like to do?")
response = input("> ")
path = evaluateChoice(currentNode.leftKey,currentNode.rightKey,response)
while path == choice.unknown:
    print("Sorry, I didn't understand that.")
    print("What would you like to do?")
    response = input("> ")
    path = evaluateChoice(currentNode.leftKey,currentNode.rightKey,response)
print(path)




    #Read the current node's output array.
    #Perform the outputs needed.
    #Take the prompt and convert to sound, then play
    #If the node is a leaf, exit and end
    #Else, Await response
    #use detection tools to identify the path
    #move to the currentnode.left or .right depending
    #Restate the prompt if needed
    #Move to appropriate node and return to beginnning of loop.
