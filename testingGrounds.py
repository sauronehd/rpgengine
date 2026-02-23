
from audioFuncs import *
from pinCalls import *
print("setting to baord")
import RPi.GPIO as GPIO
print("pinoutsetcall")
pinOutSet()
print("output call ")
outputCall([])
wait = input("Press enter to continue")
pinReset()
GPIO.cleanup()



