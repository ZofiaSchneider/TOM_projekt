import numpy as np
from scipy.ndimage import measurements as m 

def get_new_seeds(image):
    """
    This function calculates the coordinates of seeds for region growing as 
    centers of mass of two regions in the image.
    
    Arguments:
    image - image from which the seeds coordinates are calculated
    
    Returns:
    seed - array containing coordinates of new seeds
    """
    image_rectangle1 = np.zeros((512, 512))
    image_rectangle2 = np.zeros((512, 512))
    image_rectangle1[200:450,80:231] = 1 
    image_rectangle2[200:450,280:431] = 1
    nera1 = image_rectangle1*image
    nera2 = image_rectangle2*image
    
    x1 = m.center_of_mass(nera1)[0]
    y1 = m.center_of_mass(nera1)[1]
    x2 = m.center_of_mass(nera2)[0]
    y2 = m.center_of_mass(nera2)[1]
    
    if not np.isnan(x1) and not np.isnan(x2):
            
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        
        if image[x1,y1+20] == 0:
            while image[x1,y1+20] == 0:
                y1 -= 1
                
        if image[x2,y2-20] == 0:
            while image[x2,y2-20] == 0:
                y2 += 1
                
        seed =  [(x1,y1),(x2,y2)]
    
    elif np.isnan(x1) and not np.isnan(x2):
        
        x2 = int(x2)
        y2 = int(y2)
        
        if image[x2,y2-20] == 0:
            while image[x2,y2-20] == 0:
                y2 += 1
                
        seed = [(x2,y2)]
        
    elif not np.isnan(x1) and np.isnan(x2):
        
        x1 = int(x1)
        y1 = int(y1)
        
        if image[x1,y1+20] == 0:
            while image[x1,y1+20] == 0:
                y1 -= 1
                
        seed = [(x1,y1)]
        
    elif np.isnan(x1) and np.isnan(x2):
                        
        seed = []
        
    return seed 
        
        
        
    
        
    