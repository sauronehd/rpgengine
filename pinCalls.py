#use this to make callable functions for outputs(fans, heater, ect)
from enum import Enum
import Jetson.GPIO as GPIO


class pins(Enum):
    #these ae placeholder values
    heat = 1
    fan = 15
    cold = 4

#May have to backtrack later and use pinState.on.value for things because of how enums work
#Im unsure.
class pinState(Enum):
    on = GPIO.HIGH
    off = GPIO.LOW

def outputCall(outs):
    #print(outs)
    for out in outs:
        if out[0] == pins.heat:
            GPIO.output(pins.heat.value, out[1])
        elif out[0] == pins.fan:
            GPIO.output(pins.fan.value, out[1])
        elif out[0] == pins.cold:
            GPIO.output(pins.cold.value, out[1])
        else:
            print("Error:Unknown Pin reference")



def pinOutSet():
    try:
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
    finally:
        pass


def pinReset():
    for pin in pins:
        GPIO.output(pin, pinState.off)