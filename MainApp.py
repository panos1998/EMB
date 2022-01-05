"""
import soundevice and VoicePlots class
"""
import VoicePlots as vplt
import sounddevice as sd

FREQ = 8000  # Sampling frequency
duration = 5  # Recording duration in seconds
# Capture the voice
voice = sd.rec(frames=duration * FREQ, blocking=True, samplerate=FREQ, channels=1, dtype='int16')
# frames indicate  indirectly the duration of record, dtype is 16 bits per sample.
vplt.time_plot(voice, FREQ)
vplt.fourier_plot(voice, FREQ)
vplt.spectrogram_plot(voice, FREQ)
