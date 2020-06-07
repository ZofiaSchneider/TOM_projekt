import numpy as np
from scipy import signal

def gaussian_smoothing(image, sigma, size):
    center = size/2
    kernel = np.zeros((size,size))
    for i in range(size):
       for j in range(size):
          diff = np.sqrt((i-center)**2+(j-center)**2)
          kernel[i,j] = (1/(2*3.14*sigma))*np.exp(-(diff**2)/(2*sigma**2))
    return signal.convolve2d(image, kernel/np.sum(kernel))