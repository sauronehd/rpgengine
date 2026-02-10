from pinCalls import *
class outputNode:
    #the game is designed so the player may either go left or right.
    #Put keywords you think would signify the path the user chose.
    leftKey = []
    rightKey = []

    #the goal is to have a tts AI turn these prompts into speech files we can play.
    #This is inherently easier than recording these snippets ourselves
    prompt = ""

    #outputs will be an array of tuples. The output should be a pin, and its output.
    #can have multiple outputs if you want
    outputs: list[tuple[pins, pinState]] = []
    modulatingout: list[tuple[modpins, modState]] = []




