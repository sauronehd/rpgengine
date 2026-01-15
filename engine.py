import detectiontools
import nodeClass
from nodeTree import *
import pinCalls

currentNode = nodeTree.beginning

printNode(currentNode)
currentNode = currentNode.left
printNode(currentNode)
currentNode = nodeTree.beginning
currentNode = currentNode.right
printNode(currentNode)
    #Read the current node's output array.
    #Perform the outputs needed.
    #Take the prompt and convert to sound, then play
    #If the node is a leaf, exit and end
    #Else, Await response
    #use detection tools to identify the path
    #move to the currentnode.left or .right depending
    #Restate the prompt if needed
    #Move to appropriate node and return to beginnning of loop.
