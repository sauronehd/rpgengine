from audioFuncs import *
import subprocess

def get_alsa_card_number(name):
    result = subprocess.run(['aplay', '-l'], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if name.lower() in line.lower():
            card_num = line.split(':')[0].replace('card', '').strip()
            return card_num
    return None

card = get_alsa_card_number('google')
print(f"Card number: {card}")
print(f"Using device: plughw:{card},0")

# Test aplay directly
result = subprocess.run(
    ['espeak', 'Hello World', '--stdout'],
    capture_output=True
)
print(f"espeak output size: {len(result.stdout)} bytes")

aplay_result = subprocess.run(
    ['aplay', '-D', f'plughw:{card},0', '-v'],
    input=result.stdout,
    capture_output=True,
    text=False
)
print(f"aplay stdout: {aplay_result.stdout}")
print(f"aplay stderr: {aplay_result.stderr}")
print(f"aplay return code: {aplay_result.returncode}")