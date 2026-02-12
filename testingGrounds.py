
from audioFuncs import *
from pinCalls import *
print("setting to baord")
GPIO.setmode(GPIO.BOARD)
print("pinoutsetcall")
pinOutSet()
print("output call ")
outputCall([],[[modpins.mister,modState.on]])
wait = input("Press enter to continue")
pinReset()
GPIO.cleanup()



