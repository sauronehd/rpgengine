import RPi.GPIO as GPIO

# Valid BOARD mode GPIO pins (excludes power, ground, and reserved pins)
VALID_PINS = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    for i in VALID_PINS:
        try:
            GPIO.setup(i, GPIO.OUT)
            print(f"Set up pin {i}")
        except Exception as e:
            print(f"Error setting up pin {i}: {e}")

    for i in VALID_PINS:
        try:
            GPIO.output(i, GPIO.HIGH)
            print(f"Output HIGH on pin {i}")
        except Exception as e:
            print(f"Error outputting to pin {i}: {e}")

    wait = input("Press enter to continue...")

finally:
    GPIO.cleanup()