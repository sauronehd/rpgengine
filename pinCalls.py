#use this to make callable functions for outputs(fans, heater, ect)
from enum import Enum
import Jetson.GPIO as GPIO


class pins(Enum):
    #these ae placeholder values
    fan = 15
    cold = 32
    heat =33

#May have to backtrack later and use pinState.on.value for things because of how enums work
#Im unsure.
class pinState(Enum):
    on = GPIO.HIGH
    off = GPIO.LOW

def outputCall(outs):
    #print(outs)
    for out in outs:
            GPIO.output(out[0].value, out[1].value)





def pinOutSet():

    for pin in pins:
        try:
            GPIO.setup(pin.value, GPIO.OUT)
        except:
            print("Error:Failed to setup GPIO pin:"+str(pin.value))


def pinReset():
    for pin in pins:
        GPIO.output(pin, pinState.off.value)