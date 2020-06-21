from skimage import color
from skimage import exposure
import numpy as np

def histogram_equalize(img):
    """
    This function equalizes histogram of an image.
    
    Arguments:
    img - image to have it histogram equalizes
    
    Returns:
    
    """
    img = color.rgb2gray(img)
    img_cdf, bin_centers = exposure.cumulative_distribution(img)
    np.interp(img, bin_centers, img_cdf)
    return np.interp(img, bin_centers, img_cdf)