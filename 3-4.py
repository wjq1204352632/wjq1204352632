from thinkdsp import Chirp
from thinkdsp import normalize, unbias
from winsound import PlaySound
import matplotlib.pyplot as plt
import thinkdsp
import numpy as np
import os
PI2 = 2 * np.pi
from thinkdsp import decorate
wave = thinkdsp.read_wave('72475__rockwehrmann__glissup02.wav')
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()