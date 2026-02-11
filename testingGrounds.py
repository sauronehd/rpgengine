import pyttsx3
from audioFuncs import *
from pinCalls import *

GPIO.setmode(GPIO.BOARD)
pinOutSet()
outputCall([],[modpins.mister,modState.on])
wait = input("Press enter to continue")
pinReset()
GPIO.cleanup()



