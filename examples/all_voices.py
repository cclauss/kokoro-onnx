"""
pip install kokoro-onnx soundfile

wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json
python examples/all_voices.py
"""

import soundfile as sf
from kokoro_onnx import Kokoro

kokoro = Kokoro('kokoro-v0_19.onnx', 'voices.json')
for voice in kokoro.get_voices():
    samples, sample_rate = kokoro.create('Hello! This audio generated by kokoro!', voice, speed=1.0)
    sf.write(f'{voice}.wav', samples, sample_rate)
    print(f'Created {voice}.wav')