import os
from PIL import Image
import math

def compress_images(folder_path: str, compressed_folder: str):
    if not os.path.exists(compressed_folder):
        os.makedirs(compressed_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            filepath = os.path.join(folder_path, filename)
            with Image.open(filepath) as im:
                size = os.path.getsize(filepath)
                if size > 2000:
                    quality = int(math.sqrt((2000*100)/size))
                    im.save(os.path.join(compressed_folder, filename), "JPEG", quality=quality)
                else:
                    im.save(os.path.join(compressed_folder, filename))

folder_path = input("Enter the path of the folder: ")
compressed_folder = "New folder\imagess\subb"
compress_images(folder_path, compressed_folder)
