import os
import imageio.v2 as iio


def load_images(dir_path):
    """
    Loads images from specified directory
    """
    images = []
    for entry in os.listdir(dir_path):
        full_path = os.path.join(dir_path, entry)
        images.append(iio.imread(full_path))
    return images


def main():
    """
    Init application
    """
    images = load_images("frames")
    iio.mimwrite("animation.gif", images, duration=0.2)


if __name__ == "__main__":
    main()
