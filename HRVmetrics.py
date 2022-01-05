"""
Import ecgdetectors, hrv, numpy, matplotlib scipy
"""
import matplotlib.pyplot as plt
import scipy.io
from ecgdetectors import Detectors
import hrv
dictdata = scipy.io.loadmat(r"C:\Users\Πανος\Documents\GitHub\EMB\MLII\17 PR\107m (0).mat")
data = dictdata['val'][0]
FREQ = 360  # Sampling Frequency in Hz
detectors = Detectors(FREQ)
rpeaks = detectors.pan_tompkins_detector(data)
hr = hrv.HRV(360)  # Initialize a hrv.HRV class with sampling frequency
heart_rate_variability = hr.HR(rr_samples=rpeaks)
print(heart_rate_variability)
plt.figure()
plt.plot(data)
plt.plot(rpeaks, data[rpeaks], 'ro')
plt.show()
plt.title('Heart rate variability')
plt.ylabel('Interval Seconds')
plt.xlabel('Sample')
plt.plot(heart_rate_variability)
plt.show()
