import os
import numpy
import matplotlib
import imageio as iio

def get_images(dir_path):
    
    images = []
    for entry in os.listdir(dir_path):
        full_path = os.path.join(dir_path, entry)
        images.append(iio.imread(full_path))
    return images


images = get_images("circle-split")
iio.mimwrite("animation.gif", images, duration=0.2)