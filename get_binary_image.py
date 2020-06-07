def get_binary_image(img, threshold, tryb ='upper'):
    if tryb == 'upper':
        return img > threshold
    elif tryb == 'lower':
        return img < threshold