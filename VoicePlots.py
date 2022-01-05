""" Ploting functions
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import scipy.fft

# plot signal in time domain

def time_plot(data: List, frequency: int):
    """
    :param data: data points
    :param frequency: samping frequency
    :return:
    """
    data_points_size = len(data) # get signal size
    # split x axis in voice-1 points
    time = np.linspace(0, data_points_size / frequency, data_points_size)
    # points have 1/Fs distance each other
    # create subplots and create the given diagramms
    fig, ((axs2, axs4),(axs3, axs1)) = plt.subplots(2, 2)
    fig.suptitle('Time domain and sample domain plots') # add a title
    axs1.plot(data / data_points_size)
    axs1.label_outer()
    axs1.set_xlabel('No of sample') # add a label for x
    axs2.set_ylabel('Voice amplitude')  # add a label for y
    axs2.plot(time, data / data_points_size)  # plot in seconds
    axs3.plot((10**3)*time, data / data_points_size)  # plot in milliseconds
    axs3.set_ylabel('Voice Amplitude')  # add a label for y
    axs3.set_xlabel("Time") # add a label for x
    fig.delaxes(axs4)
    fig.show()

def fourier_plot(data: List, frequency: int):
    """
    plots the fourier transform
    :param data: data points
    :param frequency:  samping frequency
    :return:
    """
    number_of_samples = len(data)  # get data size
    data = data.flatten()  # get appropriate input
    # Fourier transform
    fouriervalues = scipy.fft.fft(data) / number_of_samples  # calculate fourier transform
    frequencypoints = np.linspace(0, frequency, number_of_samples//2)  # split frequencies axis
    # plot the fourier for non negative frequencies (first half of signal)
    plt.plot(frequencypoints, abs(fouriervalues[0:number_of_samples // 2]))
    plt.title("FFT of the signal") # add a title
    plt.xlabel('Frequency') # add a label for x
    plt.ylabel('Power of Frequency')  # add a label for y
    plt.show()
    # Vocals recorded with the following order e\ a\ o\  ii\
    # It seems that a and o are very close, but magnitude and frequency of e is significant lower
    # Also i has very high frequency but too low magnitude

# function to plot a spectrogramm

def spectrogram_plot(data: List[List], frequency: int) -> None:
    """
    plots  the spectrogramm
    :param data: data points
    :param frequency: sampling frequency
    :return:
    """
    data = data.flatten()  # take the signal data
    freq, time, stft = signal.spectrogram(data, frequency, mode='complex')  # extract frequencies,
    # time and stfourrier
    plt.pcolormesh(time, freq, abs(stft), cmap='magma', shading='gouraud')  # plot the spectrogramm
    plt.title('Spectrogram using STFT amplitude')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [seconds]')
    plt.colorbar()
    plt.show()
