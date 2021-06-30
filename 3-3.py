from thinkdsp import Chirp
from thinkdsp import normalize, unbias
from winsound import PlaySound
import matplotlib.pyplot as plt
import numpy as np
PI2 = 2 * np.pi
from thinkdsp import decorate
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
class SawtoothChirp(Chirp):
    """Represents a sawtooth signal with varying frequency."""

    def evaluate(self, ts):
        """Helper function that evaluates the signal.

        ts: float array of times
        """
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys
signal = SawtoothChirp(start=2500, end=3000)
wave = signal.make_wave(duration=1, framerate=20000)
wave.write("锯齿波啁啾声音.wav")
play("锯齿波啁啾声音.wav", flags=1)

wave.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')
plt.show()