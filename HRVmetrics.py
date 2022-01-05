"""
Import ecgdetectors, hrv, numpy, matplotlib scipy
"""
import matplotlib.pyplot as plt
import scipy.io
from ecgdetectors import Detectors
import hrv
matrixdata = scipy.io.loadmat(r"C:\Users\Πανος\Documents\GitHub\EMB\MLII\17 PR\107m (0).mat")
data = matrixdata['val'][0]
FREQ = 360  # Sampling Frequency in Hz
detector = Detectors(FREQ)
rpeaks = detector.pan_tompkins_detector(data)
hr = hrv.HRV(360)  # Initialize a hrv.HRV class with sampling frequency
heartratevariability = hr.HR(rr_samples=rpeaks)
print(heartratevariability)
plt.figure()
plt.plot(data)
plt.plot(rpeaks, data[rpeaks], 'ro')
plt.show()
plt.title('Heart rate variability')
plt.ylabel('Interval Seconds')
plt.xlabel('Sample')
plt.plot(heartratevariability)
plt.show()
