import sounddevice as sd
import whisper


def record_transcribe(model):
    duration = 5
    sample_rate = 16000

    print("Recording...")
    audio = sd.rec(int(duration * sample_rate),
                   samplerate=sample_rate,
                   channels=1,
                   dtype='float32')  # Changed to float32
    sd.wait()
    print("Recording finished")

    # Flatten the audio array and normalize
    audio = audio.flatten()

    # Load model


    # Transcribe directly from numpy array
    result = model.transcribe(audio, fp16=False)

    return result["text"]