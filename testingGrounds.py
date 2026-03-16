from RPi import GPIO
GPIO.setmode(GPIO.BOARD)
#force push
for i in range(1,40):
    try:
        GPIO.setup(i,GPIO.OUT)
        GPIO.output(i,GPIO.HIGH)
    except:
        print(f"Error on pin: {i}")


wait = input("Press Enter to continue...")

GPIO.cleanup()