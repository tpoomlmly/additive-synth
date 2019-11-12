import math as maths
import wave


def f(x):
    return maths.sin(x) + maths.sin(2*x)/2 + maths.sin(3*x)/3 + maths.sin(4*x)/4 + maths.sin(5*x)/5 + maths.sin(6*x)/6 + maths.sin(7*x)/7 + maths.sin(8*x)/8 + maths.sin(9*x)/9 + maths.sin(10*x)/10


def p(x):
    return (f(x/8) + f(x/4) + f(x/2) + f(x) + f(2*x) + f(4*x) + f(8*x))/7


def scale_to_16_bit(x):
    return int((p(2*maths.pi*x*200/44100)/1.16453)*32768)


sample_pairs = [(scale_to_16_bit(i) & 0xff, (scale_to_16_bit(i) >> 8) & 0xff) for i in range(441000)]

samples = bytearray([byte for pair in sample_pairs for byte in pair])  # Flatten
file = wave.open("organ.wav", 'wb')
file.setframerate(44100)
file.setnchannels(1)
file.setsampwidth(2)
file.writeframes(samples)
file.close()
