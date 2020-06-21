import numpy as np

def get_seed(image, colour, bottom=0.05, top=0.03, r=15):
    """
    This function finds coordinates of the seeds for region growing.
    
    Argumetns:
    """
    seed = []
    for i in range(1,image.shape[0]-1):
        for j in range(1,image.shape[1]-1):
            mean=np.mean(image[i-r:i+r,j-r:j+r])
            if colour - bottom < mean < colour + top:
                seed.append((i,j))
    return seed