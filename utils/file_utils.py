import os
import shutil

def get_images_name(dir):
    """
    Get all images filename and file path in the given directory.
    :param dir: Input directory to get images from.
    :return: A list of tuples (filename, file_path).
    """
    filenames = list()
    for f in os.listdir(dir):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(dir, f)
            if os.path.isfile(file_path):
                filenames.append((f, file_path))
    return filenames

def copy_image(source, destination):
    """
    Copy an image from source to destination.
    :param source: Source image path.
    :param destination: Destination path.
    """
    if not os.path.exists(destination):
        os.makedirs(destination)
    shutil.copy(source, destination)
    
def difference_hash(dhash1, dhash2):
    return bin(dhash1 ^ dhash2).count('1')
