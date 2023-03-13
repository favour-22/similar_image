import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim

#Load the two images to be compared 
img1 = cv2.imread('images.jpg')
img2 = cv2.imread('2img.jpg')

#Checking if the images have the same dimensions
if img1.shape != img2.shape:
    width = max(img1.shape[1],img2.shape[1])
    height =max(img2.shape[0],img2.shape[0])
    dim = (width,height)
    img1 =cv2.resize(img1,(500,500))
    img2 =cv2.resize(img2,(500,500))
    cv2.imshow('images.jpg',img1)
    print("Error: Images have different dimensions")
else:
    
    #convert the images to gray scale
    gray_1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
   

    #Calculating the SSIM score /comparing the images
    (score,diff) = compare_ssim(gray_1,gray_2, full=True)
    diff = (diff * 225 / np.max(diff)).astype(np.uint8)


    #print the similarity score 
    print("Status score : :{:.2f}".format(score))
    cv2.imshow(" Image", diff)
    cv2.imshow('img1',img1)
    cv2.imshow('img',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

