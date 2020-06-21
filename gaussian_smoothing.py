import numpy as np
from scipy import signal

def gaussian_smoothing(image, sigma, size):
    """
    This function filters an image using Gaussian filter.
    
    ArgumentsL
    image - image to filter
    sigma - sigma parameter of Gaussian filter
    size - size of a filter
    
    Returns:
    im_f - filtered image
    """
    center = size/2
    kernel = np.zeros((size,size))
    for i in range(size):
       for j in range(size):
          diff = np.sqrt((i-center)**2+(j-center)**2)
          kernel[i,j] = (1/(2*3.14*sigma))*np.exp(-(diff**2)/(2*sigma**2))
    im_f = signal.convolve2d(image, kernel/np.sum(kernel))
    return im_f