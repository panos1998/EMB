import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

Fs = 8000
duration = 5
voice = sd.rec(frames=duration * Fs,samplerate=Fs,channels=1,dtype='int16')
sd.wait()
time = np.linspace(0, len(voice - 1) / Fs, len(voice - 1))
print(time, len(time))
plt.plot(voice)
plt.show()
plt.plot(time, voice)
plt.show()