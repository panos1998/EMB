"""
Import typing, numpy, matplotlib scipy
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft
fourier_data = list()  # initialize fourier list
frequencies_of_partitions = list()  # initialize frequencies list
# function to plot a list of fourrier transform in frequency domain
def fourier_plot(signal_data: List, frequency: int, index: int) -> None:
    """
    :param signal_data: the signal data
    :param frequency: the sampling frequency
    :param index: iterator for each signal
    :return:
    """
    # calculate fourier transform of the input signal
    fourier_data.append(fft.fft(signal_data))
    # calculate the corresponding fourier magnitude
    fourier_mag = abs(fourier_data[index])  # of all coeffs
    # split frequencies axis
    frequencies_of_partitions.append(np.linspace(0, frequency, len(signal_data) // 2))
    # plot the data
    plt.plot(frequencies_of_partitions[index], fourier_mag[0:len(signal_data) // 2])
    plt.title(f'Fourrier of signal: {index + 1}') # add a title
    plt.xlabel('frequency in Hz')
    plt.ylabel('Fourier magnitude ')
    plt.show() # show the plot
