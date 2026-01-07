import detectiontools
from  dataclasses import dataclass
class outputNode:
    #SHould force people to only use the ocrrect pins, as well as gives more descriptive names to them
    #ALso forces only off/low/high for easier control.
    @dataclass
    class pinouts:
        pin: detectiontools.pins
        signal: detectiontools.outputs
    #the game is designed so the player may either go left or right.
    #Put keywords you think would signify the path the user chose.
    leftKey = []
    rightKey = []
    #the goal is to have a tts ai turn these prompts into speech files we can play.
    #This is inherently easier then recording these snippets ourselves
    prompt = ""
    #outputs will be an array of pinouts.
    #can have multiple outputs if you want
    outputs = Array[pinouts]





