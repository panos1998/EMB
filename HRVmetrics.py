import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from ecgdetectors import Detectors
import hrv
dict_data = scipy.io.loadmat(r"C:\Users\Πανος\Documents\GitHub\EMB\MLII\17 PR\107m (0).mat")
data = dict_data['val'][0]
Fs = 360  # Sampling Frequency in Hz
detectors = Detectors(Fs)
r_peaks = detectors.pan_tompkins_detector(data)

print(r_peaks)
Hr = hrv.HRV(360)  # Initialize a hrv.HRV class with sampling frequency
heart_rate_variability = Hr.HR(rr_samples=r_peaks)
print(heart_rate_variability)
plt.figure()
plt.plot(data)
plt.plot(r_peaks, data[r_peaks], 'ro')
plt.show()
plt.title('Heart rate variability')
plt.ylabel('Interval Seconds')
plt.xlabel('Sample')
plt.plot(heart_rate_variability)
plt.show()