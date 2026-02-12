#use this to make callable functions for outputs(fans, heater, ect)
from enum import Enum
import Jetson.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
class pins(Enum):
    fan = 60
    cold = 32
    heat =33

class modpins(Enum):
    mister = GPIO.PWM(15, 1000000)


#May have to backtrack later and use pinState.on.value for things because of how enums work
#Im unsure.
class pinState(Enum):
    on = GPIO.HIGH
    off = GPIO.LOW

class modState(Enum):
    on = 100
    off = 0

def outputCall(gpioouts,modulatingout):
    #print(outs)
    for out in gpioouts:
            GPIO.output(out[0].value, out[1].value)

    for mod in modulatingout:
        mod[0].value.ChangeDutyCycle(mod[1].value)








def pinOutSet():

    for pin in pins:
        try:
            GPIO.setup(pin.value, GPIO.OUT)
        except:
            print("Error:Failed to setup GPIO pin:"+str(pin.value))

    for pin in modpins:
        try:
            GPIO.setup(pin.value.channel, GPIO.OUT)
        except:
            print("Error:Failed to setup GPIO pin:"+str(pin.value))



def pinReset():
    for pin in pins:
        GPIO.output(pin.value, pinState.off.value)

    for pin in modpins:
        pin.value.ChangeDutyCycle(modState.off.value)

