import cv2 
import os
import numpy as np
import glob 
from skimage.filters import gaussian
from skimage import img_as_ubyte
from skimage import img_as_ubyte

#The uploaded image
img_get = cv2.imread('1-r.jpg')

#percent by which the image is resized
scale_percent = 50

#calculate the 50 percent of original dimensions
width = int(img_get.shape[1] * scale_percent / 100)
height = int(img_get.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(img_get, dsize)
img_list= []
SIZE = 512
path = 'img_base_dir'
for images in glob.glob(path):
    
    #if images.endswith('.jpg') or images.endswith('.jpeg') or images.endswith('.png'):
    print(images)
    img_dir = cv2.imread(images,0)
    #img_dir = cv2.resize(img_dir,(SIZE, SIZE))
    img_list.append(img_dir)

    img_list = np.array(img_list)
      
    #Process each images : convert the images from BGR to RBG 
    img_num = 1
    for images in range(img_list.shape[0]):
        input_img = img_list[images]
        smooth_image = img_as_ubyte(gaussian(img_dir,sigma=5,mode='constant',cval=0.0))
        cv2.imwrite("saved_file"+str(img_num) + ".jpg",smooth_image)
        img_num+=1

   
    

cv2.imshow('1-r.jpg',output) 
cv2.waitKey(0)
cv2.destroyAllWindows()
