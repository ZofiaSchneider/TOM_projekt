from skimage import io
from skimage.transform import resize
from skimage import color, morphology
import os.path
from region_growing_local import region_growing_local
from preprocessing import preprocessing
from get_new_seeds import get_new_seeds
from save_to_png import save_to_png
import numpy as np
from imageio import imwrite

def find_and_save_kidneys(number, seed, colour, image_path, mode ='up'):
    """
    This function performs a region growing on the image starting from seeds 
    given as arguments. Then it creates a mask which is overlayed on an image.
    The image with the mask is then saved as a .png file. The function 
    processes all images in the directory starting from the image of number 
    given as an argument.
    
    Arguments:
    number - number of the first image
    seed - array of seed from which region growing should be started
    colour - colour to which the pixels should be compared in region growing
    image_path - path of an image
    mode - mode of function. It determines whether the number of processed 
    images should be incremented or decremented
    """
    
    n = number
    
    if mode == 'up':
        i = 1
    elif mode =='down':
        i = -1
    
    number_of_pixels = 10
    
    lista = os.listdir(image_path)
    number_of_images = int(len(lista))
    print(number_of_images)
    
    while(0 <= n < number_of_images):
        n += i
        path = image_path+'\\'+str(n).zfill(5)+'.png'
        
        if not os.path.exists(path):
            pass
        elif number_of_pixels <= 2:
            image_rgb = io.imread(path)
            imwrite("segm_" + image_path + "\\" + str(n).zfill(5) + "_our.png",image_rgb)
        elif not seed:
            break
        else:
            print(path)
            image_rgb = io.imread(path)
            image  = color.rgb2gray(image_rgb)
            image_clear, crop = preprocessing(image)
            image_rectangle = np.zeros((512, 512))
            image_rectangle[200:450,80:231] = 1 
            image_rectangle[200:450,280:431] = 1
            kidneys_areas = image_rectangle*image_clear
            region2 = region_growing_local(kidneys_areas,seed,0.17,0.03,colour)
            mask = morphology.remove_small_holes(region2,10000)
            seed = get_new_seeds(region2)
            number_of_pixels = np.count_nonzero(mask > 0)
            height = crop[3]-crop[2]
            width = crop[1]-crop[0]
            mask = resize(mask, (width,height))
            real_mask = np.zeros(image.shape)
            real_mask[crop[0]:crop[1],crop[2]:crop[3]] = mask

            save_to_png(image_rgb, real_mask, n, image_path)