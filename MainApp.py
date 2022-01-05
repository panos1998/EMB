"""
import soundevice and VoicePlots class
"""
import VoicePlots as vplt
import sounddevice as sd

FREQUENCY = 8000  # Sampling frequency
duration = 5  # Recording duration in seconds
# Capture the voice
voice = sd.rec(frames=duration * FREQUENCY, blocking=True, samplerate=FREQUENCY, channels=1, dtype='int16')
# frames indicate  indirectly the duration of record, dtype is 16 bits per sample.
vplt.time_plot(voice, FREQUENCY)
vplt.fourier_plot(voice, FREQUENCY)
vplt.spectrogram_plot(voice, FREQUENCY)
