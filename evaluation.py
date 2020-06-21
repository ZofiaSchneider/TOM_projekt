from skimage import io,color,measure
from skimage import img_as_float
from skimage.measure import compare_mse as mse
import math
import os.path
import os 
import numpy as np
import csv

def evaluation(case_num):
    
    """
    This function compares 2 series of images - calculates root mean square 
    (rms) and structural similarity (ssim) between each two images. Then it 
    calculates the mean and standard deviation of rms and ssim for the whole 
    case and write it to a csv file which name is "evaluation".
    
    Arguments:
    case_num - number of case
    
    Returns:
    evaluation_array - array with rms and ssim for each pair of images
    rms_mean - mean of root mean square for all pairs od images
    rms_sd - standard deviation of root mean square for all pairs of images
    ssim_mean - mean of structural similarity fo all pairs of images
    ssim_sd - standard deviation of structural similiarity for all pairs of images
    
    """
    directory_path = "segm_case" + case_num
    evaluation_array = []
    lista = os.listdir(directory_path) # dir is your directory path
    number_of_images = int(len(lista)/2)
    print(number_of_images)
    for n in range(0,number_of_images):
    
        path_kits = directory_path+'\\'+str(n).zfill(5)+'_kits.png'
        path_our = directory_path+'\\'+str(n).zfill(5)+'_our.png'
        
        if (not os.path.exists(path_kits) or not os.path.exists(path_our)):
            pass
        
        img_kits = color.rgb2gray(io.imread(path_kits))
        img_our = color.rgb2gray(io.imread(path_our))
        
        def rmsdiff(im1, im2):
            return math.sqrt(mse(img_as_float(im1), img_as_float(im2)))
        
        #root mean square
        rms = rmsdiff(img_kits,img_our)
        
        #structural similarity
        ssim1,grad1,ssim1_img = measure.compare_ssim(img_kits,img_our,gradient=True,full=True)
        evaluation_array.append([n,rms,ssim1])
        
    rms = []
    ssim = []
    
    for ev in evaluation_array:
        rms.append(ev[1])
        ssim.append(ev[2])
        
    rms_mean = np.mean(rms)
    rms_sd = np.std(rms)
    ssim_mean = np.mean(ssim)
    ssim_sd = np.std(ssim)
        
    e = [case_num,rms_mean,rms_sd,ssim_mean,ssim_sd]
    
    if not os.path.exists("evaluation.csv"):
        with open('evaluation.csv', 'a',) as myfile:
            wr = csv.writer(myfile, delimiter=',',  quoting=csv.QUOTE_NONE)
            wr.writerow(["Case","RMS mean","RMS sd", "SSIM mean","SSIM sd"])
    with open('evaluation.csv', 'a',) as myfile:
        wr = csv.writer(myfile, delimiter=',',  quoting=csv.QUOTE_NONE)
        wr.writerow(e)

    return evaluation_array,rms_mean,rms_sd,ssim_mean,ssim_sd      