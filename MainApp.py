"""
import soundevice and VoicePlots class
"""
import VoicePlots as vplt
import sounddevice as sd

Fs = 8000  # Sampling frequency
duration = 5  # Recording duration in seconds
# Capture the voice
voice = sd.rec(frames=duration * Fs, blocking=True, samplerate=Fs, channels=1, dtype='int16')
# frames indicate  indirectly the duration of record, dtype is 16 bits per sample.
vplt.time_plot(voice, Fs)
vplt.fourier_plot(voice, Fs)
vplt.spectrogram_plot(voice, Fs)
