import cv2 
import numpy as np
import glob 
import json
from PIL import Image
import os

#The uploaded image
base_img_path = 'test_img.jpg'
#Pth to image folder 
image_folder_path ='img_base_dir'

#load th img
base_image =Image.open(base_img_path)
base_img_array = np.array(base_image)

image_list = []

# Loop through the images in the folder
image_list = []
for filename in os.listdir(image_folder_path):
        if filename.endswith('.jpg'):
            # Load the image
            image_path = os.path.join(image_folder_path, filename)
            image = Image.open(image_path)
            
            # Convert the image to an array
            image_array = np.array(image)
            
            # Check if the image is the same as the base image
            if np.array_equal(image_array, base_img_array):
                #print(f'{filename} is the same as the base image')
                print("image is the same ")
            else:
                #print(f'{filename} is different from the base image')
                print("image is not the same")
            
            # Add the image array to the list
            image_list.append(image_array.tolist())


 # Convert the list of image arrays to JSON
#image_json = json.dumps(image_list)
    
    # Echo the JSON to the screen
#print(image_json)
