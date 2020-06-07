from skimage import color
from skimage import exposure
import numpy as np

def histogram_equalize(img):
    img = color.rgb2gray(img)
    img_cdf, bin_centers = exposure.cumulative_distribution(img)
    return np.interp(img, bin_centers, img_cdf)