import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
frequency_axis = np.linspace(0.0, N*T, N, endpoint=False)
sine_wave = np.sin(50.0 * 2.0*np.pi*frequency_axis) + np.sin(300*2*np.pi*frequency_axis) + 0.5*np.sin(80.0 * 2.0*np.pi *frequency_axis)
sine_fourier = fft(sine_wave)
frequency_partition = fftfreq(N, T)[:N//2]
plt.plot(frequency_partition, 2.0/N * np.abs(sine_fourier[0:N//2]))
plt.grid()
plt.show()
