from enum import Enum



class choice(Enum):
    left = 0
    right = 1
    unknown = 2


negatives = ["don't","won't","will not","shouldn't","should not","would not","not"]



#Note: This code is breakable. The player certainly can cause for unintended code paths.
#However, given that the only thing they can do is force the question to be reasked or go down the wrong path,
#I think that given the limitations, it is fine.
def evaluateChoice(leftKey:[str],rightKey:[str],response:str):

    if ifcontains(leftKey,response) and ifcontains(rightKey,response):
        #print("both")
        return choice.unknown
    if ifcontains(negatives,response):
        #this code will invert things
        #print("negative")
        if ifcontains(rightKey,response):
            #print("negative right, return left")
            return choice.left
        elif ifcontains(leftKey,response):
            #print("negative left, return right")
            return choice.right
        else:
            #print("negative, no keywords")
            return choice.unknown
    else:
        #read as if normal
        #print("no negatives")
        if ifcontains(rightKey,response):
            #print("Normal right")
            return choice.right
        elif ifcontains(leftKey,response):
            #print("Normal left")
            return choice.left
        else:
            #print("normal, no keywords")
            return choice.unknown


def ifcontains(keys:[str], response:str):
    for key in keys:
        if key in response:
            #print("contains: "+key)
            return True
    return False




