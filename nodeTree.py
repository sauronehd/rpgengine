#This is the idiot zone. This is where you send the first day Robotics students who
#cant code but you need them interested. The engine if i've made it right will take a
#binary node tree from here with all the apporiate data and turn it into the story.
#Every node placed needs, and i mean REQUIRES:
#leftkey
#rightkey
#prompt
#and outputs set appropiately.
#If not set, the engine will break.
#The students should creat the root node and give it all its qualities, and then makes nodes
# left and right of it, and ectrera. Ona nd on, exponential gorwth. They are allowed to make
#path end early to reduce work - path can lead to deaths or wins or boring things earlier than
#the rest of the tree.
#The easiest way to mkae this work i imiagine is to have them send you thier idiot zones
#like we did poker bots, and you can swap out which one is loaded. This system is not
#entirely robust, so simply replacing with their script through copy+paste may be the best method.
#ALWAYS MAKE SURE THE ROOT NODE IS CALLED BEGINNING! THE ENGINE WILL NOT WORK WITHOUT THIS

from nodeClass import *
import detectiontools

class nodeTree:
    def __init__(self):
        print("node tree pulled")


    #basic example of how this might look
    beginning = outputNode()
    beginning.prompt = ("Would you like to go left to candy or "
                        "right to the telephone?")
    beginning.leftKey = ["candy", "left"]
    beginning.rightKey = ["telephone", "right"]
    beginning.outputs = [("fan",2)]
    candy = outputNode()
    beginning.left = candy
    candy.prompt =("CANDY!!!!!!")
    candy.outputs = [("heat",1)]
    telephone = outputNode()
    beginning.right = telephone
    telephone.prompt = ("Would you like to turn the dial left or right?")
    telephone.outputs = [("audio", 2)]
    telephone.rightKey = ["right"]
    telephone.leftKey = ["left"]
    rightDial = outputNode()
    telephone.right = rightDial
    rightDial.prompt = ("You have called Mico. Sorry about that")
    rightDial.outputs = [("audio", 8)]
    leftDial = outputNode()
    telephone.left = leftDial
    leftDial.prompt = ("YOu have called barbara. Yay!")
    leftDial.outputs = [("Audio", 1)]


def printNode(node:outputNode):
    print(node.prompt)
    print(node.rightKey)
    print(node.leftKey)
    print(node.outputs)



