
import RPi.GPIO as GPIO
try:
    GPIO.setmode(GPIO.BOARD)
    for i in range (40):
        try:
            GPIO.setup(i, GPIO.OUT)
        except error as e:
            print(e)

    for i in range(40):
        try:
            GPIO.output(i, GPIO.HIGH)
        except error as e:
            print(e)
finally:
    GPIO.cleanup()