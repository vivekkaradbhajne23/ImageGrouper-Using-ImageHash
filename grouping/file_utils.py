import os
import mimetypes

def get_images_name(directory):
    filenames = []
    for f in os.listdir(directory):
        content_type = mimetypes.guess_type(f)[0]
        if content_type and content_type.startswith('image'):
            file_path = os.path.join(directory, f)
            if os.path.isfile(file_path):
                filenames.append((f, file_path))
    return filenames

def difference_hash(dhash1, dhash2):
    return bin(dhash1 ^ dhash2).count('1')
