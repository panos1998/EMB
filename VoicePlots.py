import matplotlib.pyplot as plt
import numpy as np
import scipy.fft
from scipy import signal

# plot signal in time domain

def time_plot(data, frequency):
    N = len(data) # get signal size
    time = np.linspace(0, N / frequency, N)  # split x axis in voice-1 points
    # points have 1/Fs distance each other
    fig, ((axs2, axs4),(axs3, axs1)) = plt.subplots(2, 2)  # create subplots and create the given diagramms
    fig.suptitle('Time domain and sample domain plots')
    axs1.plot(data / N)
    axs1.label_outer()
    axs1.set_xlabel('No of sample')
    axs2.set_ylabel('Voice amplitude')
    axs2.plot(time, data / N)  # plot in seconds
    axs3.plot((10**3)*time, data / N)  # plot in milliseconds
    axs3.set_ylabel('Voice Amplitude')
    axs3.set_xlabel("Time")
    fig.delaxes(axs4)
    fig.show()

def fourier_plot(data, frequency):
    N = len(data)  # get data size
    data = data.flatten()  # get appropriate input
    # Fourier transform
    F = scipy.fft.fft(data) / N  # calculate fourier transform
    f = np.linspace(0, frequency, N//2)  # split frequencies axis
    plt.plot(f, abs(F[0:N // 2]))  # plot the fourier for non negative frequencies (first half of signal)
    plt.title("FFT of the signal")
    plt.xlabel('Frequency')
    plt.ylabel('Power of Frequency')
    plt.show()
    # Vocals recorded with the following order e\ a\ o\  ii\
    # It seems that a and o are very close, but magnitude and frequency of e is significant lower
    # Also i has very high frequency but too low magnitude

# function to plot a spectrogramm
def spectrogram_plot(data, frequency):
    data = data.flatten()  # take the signal data
    freq, t, stft = signal.spectrogram(data, frequency, mode='complex')  # extract frequencies,
    # time and stfourrier
    plt.pcolormesh(t, freq, abs(stft), cmap='magma', shading='gouraud')  # plot the spectrogramm
    plt.title('Spectrogram using STFT amplitude')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [seconds]')
    plt.colorbar()
    plt.show()
