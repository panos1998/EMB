"""
Import typing, numpy, matplotlib scipy
"""
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
from scipy.io import loadmat

# function to reformat data
def data_formatting(data_path: str) -> Tuple[List, int]:
    """
    Parameters:
        data_path: str
        the path of file to format
    Returns:
        a tuple of signals and the sampling frequency
    """
    data = loadmat(data_path) # load data from path
    sampling_frequency = data['Fs'][0][0] # extract sampling frequency
    list_signal = []  # initialize signal list
    for j in range(len(data['x'][0])): # reformat data
        list_signal.append([points[j] for points in data['x']])  # this list contains 10 lists
    return list_signal, sampling_frequency  # of 38080 values

# function to plot a list of data in time domain
def time_plot(data: List, frequency: int, index: int = 0) -> None:
    """

    :param data: the list with data to plot
    :param frequency: the samping frequency value
    :param index: iterator for each signal
    :return: nothing
    """
    time = np.linspace(0, (len(data)) / frequency, len(data)) # split time axis
    plt.plot(time, data) # plot data
    plt.title(f' Number of signal {index + 1}')
    plt.show()


# function to plot a list of fourrier transform in frequency domain
def fourier_plot(signal_data: List, frequency: int, index: int) -> None:
    """
    :param signal_data: the signal data
    :param frequency: the sampling frequency
    :param index: iterator for each signal
    :return:
    """
    # calculate fourier transform of the input signal
    fourier_transforms.append(fft.fft(signal_data))
    # calculate the corresponding fourier magnitude
    fourier_mag = abs(fourier_transforms[index])  # of all coeffs
    frequencies.append(np.linspace(0, frequency, len(signal_data) // 2)) # split frequencies axis
    plt.plot(frequencies[index], fourier_mag[0:len(signal_data) // 2]) # plot the data
    plt.title(f'Fourrier of signal: {index + 1}')
    plt.xlabel('frequency in Hz')
    plt.ylabel('Fourier magnitude ')
    plt.show()
# extract formatted signal list
signal_list, Fs = data_formatting(r'voice_data.mat')
# and sampling frequency
i = 0 # index iterator
# plot all signals in time domain
for signal in signal_list:
    time_plot(signal, Fs, index=i)  # plot each signal
    i += 1

fourier_transforms = []  # initialize fourier list
frequencies = []  # initialize frequencies list
i = 0 # index iterator
# plot all fourier transforms in frequency domain
for signal in signal_list:
    fourier_plot(signal, Fs, index=i)
    i += 1
