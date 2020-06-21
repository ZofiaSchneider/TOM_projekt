from starter_code.visualize import visualize
import numpy as np
from skimage import io, morphology, color
from pathlib import Path
from find_image_with_kidneys import find_image_with_kidneys
from region_growing_local import region_growing_local
from get_seed import get_seed
from preprocessing import preprocessing
from find_and_save_kidneys import find_and_save_kidneys
from save_to_png import save_to_png
import re
from skimage.transform import resize
from get_new_seeds import get_new_seeds

case_num = input("Please enter a case number:\n")

data_path = "case_" + case_num.zfill(5)
image_path = "case" + case_num

out_path = Path(image_path)
if not out_path.exists():
    visualize(data_path, image_path,t_color=[0,255,0]) #konwersja danych z repozytorium do obrazów .png

image,name,colour = find_image_with_kidneys(image_path+'/*[0-9].png')

image_rgb = io.imread(name)
image = (color.rgb2gray(image_rgb))

p = '[\d]+[\d]+[\d]+[\d]+[\d]'
if re.search(p,name) is not None:
    for catch in re.finditer(p,name):
        number=int(catch[0])
            
image_clear,crop = preprocessing(image)
image_rectangle = np.zeros((512, 512))
image_rectangle[200:450,80:231] = 1 
image_rectangle[200:450,280:431] = 1
kidneys_areas = image_rectangle*image_clear
seed = get_seed(kidneys_areas,colour,bottom = 0.04, top = 0.04, r=10)

region = region_growing_local(kidneys_areas,seed,0.15,0.05,colour)
mask = morphology.remove_small_holes(region,10000)
nerki = mask*image_clear

height = crop[3]-crop[2]
width = crop[1]-crop[0]
seed = get_new_seeds(region)
mask = resize(mask, (width,height))
real_mask = np.zeros(image.shape)
real_mask[crop[0]:crop[1],crop[2]:crop[3]] = mask

save_to_png(image_rgb, real_mask, number , image_path)

find_and_save_kidneys(number,seed,colour,image_path,mode='down')
find_and_save_kidneys(number,seed,colour,image_path,mode='up')