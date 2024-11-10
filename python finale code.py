
# Student Number: 5977320
# Name: Shaquille Huiswoud
# Description: A script to resize images in a directory and save them to an output directory.

import os
from PIL import Image

def create_output_directory(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    else:
        print(f"Output directory already exists: {output_dir}")

def resize_image(image_path, width, height):
    img = Image.open(image_path)
    resized_img = img.resize((width, height))
    return resized_img

def process_and_save_image(input_dir, output_dir, filename, width, height):
  
    img_path = os.path.join(input_dir, filename)
    resized_img = resize_image(img_path, width, height)
    
    output_path = os.path.join(output_dir, filename)
    resized_img.save(output_path)
    print(f"Resized and saved: {output_path}")

def process_images(input_dir, output_dir, width, height):
    create_output_directory(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.jfif')):
            process_and_save_image(input_dir, output_dir, filename, width, height)
        else:
            print(f"Skipping file: {filename} (not an image)")
if __name__ == "__main__":
    input_dir = r"H:\My Documents\My Pictures\Images - Python Project" #input trajectory
    output_dir = r"H:\My Documents\My Pictures\Resized Images"   #output trajectory
    width = 900
    height = 375

    process_images(input_dir, output_dir, width, height)