#use this to make callable functions for outputs(fans, heater, ect)
from enum import Enum
import Jetson.GPIO as GPIO


class pins(Enum):
    #these ae place holder values
    heat = 1
    fan = 2
    cold = 3


def outputCall(outs):
    print(outs)
    for pin in outs:
        if pin(0) == pins.heat:
            GPIO.output(pins.heat.value, readOut(pin))
        elif pin(0) ==pin.fan:
            GPIO.output(pin.fan.value, readOut(pin))
        elif pin(0) ==pin.cold:
            GPIO.output(pin.cold.value, readOut(pin))
        else:
            print("Error:Unknown Pin reference")

def readOut(pin):
    if pin(1) == 0:
        return GPIO.LOW
    elif pin(1) == 1:
        return GPIO.HIGH
    print("Failure, turning off.")
    return GPIO.LOW

def pinReset():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)