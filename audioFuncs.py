import sounddevice as sd
import whisper
import pyttsx3
import time

def record_transcribe(model):
    duration = 5
    sample_rate = 16000

    print("Recording...")
    audio = sd.rec(int(duration * sample_rate),
                   samplerate=sample_rate,
                   channels=1,
                   dtype='float32')
    sd.wait()
    print("Recording finished")

    # Flatten the audio array and normalize
    audio = audio.flatten()


    # Transcribe directly from numpy array
    result = model.transcribe(audio, fp16=False)
    sd.stop()
    time.sleep(0.5)  # Give audio device time to release
    return result["text"]

def compSpeak(engine,text):
    time.sleep(0.3)
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()
    print("Finished speaking")
