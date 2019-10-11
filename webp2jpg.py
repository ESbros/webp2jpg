from PIL import Image
import imghdr
import os

image_folder = '/Path to images folder/'  
file_names = os.listdir(image_folder) 

for file_name in file_names: 
    if file_name[0] != '.': 
        if imghdr.what(image_folder + file_name) == 'webp':
            im = Image.open(image_folder + file_name).convert("RGB")
            im.save(image_folder + file_name, "jpeg")
            print('WEBP image: ', file_name)
        else:
            print('Valid Image')
