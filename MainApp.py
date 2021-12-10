import VoicePlots as vplt
import sounddevice as sd


Fs = 8000  # Sampling frequency
duration = 5  # Recording duration in seconds
voice = sd.rec(frames=duration * Fs, samplerate=Fs, channels=1, dtype='int16')  # Capture the voice
# frames indicate  indirectly the duration of record, dtype is 16 bits per sample.
vplt.time_plot(voice, Fs)
vplt.fourier_plot(voice, Fs)
vplt.spectrogram_plot(voice, Fs)
