from enum import Enum, auto

class detectionTools():

    def __init__(self):
        print("detectionTools init called")

    class choice(Enum):
        left = 0
        right = 1
        unknown = 2

    negatives = ["don't","won't","will not",
                 "shouldn't","should not"]


    def ifcointains(self, keys: Array[String], response: string):
        for key in keys:
            if find(key in response):
                return true

        return false

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
            if ifconains(rightKey,response):
                return choice.right
            elif ifconains(leftKey,response):
                return choice.left
            else:
                return choice.unknown






