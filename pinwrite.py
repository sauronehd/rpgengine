
from pinCalls import *
print("Starting")
GPIO.setmode(GPIO.BOARD)
pinOutSet()
for pin in pins:
    outputCall(pin,pinState.on)
wait = input("Press Enter to continue...")
GPIO.cleanup()
print("Goodbye")