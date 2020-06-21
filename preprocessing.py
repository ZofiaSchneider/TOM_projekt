from gaussian_smoothing import gaussian_smoothing
from otsu_threshold import otsu_threshold
from get_binary_image import get_binary_image
from cut_image import cut_image
from histogram_equalize import histogram_equalize
from skimage.transform import resize

def preprocessing(image, sigma=10, size=20):
    """
    This function realizes preprocessing on image on a few steps: smoothing,
    cropping, resizing and histogram equalization. It also removes the lines 
    of bed from CT images.
    
    Arguments:
    image - an image to preprocess
    sigma - sigma parameter of gaussian filter
    size - size of gaussian filter
    
    Returns:
    image_clear - processed image
    crop_loc - 
    """
    th = otsu_threshold(image)
    mask = get_binary_image(image, th, 'upper')
    mask2 = gaussian_smoothing(mask, sigma = 10, size = 20)
    mask2_resized = resize(mask2, (512, 512))
    th2 = otsu_threshold(mask2_resized)
    mask3 = get_binary_image(mask2_resized, th2, 'upper')
    image_new = mask3*image
    image_cropped, crop_loc = cut_image(image_new)
    image_clear = histogram_equalize(resize(image_cropped, (512, 512)))

    return image_clear, crop_loc