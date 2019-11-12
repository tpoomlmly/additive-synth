from typing import List, Tuple
import wave

from wavegenerators import sine

SAMPLE_RATE: int = 44100
BYTE_DEPTH: int = 2


sample_pairs: List[Tuple[int, int]] = [(int(sample * (2 ** (BYTE_DEPTH*8 - 1))) & 0xff,
                                       (int(sample * (2 ** (BYTE_DEPTH*8 - 1))) >> 8) & 0xff)
                                       for sample in sine(200, SAMPLE_RATE, 10)]

samples: bytearray = bytearray([byte for pair in sample_pairs for byte in pair])

with wave.open("sine.wav", 'wb') as file:
    file.setframerate(SAMPLE_RATE)
    file.setnchannels(1)
    file.setsampwidth(BYTE_DEPTH)
    file.writeframes(samples)
