from pinCalls import *

pinOutSet()
GPIO.setmode(GPIO.BOARD)

GPIO.output(pinOutSet.fan, GPIO.HIGH)

wait = input("Press Enter to continue...")
GPIO.cleanup()
