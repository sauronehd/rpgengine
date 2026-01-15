from detectiontools import ifcontains

if ifcontains(["no","yay"]," i really don want to yay"):
    print("contains")

else:
    print("not contains")