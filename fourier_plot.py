"""
Import typing, numpy, matplotlib scipy
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

fouriertransforms = []  # initialize fourier list
frequencylist = []  # initialize frequencies list
# function to plot a list of fourrier transform in frequency domain
def fourier_plot(signal_data: List, frequency: int, index: int) -> None:
    """
    :param signal_data: the signal data
    :param frequency: the sampling frequency
    :param index: iterator for each signal
    :return:
    """
    # calculate fourier transform of the input signal
    fouriertransforms.append(fft.fft(signal_data))
    # calculate the corresponding fourier magnitude
    fourier_mag = abs(fouriertransforms[index])  # of all coeffs
    frequencylist.append(np.linspace(0, frequency, len(signal_data) // 2)) # split frequencies axis
    plt.plot(frequencylist[index], fourier_mag[0:len(signal_data) // 2]) # plot the data
    plt.title(f'Fourrier of signal: {index + 1}')
    plt.xlabel('frequency in Hz')
    plt.ylabel('Fourier magnitude ')
    plt.show()