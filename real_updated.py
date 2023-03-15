import cv2 
import os
import numpy as np

#The uploaded image
img_get = cv2.imread('1-r.jpg',cv2.IMREAD_UNCHANGED)

#percent by which the image is resized
scale_percent = 50

#calculate the 50 percent of original dimensions
width = int(img_get.shape[1] * scale_percent / 100)
height = int(img_get.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(img_get, dsize)

for images in os.listdir('img_base_dir'):
    if images.endswith('.jpg') or images.endswith('.jpeg') or images.endswith('.png'):
      print(images)
      cv2.imshow('big_er',images)
      

      """  if images.size != img_get:
            #resize all the images
            path = 'img_base_dir'
            resize_img = cv2.imread(os.path(path))
            img_dir = cv2.imread(os.path.join(path, images))

            scale_percent = 50
            width = int(img_get.shape[1] * scale_percent / 100)
            height = int(img_get.shape[0] * scale_percent / 100)

            dsiz_dir = (width, height)
            print("loop throught the images ") """
        


            
            
    

cv2.imshow('1-r.jpg',output) 
cv2.waitKey(0)
cv2.destroyAllWindows()
