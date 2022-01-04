"""
Import typing,  scipy
"""
from typing import List, Tuple
from scipy.io import loadmat

# function to reformat data
def data_formatting(data_path: str) -> Tuple[List, int]:
    """
    Parameters:
        data_path: str
        the path of file to format
    Returns:
        a tuple of signals and the sampling frequency
    """
    data = loadmat(data_path) # load data from path
    sampling_frequency = data['Fs'][0][0] # extract sampling frequency
    list_signal = []  # initialize signal list
    for j in range(len(data['x'][0])): # reformat data
        list_signal.append([points[j] for points in data['x']])  # this list contains 10 lists
    return list_signal, sampling_frequency  # of 38080 values
