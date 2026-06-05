
from pinCalls import *
print("Starting")
GPIO.setmode(GPIO.BOARD)
pinOutSet()
outputCall([[pins.heat,pinState.on],[pins.fan,pinState.on],[pins.cold,pinState.on]])
wait = input("Press Enter to continue...")
GPIO.cleanup()
print("Tryong all pins now")

newpins = []

for i in range(1,40):
    newpins.append(i)
print(newpins)

for pin in newpins:
    try:
        GPIO.setup(pin,GPIO.OUT)
    except Exception as e:
        print(f"Error on pin {pin}: {e}")
for pin in newpins:
    try:
        GPIO.output(pin, GPIO.OUT)
    except:
        print(f"Error on pin {pin}")
wait = input("Press Enter to continue...")