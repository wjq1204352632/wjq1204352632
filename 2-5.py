import os
import thinkdsp
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
from thinkdsp import SawtoothSignal
from winsound import PlaySound
def filter_spectrum(spectrum):
    # avoid division by 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
trangle = TriangleSignal(freq=440).make_wave(duration=0.01, framerate=10000)
plt.subplot(231)
plt.title("trangle")

trangle .plot()
trangle.write("三角波声音.wav")
play("三角波声音.wav", flags=1)
square = SquareSignal(freq=440).make_wave(duration=0.01, framerate=10000)
plt.subplot(232)
plt.title("square")
square.plot()
square.write("方波声音.wav")
play("方波声音.wav", flags=1)
sawtooth = SawtoothSignal(freq=440).make_wave(duration=0.01, framerate=10000)
plt.subplot(233)
plt.title("sawtooth")
sawtooth.plot()
sawtooth.write("斜波声音.wav")
play("斜波声音.wav", flags=1)


spectrum_tra = trangle.make_spectrum()
filter_spectrum(spectrum_tra)
plt.subplot(234)
spectrum_tra.plot()

spectrum_squ = square.make_spectrum()
filter_spectrum(spectrum_squ)
plt.subplot(235)
spectrum_squ.plot()

spectrum_saw = sawtooth.make_spectrum()
filter_spectrum(spectrum_saw)
plt.subplot(236)
spectrum_saw.plot()

plt.show()