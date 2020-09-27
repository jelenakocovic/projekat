import numpy as np
import matplotlib.pyplot as plt

f1 = 1.8
f2 = 2.6

#try tDelay = .02002 and tDelay = .0205

tDelay = 0.9 #seconds
samples = 1024
tStart = -5
tEnd = 5

samplePeriod = (tEnd -tStart) / (samples)
print("\n The sampling period is %f seconds" % tDelay)

tDelayInSamples = (tDelay / samplePeriod)
print("The time delay in samples is %f samples" % tDelayInSamples)

timeList = (np.linspace(tStart, tEnd, samples))

waveForm = np.sinc(2 * np.pi * f1 * timeList) + np.sinc(2 * np.pi * f2 * timeList)

fftOut = np.fft.fft(waveForm)

N = fftOut.shape[0]
k = np.linspace(0, N-1, N)

phaseShiftFunction = np.exp((-2 * np.pi * 1j * k * tDelayInSamples ) / (N))

fftWithDelay = np.multiply(fftOut, phaseShiftFunction)

waveForm2 = np.fft.ifft(fftWithDelay)

plots = 1
plt.subplot(plots, 1, 1)
plt.plot(waveForm)
plt.plot(waveForm2)
plt.show()
