
from pinCalls import *
print("Starting")
GPIO.setmode(GPIO.BOARD)
pinOutSet()
outputCall([[pins.heat,pinState.on],[pins.fan,pinState.on],[pins.cold,pinState.on]])
wait = input("Press Enter to continue...")

