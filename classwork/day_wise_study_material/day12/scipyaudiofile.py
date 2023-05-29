# -*- coding: utf-8 -*-
"""
Created on Tue May 23 13:25:34 2023

@author: anilk
"""

from scipy.io.wavfile import read #import the required function from the module
import numpy as np
#return rate of sample and the actual data
samplerate, data = read(r"sample-12s.wav")

print(samplerate) #echo samplerate
22050

print(data) #echo data -> note that the data is a single dimensional array
#array([   3,    7,    0, ...,  -12, -427, -227], dtype=int16)
#Compute the duration and the time vector of the audio sample from the 
#sample rate
duration = len(data)/samplerate
time = np.arange(0,duration,1/samplerate) #time vector
#Plot the time-series data using matplotlib package
import matplotlib.pyplot as plt
import numpy as np
plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('sample-12s.wav')
plt.show()
