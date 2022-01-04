from typing import List, Tuple
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft


def data_formatting(data_path: str) -> Tuple[List, int]:
    data = loadmat(data_path)
    sampling_frequency = data['Fs'][0][0]
    signal_list = []
    for i in range(len(data['x'][0])):
        signal_list.append([points[i] for points in data['x']])  # this list contains 10 lists
                                                                 # of 38080 values
    return signal_list, sampling_frequency


def time_plot(data: List, frequency: int, index: int = 0) -> None:
    time = np.linspace(0, (len(data)) / frequency, len(data))
    plt.plot(time, data)
    plt.title(f' Number of signal {index + 1}')
    plt.show()


def fourier_plot(signal: List, frequency: int, index: int) -> None:
    fouriers.append(fft.fft(signal))
    fourier_mag = abs(fouriers[index])
    freqs.append(np.linspace(0, Fs, len(signal) // 2))
    plt.plot(freqs[index], fourier_mag[0:len(signal) // 2])
    plt.title(f'Fourrier of signal: {index + 1}')
    plt.xlabel('frequency in Hz')
    plt.ylabel('Fourier magnitude ')
    plt.show()


signal_list, Fs = data_formatting(r'voice_data.mat')  # extract formatted signal list
                                                    # and sampling frequency

i = 0
# plot all signals in time domain
for signal in signal_list:
    time_plot(signal, Fs, index=i)  # plot each signal
    i += 1

fouriers = []
freqs = []

i = 0
# plot all fourier transforms in frequency domain
for signal in signal_list:
    fourier_plot(signal, Fs, index=i)
    i += 1