import sounddevice as sd

device_info = sd.query_devices(1)
print(device_info)