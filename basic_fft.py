"""
A simple fft implementation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
partition = np.linspace(0.0, N*T, N, endpoint=False)
sine = np.sin(50.0 * 2.0*np.pi*partition) + np.sin(300*2*np.pi*partition) + \
              0.5*np.sin(80.0 * 2.0*np.pi *partition)
fouriervalues = fft(sine)
frequency = fftfreq(N, T)[:N//2]
plt.plot(frequency, 2.0/N * np.abs(fouriervalues[0:N//2]))
plt.grid()
plt.show()
