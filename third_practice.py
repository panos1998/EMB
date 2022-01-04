from typing import List, Tuple
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

# function to reformat data
def data_formatting(data_path: str) -> Tuple[List, int]:
    data = loadmat(data_path) # load data from path
    sampling_frequency = data['Fs'][0][0] # extract sampling frequency
    signal_list = []  # initialize signal list
    for i in range(len(data['x'][0])): # reformat data
        signal_list.append([points[i] for points in data['x']])  # this list contains 10 lists
    return signal_list, sampling_frequency  # of 38080 values

# function to plot a list of data in time domain
def time_plot(data: List, frequency: int, index: int = 0) -> None:
    time = np.linspace(0, (len(data)) / frequency, len(data)) # split time axis
    plt.plot(time, data) # plot data
    plt.title(f' Number of signal {index + 1}')
    plt.show()


# function to plot a list of fourrier transform in frequency domain
def fourier_plot(signal: List, frequency: int, index: int) -> None:
    fouriers.append(fft.fft(signal)) # calculate fourier transform of the input signal
    fourier_mag = abs(fouriers[index]) # calculate the corresponding fourier magnitude of all coeffs
    freqs.append(np.linspace(0, Fs, len(signal) // 2)) # split frequencies axis
    plt.plot(freqs[index], fourier_mag[0:len(signal) // 2]) # plot the data
    plt.title(f'Fourrier of signal: {index + 1}')
    plt.xlabel('frequency in Hz')
    plt.ylabel('Fourier magnitude ')
    plt.show()

signal_list, Fs = data_formatting(r'voice_data.mat')  # extract formatted signal list
# and sampling frequency
i = 0 # index iterator
# plot all signals in time domain
for signal in signal_list:
    time_plot(signal, Fs, index=i)  # plot each signal
    i += 1

fouriers = []  # initialize fourier list
freqs = []  # initialize frequencies list
i = 0 # index iterator
# plot all fourier transforms in frequency domain
for signal in signal_list:
    fourier_plot(signal, Fs, index=i)
    i += 1

