from pinCalls import *

pinOutSet()
GPIO.setmode(GPIO.BOARD)

GPIO.output(pins.fan.value, GPIO.HIGH)
GPIO.output(pins.heat.value, GPIO.LOW)
GPIO.output(pins.cold.value, GPIO.HIGH)
print("Writing to 19, 13, 15")
wait = input("Press Enter to continue...")
GPIO.cleanup()
