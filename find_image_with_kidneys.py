import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import glob
from skimage import color

from scipy.signal import find_peaks_cwt
from preprocessing import preprocessing

def find_image_with_kidneys(path):
    """
    This function searches for the CT image containing kidneys. To find kidneys 
    it creates histograms of images and search for a peak in the range of 
    lightness that is typical for kidney in CT image.
    
    Arguments:
    path - path to the directory containing CT images
    
    Returns:
    image_clear - preprocessed image containing kidneys
    name - name of the found image
    colour - colour of kidneys on the found image
    """
    for name in glob.glob(path):
        image  = (color.rgb2gray(io.imread(name)))
        image_clear,c = preprocessing(image)
                                         
        image_rectangle1 = np.zeros((512, 512))
        image_rectangle2 = np.zeros((512, 512))
        image_rectangle1[200:450,80:231] = 1 
        image_rectangle2[200:450,280:431] = 1
        kidneys_areas1 = image_rectangle1*image_clear
        kidneys_areas2 = image_rectangle2*image_clear
        
        histogram1,bins1,n1 = plt.hist(kidneys_areas1.ravel(), bins=255)
        peaks1 = find_peaks_cwt(histogram1, widths = np.arange(1,20))
        
        histogram2,bins2,n2 = plt.hist(kidneys_areas2.ravel(), bins=255)
        peaks2 = find_peaks_cwt(histogram2, widths = np.arange(1,20))
        
        kidney1 = kidney2 = False
        
        for i in peaks1:
            if 245 <= i <= 252 and histogram1[i] >= 350:
                kidney1 = True
                colour = bins1[i]
                break
        
        for i in peaks2:
            if 245 <= i <= 252 and histogram2[i] >= 350:
                kidney2 = True
                break
        
        if kidney1 and kidney2:
            return image_clear,name,colour
        
  

    
    
    
    
    
    
    
    
    
    
    
    
