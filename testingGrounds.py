from pinCalls import *
import Jetson.GPIO as GPIO
import time
print("commencing test")
GPIO.setmode(GPIO.BOARD)
pinOutSet()
outputCall([[pins.fan,pinState.on],[pins.heat,pinState.on],[pins.cold,pinState.on]])
wait = input("Press enter to continue")
outputCall([[pins.fan,pinState.off]])

GPIO.cleanup()
print("testing complete")