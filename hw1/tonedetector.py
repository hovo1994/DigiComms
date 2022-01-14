import numpy as np
from matplotlib import pyplot


sampleRate = 2**10 # number of sapmles per second

startTime = 0 # seconds
endTime = 1 # seconds

time = np.arange(startTime, endTime, 1/sampleRate) # time axis


frequency = 10 # number of oscilations per second
amplitude = 1 # peak height of sine wave
theta = 0 # aplittude of sine wave at time 0


sinewave = amplitude * np.sin(2 * np.pi * frequency * time + theta)
frequency = 40 # number of oscilations per second
amplitude = 1 # peak height of sine wave
theta = 0 # aplittude of sine wave at time 0
sinewave2 = amplitude * np.sin(2 * np.pi * frequency * time + theta)

# noise = np.random.uniform(low=0.0, high=1.0, size=(sampleRate,))
noise = np.random.rand(sampleRate)
noise = noise * 40

totalsinw = sinewave + sinewave2 + noise

pyplot.subplot(2,1,1)
pyplot.plot(time, totalsinw)

# pyplot.show()

# frequency domain plot
fftsinewave = np.fft.fft(totalsinw)
lenofft = round(len(fftsinewave)/2)
magarray = []
for binNum in range(lenofft):
    sample = fftsinewave[binNum]
    mag = np.sqrt(sample.real**2 + sample.imag**2)
    magarray.append(mag)
    print(f"{binNum}: {mag}")

freq = np.arange(0.0, sampleRate/2) # freq axis

# print(freq)

pyplot.subplot(2,1,2)
pyplot.plot(range(0, int(sampleRate/2)), magarray)
pyplot.show()


