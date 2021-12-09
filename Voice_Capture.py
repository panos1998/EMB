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
time = np.linspace(0, len(voice - 1) / Fs, len(voice - 1))  # split x axis in voice-1 points
# points have 1/Fs distance each other
plt.plot(voice / len(voice))
plt.ylabel('Voice amplitude')
plt.xlabel('No of sample')
plt.title("Voice Signal with respect to sample number")
plt.show()
plt.plot(time, voice / len(voice))  # plot in seconds
plt.title("Voice Signal")
plt.xlabel("Time [seconds]")
plt.ylabel("Voice amplitude")
plt.show()
plt.plot((10**3)*time, voice / len(voice))  # plot in milliseconds
plt.title("Voice Signal")
plt.xlabel("Time [milliseconds]")
plt.ylabel("Voice amplitude")
plt.show()

N = len(voice)
# Fourier transform
F = scipy.fft.fft(voice) / N
#f = np.linspace(0, Fs - Fs / N, N)
f = fft.fftfreq(n=N, d=1 / Fs)[:N // 2]
#f = np.linspace(0, 4000, N//2)
plt.plot(f, abs(F[0:N // 2]))
plt.title("FFT of the signal")
plt.xlabel('Frequency')
plt.ylabel('Power of Frequency')
plt.show()
# Vocals recorded with the following order e\ a\ o\  ii\
# It seems that a and o are very close, but magnitude and frequency of e is significant lower
# Also i has very high frequency but too low magnitude
Voice = voice.flatten()  # formatting Voice 2-D array to numpy 1-D array
print(Voice)
freq, t, stft = signal.spectrogram(Voice, Fs, mode='complex')
#Sxx, freq, t = plt.specgram(Voice, Fs=Fs, mode='magnitude')
print(stft)
print(freq)
print(t)
plt.pcolormesh(t, freq, abs(stft), shading='gouraud')
plt.title('Spectrogramm using STFT amplitude')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [seconds]')
plt.show()
