#use this to make callable functions for outputs(fans, heater, ect)
from enum import Enum
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
class pins(Enum):
    fan = 13
    cold = 15
    heat = 21
    speaker = 34
    subwoofer = 35

#May have to backtrack later and use pinState.on.value for things because of how enums work
#Im unsure.
class pinState(Enum):
    on = GPIO.HIGH
    off = GPIO.LOW



def outputCall(gpioouts):
    #print(outs)
    for out in gpioouts:
            GPIO.output(out[0].value, out[1].value)


def pinOutSet():

    for pin in pins:
        try:
            GPIO.setup(pin.value, GPIO.OUT)
        except:
            print("Error:Failed to setup GPIO pin:"+str(pin.value))


def pinReset():
    for pin in pins:
        GPIO.output(pin.value, pinState.off.value)


