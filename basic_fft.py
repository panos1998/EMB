import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
frequency_points = np.linspace(0.0, N*T, N, endpoint=False)
sine_values = np.sin(50.0 * 2.0*np.pi*frequency_points) + np.sin(300*2*np.pi*frequency_points) + 0.5*np.sin(80.0 * 2.0*np.pi *frequency_points)
fourier_values = fft(sine_values)
frequency_values = fftfreq(N, T)[:N//2]
plt.plot(frequency_values, 2.0/N * np.abs(fourier_values[0:N//2]))
plt.grid()
plt.show()
