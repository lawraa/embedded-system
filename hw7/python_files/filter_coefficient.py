import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# FIR filter coefficients
fir_coeffs = np.array([
    -0.0018225230, -0.0015879294, 0.0000000000, +0.0036977508, +0.0080754303,
    +0.0085302217, -0.0000000000, -0.0173976984, -0.0341458607, -0.0333591565,
    +0.0000000000, +0.0676308395, +0.1522061835, +0.2229246956, +0.2504960933,
    +0.2229246956, +0.1522061835, +0.0676308395, +0.0000000000, -0.0333591565,
    -0.0341458607, -0.0173976984, -0.0000000000, +0.0085302217, +0.0080754303,
    +0.0036977508, +0.0000000000, -0.0015879294, -0.0018225230
])

# Plot the FIR filter coefficients
plt.figure(figsize=(10, 4))
plt.stem(fir_coeffs)
plt.title("FIR Filter Coefficients")
plt.xlabel("Coefficient Index")
plt.ylabel("Coefficient Value")
plt.grid(True)
plt.tight_layout()
plt.show()

# Compute and plot the frequency response of the filter
w, h = freqz(fir_coeffs, worN=8000)
plt.figure(figsize=(10, 4))
plt.plot(0.5 * 16000 * w / np.pi, np.abs(h), 'b') 
plt.title("Frequency Response of the FIR Filter")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain")
plt.grid(True)
plt.tight_layout()
plt.show()
