import os
import hashlib
import shutil
from PIL import Image
from utils.file_utils import difference_hash
from config import Default_Resize_Width, Default_Resize_Height, Same_Image_Value

class ImageToGroup:
    def __init__(self, filename, path):
        self.hash = self.hash_image(path)
        self.path = path
        self.filename = filename
        self.hash_path = hashlib.md5(str(self.hash).encode()).hexdigest()
        self.root = None

    def is_same_group(self, other_image):
        return difference_hash(self.hash, other_image.hash) < Same_Image_Value

    def create_root_dir(self, base):
        if not os.path.exists(os.path.join(base, self.root_rpath)):
            os.makedirs(os.path.join(base, self.root_rpath))

    def copy_to_root_dir(self, base):
        shutil.copyfile(self.path, os.path.join(base, self.root_rpath, self.filename))

    def copy(self, base):
        self.create_root_dir(base)
        self.copy_to_root_dir(base)

    def get_gray_scale_image_data(self, path, resize_width=Default_Resize_Width, resize_height=Default_Resize_Height):
        im = Image.open(path)
        smaller_image = im.resize((resize_width, resize_height))
        grayscale_image = smaller_image.convert('L')
        return grayscale_image.getdata()

    def hash_image(self, path, resize_width=Default_Resize_Width, resize_height=Default_Resize_Height):
        hash_string = ""
        pixels = list(self.get_gray_scale_image_data(path, resize_width, resize_height))
        for row in range(1, len(pixels) + 1):
            if row % resize_width:
                if pixels[row - 1] > pixels[row]:
                    hash_string += '1'
                else:
                    hash_string += '0'
        return int(hash_string, 2)

    @property
    def root_rpath(self):
        return self.root.hash_path if self.root else self.hash_path
