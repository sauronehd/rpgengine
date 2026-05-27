import sounddevice as sd
import time
#force push
import subprocess


def compSpeak(engine, text, card):
    print(f"Speaking: {text}")
    start = time.time()

    # generate audio with espeak
    espeak_proc = subprocess.run(
        ['espeak', text, '--stdout'],
        capture_output=True
    )

    # pipe directly to the correct device
    subprocess.run(
        ['aplay', '-D', f'plughw:{card},0'],
        input=espeak_proc.stdout
    )

    elapsed = time.time() - start
    print(f"Finished speaking in {elapsed:.2f} seconds")
def record_transcribe(model):
    duration = 5
    sample_rate = 48000
    target_rate =16000
    print("Recording...")
    audio = sd.rec(int(duration * sample_rate),
                   samplerate=sample_rate,
                   channels=1,
                   dtype='float32')
    sd.wait()
    print("Recording finished")

    # Flatten the audio array and normalize
    audio = audio.flatten()
    resample_factor = sample_rate // target_rate  # = 3
    audio = audio[::resample_factor]
    print("audio is:")
    print(audio)


    # Transcribe directly from numpy array
    result = model.transcribe(audio, fp16=False)

    sd.stop()
    time.sleep(0.5)# Give audio device time to release
    print(result["text"])
    return result["text"]

