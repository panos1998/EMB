import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

Fs = 8000  # Sampling frequency
duration = 5  # Recording duration in seconds
voice = sd.rec(frames=duration * Fs, samplerate=Fs, channels=1, dtype='int16')  # Capture the voice
# frames indicate  indirectly the duration of record, dtype is 16 bits per sample.
sd.wait()  # close after recording finish
time = np.linspace(0, len(voice - 1) / Fs, len(voice - 1))  # split x axis in voice-1 points
print(voice)  # points have 1/Fs distance each other
plt.plot(time, voice)  # plot in seconds
plt.title("Seconds")
plt.xlabel("Seconds")
plt.ylabel("Voice amplitude")
plt.show()
plt.plot((10**3)*time, voice)  # plot in milliseconds
plt.title("Milliseconds")
plt.xlabel("Milliseconds")
plt.ylabel("Voice amplitude")
plt.show()
