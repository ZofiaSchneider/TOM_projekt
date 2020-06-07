from starter_code.visualize import visualize
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage.transform import resize
import glob
from skimage import color

from histogram_equalize import histogram_equalize
from get_binary_image import get_binary_image
from gaussian_smoothing import gaussian_smoothing
from otsu_threshold import otsu_threshold
from cut_image import cut_image
from pathlib import Path

out_path = Path("case13")
if not out_path.exists():
    visualize("case_00013", "case13",t_color=[0,255,0]) #konwersja danych z repozytorium do obrazów .png
  
for name in glob.glob('case13/*[0-9].png'):
    print(name)
    image  = (color.rgb2gray(io.imread(name)))
    th = otsu_threshold(image)
    mask = get_binary_image(image, th, 'upper')
    mask2 = gaussian_smoothing(mask, sigma = 10, size = 20)
    mask2_resized = resize(mask2, (512, 512))
    th2 = otsu_threshold(mask2_resized)
    mask3 = get_binary_image(mask2_resized, th2, 'upper')
    image_new = mask3*image
    image_cropped = cut_image(image_new)
    image_clear = histogram_equalize(skimage.transform.resize(image_cropped, (512, 512)))
                                     
    image_rectangle = np.zeros((512, 512))
    image_rectangle[250:450,80:231] = 1 
    image_rectangle[250:450,280:431] = 1
    kidneys_areas = image_rectangle*image_clear

    th3= otsu_threshold(kidneys_areas)
    kidneys_binary = get_binary_image(kidneys_areas, th3+0.48, 'upper') & ~get_binary_image(kidneys_areas, th3+0.59, 'upper')
    
    plt.figure()
    plt.subplot(2,3,1)
    plt.imshow(image, cmap='gray')
    plt.subplot(2,3,2)
    plt.imshow(image_cropped, cmap='gray')
    plt.subplot(2,3,3)
    plt.imshow(image_clear, cmap='gray')
    plt.subplot(2,2,3)
    plt.imshow(kidneys_areas,cmap='gray')
    plt.subplot(2,2,4)
    plt.imshow(kidneys_binary, cmap='gray')