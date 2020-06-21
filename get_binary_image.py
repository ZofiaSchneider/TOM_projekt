def get_binary_image(img, threshold, mode ='upper'):
    """
    This function creates an binary image using thresholding.
    """
    if mode == 'upper':
        return img > threshold
    elif mode == 'lower':
        return img < threshold