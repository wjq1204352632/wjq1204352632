import os
import thinkdsp
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
import numpy as np
from thinkdsp import decorate
from thinkdsp import SawtoothSignal
import matplotlib.pyplot as plt
class SawtoothSignal(Sinusoid):
    """Represents a sawtooth signal."""
    def evaluate(self, ts):
        """Evaluates the signal at the given times.
        ts: float array of times
        returns: float wave array
        """
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys
sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
from thinkdsp import SquareSignal
sawtooth.make_spectrum().plot(color='black')
square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
sawtooth.make_spectrum().plot(color='yellow')
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
from thinkdsp import TriangleSignal
sawtooth.make_spectrum().plot(color='red')
triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
triangle.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()
