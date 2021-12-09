import matplotlib.pyplot as plt
import numpy as np
import scipy.fft
import sounddevice as sd
from scipy import signal, fft

Fs = 8000  # Sampling frequency
duration = 5  # Recording duration in seconds
voice = sd.rec(frames=duration * Fs, samplerate=Fs, channels=1, dtype='int16')  # Capture the voice
# frames indicate  indirectly the duration of record, dtype is 16 bits per sample.
sd.wait()  # close after recording finish


def time_plot(data, frequency):
    N = len(data)
    time = np.linspace(0, N / frequency, N)  # split x axis in voice-1 points
    # points have 1/Fs distance each other
    plt.plot(data / N)
    plt.ylabel('Voice amplitude')
    plt.xlabel('No of sample')
    plt.title("Voice Signal with respect to sample number")
    plt.show()
    plt.plot(time, data / N)  # plot in seconds
    plt.title("Voice Signal")
    plt.xlabel("Time [seconds]")
    plt.ylabel("Voice amplitude")
    plt.show()
    plt.plot((10**3)*time, voice / N)  # plot in milliseconds
    plt.title("Voice Signal")
    plt.xlabel("Time [milliseconds]")
    plt.ylabel("Voice amplitude")
    plt.show()


def fourier_plot(data, frequency):
    N = len(data)
    data = data.flatten()
    # Fourier transform
    F = scipy.fft.fft(data) / N
    f = np.linspace(0, frequency, N//2)
    plt.plot(f, abs(F[0:N // 2]))
    plt.title("FFT of the signal")
    plt.xlabel('Frequency')
    plt.ylabel('Power of Frequency')
    plt.show()
    # Vocals recorded with the following order e\ a\ o\  ii\
    # It seems that a and o are very close, but magnitude and frequency of e is significant lower
    # Also i has very high frequency but too low magnitude


def spectrogram_plot(data, frequency):
    data = data.flatten()
    freq, t, stft = signal.spectrogram(data, frequency, mode='complex')
    plt.pcolormesh(t, freq, abs(stft), cmap='magma', shading='gouraud')
    plt.title('Spectrogram using STFT amplitude')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [seconds]')
    plt.colorbar()
    plt.show()


time_plot(voice, Fs)
fourier_plot(voice, Fs)
spectrogram_plot(voice, Fs)
