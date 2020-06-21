import numpy as np
from imageio import imwrite
import os
import os.path

def save_to_png(orig_im, mask, im_number, image_path):
    """
    This function overlay a mask (segmentation) on an original image and save it
    as a .png file.
    
    Arguments:
    orig_im - original image without segmentation
    mask - binary mask (segmentation)
    im_number - number of an image
    image_path - path of the original image
    """
    s = mask.shape[0]
    seg_color = np.zeros((s,s,3), dtype=np.float32)
    seg_color[:,:,0] = np.where(mask==1, 255, 0)
    alpha = 0.3
    overlayed = np.where(np.stack((mask==1, mask==1, mask==1), axis=-1), alpha*seg_color+(1-alpha)*orig_im, orig_im)
    new_path = "segm_" + image_path
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    imwrite(new_path + "\\" + str(im_number).zfill(5) + "_our.png", overlayed)