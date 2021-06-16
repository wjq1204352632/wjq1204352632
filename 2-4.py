import os
import thinkdsp
import matplotlib.pyplot as plt
from thinkdsp import decorate
from thinkdsp import SquareSignal
from thinkdsp import TriangleSignal
triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()
decorate(xlabel='Time (s)')
spectrum = triangle.make_spectrum()
spectrum.hs[0]
print(spectrum.hs[0])
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')
plt.show()