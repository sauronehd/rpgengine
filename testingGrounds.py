import sounddevice as sd
import numpy as np

sd.default.device = (1, 1)
sd.default.samplerate = 48000

audio = sd.rec(int(3 * 48000), channels=1, dtype='float32')
sd.wait()

print("Max amplitude:", np.max(np.abs(audio)))
print("Mean amplitude:", np.mean(np.abs(audio)))

device_info = sd.query_devices(1)
print("Max input channels:", device_info['max_input_channels'])
print("Max output channels:", device_info['max_output_channels'])