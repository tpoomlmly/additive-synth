from typing import Tuple, Iterable

from wavegenerators import sine
import wave

SAMPLE_RATE: int = 60000000
BYTE_DEPTH: int = 2
LENGTH: float = 0.01

# Create a 3MHz carrier and a 200Hz sound and multiply them, after scaling and shifting the audio signal
signal: Iterable[float] = (carrier * (audio + 1.5) / 2.5
                           for carrier, audio
                           in zip(sine(3000000, SAMPLE_RATE, LENGTH),
                                  sine(200, SAMPLE_RATE, LENGTH)))

# Scale each sample from the range [-1, 1] to [-32767, 32767] and cast to int.
# Then, split it into a low byte and high byte; lower byte first for little-endian systems.
sample_pairs: Iterable[Tuple[int, int]] = ((int(sample * (2 ** (BYTE_DEPTH * 8 - 1) - 1)) & 0xff,  # Low byte
                                           (int(sample * (2 ** (BYTE_DEPTH * 8 - 1) - 1)) >> 8) & 0xff)  # High byte
                                           for sample in signal)

# Unpack the pairs of samples into one long list and make a bytearray out of it
samples: bytearray = bytearray([byte for pair in sample_pairs for byte in pair])

with wave.open("AM.wav", 'wb') as file:
    file.setframerate(SAMPLE_RATE)
    file.setnchannels(1)
    file.setsampwidth(BYTE_DEPTH)
    file.writeframes(samples)
