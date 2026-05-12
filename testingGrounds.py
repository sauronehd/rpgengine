from pinCalls import *

pinOutSet()
GPIO.setmode(GPIO.BOARD)

GPIO.output(pins.fan.value, GPIO.HIGH)

wait = input("Press Enter to continue...")
GPIO.cleanup()
