import os
from PIL import Image

def resize_image(input_dir, output_dir, width, height):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.jfif')):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            
            # Resize image
            resized_img = img.resize((width, height))
            
            # Save resized image
            output_path = os.path.join(output_dir, filename)
            resized_img.save(output_path)
            
            print(f"Resized and saved: {output_path}")
        else:
            print(f"Skipping file: {filename} (not an image)")

if __name__ == "__main__":
    # Use raw strings (r"") for all paths to avoid escape sequence issues
    input_dir = r"H:\My Documents\My Pictures\Images - Python Project"  #input directory path
    output_dir = r"H:\My Documents\My Pictures\Resized Images"  #output directory path
    width = 375  # Desired width
    height = 800  # Desired height

    resize_image(input_dir, output_dir, width, height)

