"""
Import typing, numpy, matplotlib
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt

def time_plot(data: List, frequency: int, index: int = 0) -> None:
    """
    a function to plot data in time
    :param data: the list with data to plot
    :param frequency: the samping frequency value
    :param index: iterator for each signal
    :return: nothing
    """
    time = np.linspace(0, (len(data)) / frequency, len(data)) # split time axis
    plt.plot(time, data) # plot data
    plt.title(f' Number of signal {index + 1}')
    plt.show()