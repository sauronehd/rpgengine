from pinCalls import *
import Jetson.GPIO as GPIO
import time
print("commencing test")
GPIO.setmode(GPIO.BOARD)
pinOutSet()
outputCall([[pins.fan,pinState.on]])
time.sleep(2)
outputCall([[pins.fan,pinState.off]])

GPIO.cleanup()
print("testing complete")