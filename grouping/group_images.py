from grouping.image_handler import ImageToGroup

class Groupter:
    def __init__(self, filenames):
        self.images_to_group = [ImageToGroup(f[0], f[1]) for f in filenames]

    def group_images(self):
        for i in range(0, len(self.images_to_group)):
            for j in range(i + 1, len(self.images_to_group)):
                i1 = self.images_to_group[i]
                i2 = self.images_to_group[j]
                if not i1.root and i1.is_same_group(i2):
                    i2.root = i1

    def save_grouped_images(self, output_dir):
        for image in self.images_to_group:
            image.copy(output_dir)

    def remove_duplicates(self, output_dir):
        for image in self.images_to_group:
            if not image.root:
                image.copy(output_dir)
