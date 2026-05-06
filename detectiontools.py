from nodeClass import *
import typing

def returnnode(dictionary:dict, response:str):

    keys = dictionary.keys()
    for key in keys:
        if key in response:
            node = dictionary.get(key)
            return node

    return False




