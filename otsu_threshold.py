import numpy as np

def otsu_threshold(image):
    
    hist, bin_e = np.histogram(image*256, bins=256)
    p = 1.0*hist/np.sum(hist)    
    sigma_B_max = -999
    threshold = -1
    for t in range(1,255):
        om1 = np.sum(p[:t])
        om2 = np.sum(p[t:])
        mi1 = np.sum(np.array([i for i in range(t)])*p[:t])/om1
        mi2 = np.sum(np.array([i for i in range(t,256)])*p[t:])/om2
        sigma_B = om1*om2*np.power(mi2-mi1,2)
#        if t==1:
#            sigma_B_max = sigma_B
        if sigma_B > sigma_B_max:
            sigma_B_max = sigma_B
            threshold = t/256
    return threshold