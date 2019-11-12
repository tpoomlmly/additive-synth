import math as maths
from typing import Optional, Iterable


def sawtooth(frequency: float, sample_rate: int = 44100):
    while True:
        pass


def sine(frequency: float, sample_rate: int = 44100, time: Optional[float] = None) -> Iterable[float]:
    """Generator for a sine wave with a given frequency and optional sample rate and length in seconds."""

    delta_phase: float = 2 * maths.pi * frequency / sample_rate  # The difference in phase between two samples
    phase: float = 0

    while time is None:  # If time is not None then this will just be skipped.
        yield maths.sin(phase)
        # Add the difference in phase to the next sample and make sure it doesn't go above 2π
        phase = (phase + delta_phase) % (2*maths.pi)

    for sample_num in range(int(sample_rate * time)):
        yield maths.sin(delta_phase * sample_num)
