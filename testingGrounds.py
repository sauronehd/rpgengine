import pyttsx3
from audioFuncs import *
from pinCalls import *

GPIO.setmode(GPIO.BOARD)
pinOutSet()
outputCall([[pins.cold,pinState.on],[pins.heat,pinState.on],[pins.fan,pinState.on]],[modpins.mister,modState.on])
wait = input("Press enter to continue")
pinReset()
GPIO.cleanup()



