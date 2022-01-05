"""
Import typing, numpy, matplotlib scipy
"""
from fourier_plot import fourier_plot
from data_processing import data_formatting
from time_plot import time_plot
# extract formatted signal list
data, FREQUENCY = data_formatting(r'voice_data.mat')
# and sampling frequency
i = 0 # index iterator
# plot all signals in time domain
for signal in data:
    time_plot(signal, FREQUENCY, index=i)  # plot each signal
    i += 1

i = 0 # index iterator
# plot all fourier transforms in frequency domain
for signal in data:
    fourier_plot(signal, FREQUENCY, index=i)
    i += 1
