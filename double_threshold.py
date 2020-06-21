from otsu_threshold import otsu_threshold 
import numpy as np

def double_threshold(image):
    """
    This function proceeds a double threshold algorithm on the image. 
    The thresholds are calculated using Otsu method.
    
    Arguments:
    image - an image to be processed
    
    Returns:
    tab - an thresholded image
    """
    upper = otsu_threshold(image[270:420,100:200])
    lower = upper/1.05
    tab = np.where(image>lower,0.5,0)
    tab = np.where(image>upper,1,tab)
    return tab