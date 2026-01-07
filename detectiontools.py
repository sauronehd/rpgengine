from enum import Enum, auto

class detectionTools():

    def __init__(self):
        print("detectionTools init called")

    class choice(Enum):
        left = 0
        right = 1
        unknown = 2

    class pins(Enum):
        #will add and change as we go
        shaker = 0
        audio = 1
        sprinkler = 2

    class outputs(Enum):
        off = 0
        low = 1
        high =2


    negatives = ["don't","won't","will not",
                 "shouldn't","should not"]


    def ifcointains(self, keys: Array[String], response: string):
        for key in keys:
            if find(key in response):
                return true

        return false
    #Note: This code is breakable. The player certainly can cause for unintended code paths.
    #However, given that the only thing they can do is force the question to be reasked or go down the wrong path,
    #I think that given the limitations, it is fine.
    def evaluateChoice(self,leftKey:Array[String],
                       rightKey:Array[String],response:string):
        if ifcontains(negatives,response):
            #this code will invert things
            if ifconains(rightKey,response):
                return choice.left
            elif ifconains(leftKey,response):
                return choice.right
            else:
                return choice.unknown
        else:
            #read as if normal
            if ifconains(rightKey,response):
                return choice.right
            elif ifconains(leftKey,response):
                return choice.left
            else:
                return choice.unknown






