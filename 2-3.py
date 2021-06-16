import os
import thinkdsp
from winsound import PlaySound
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
square = SquareSignal(1500).make_wave(duration=0.5, framerate=10000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
square.make_audio()
square.write("方波声音.wav")
play("方波声音.wav", flags=1)
plt.show()