from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

data = loadmat(r'voice_data.mat')  # Load data
Fs = data['Fs'][0][0]  # Sampling frequency
signal_list = []
for i in range(0, 10):
    signal_list.append([points[i] for points in data['x']])  # this list contains 10 lists
                                                             # of 38080 values
i = 0
time = np.linspace(0, (len(signal_list[0])) / Fs, len(signal_list[0]))  # time axis format
for signal in signal_list:  # plot each signal
    i += 1
    plt.plot(time,signal)
    plt.title(f' Number of signal {i}')
    plt.show()

fouriers = []
for signal in signal_list:
    fouriers.append(fft.fft(signal))

print(fouriers)