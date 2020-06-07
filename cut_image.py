def cut_image(image):
    lf=0  #sprawdzają, czy znaleziono już brzeg
    rf=0
    uf=0
    df=0
    for x in range(512):
        for y in range(512):
            if image[x,y] != 0 and lf==0:
                left = x
                lf=1
                
            if image[511-x,y] !=0 and rf==0:
                right = 511-x
                rf=1
            if lf==1 and rf==1:
                break
    for y in range(512):
        for x in range(512):
            if image[x,y] != 0 and uf==0:
                up = y
                uf=1
            if image[x,511-y] != 0 and df==0:
                down = 511-y
                df=1
            if uf==1 and df==1:
                break
    cut = image[left:right,up:down]
    print(left,right,up,down)
    return cut