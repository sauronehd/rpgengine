
import RPi.GPIO as GPIO
try:
    GPIO.setmode(GPIO.BOARD)
    for i in range (40):
        try:
            GPIO.setup(i, GPIO.OUT)
        finally:
            print(f"Error in setting up {i}")

    for i in range(40):
        try:
            GPIO.output(i, GPIO.HIGH)
        finally:
            print(f"Error in outputting to {i}")
finally:
    GPIO.cleanup()