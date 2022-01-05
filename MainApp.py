"""
import soundevice and VoicePlots class
"""
import VoicePlots as vplt
import sounddevice as sd

FREQ = 8000  # Sampling frequency
DURATION = 5  # Recording duration in seconds
# Capture the voice

points = sd.rec(frames=DURATION * FREQ, blocking=True, samplerate=FREQ, channels=1, dtype='int16')

# frames indicate  indirectly the duration of record, dtype is 16 bits per sample.
vplt.time_plot(points, FREQ) # plot signal in time domain
vplt.fourier_plot(points, FREQ) # plot fourier in freq domain
vplt.spectrogram_plot(points, FREQ) # plot spectrogramm
