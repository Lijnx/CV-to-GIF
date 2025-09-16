from pathlib import Path
import argparse
import imageio.v3 as iio


def load_images(dir_path):
    """
    Loads images from specified directory.

    Args:
        dir_path (str): path to the folder with images.

    Returns:
        list[Array]: list of loaded images.
    """
    images = list()
    for file in Path(dir_path).iterdir():
        if not file.is_file():
            continue
        
        try:
            images.append(iio.imread(file))
        except Exception as e:
            print(f"WARNING! Couldn't load file {file}: {e}")

    return images


def create_gif(images_dir, output_file):
    """
    Creates GIF-animation from frames.

    Args:
        images_dir (str): path to the folder with frames.
        output_file (str): name of an output file.
    """
    images = load_images(images_dir)
    if not images:
        print("ERROR! No images found.")
    else:
        if output_file[-4:] != ".gif":
            output_file += ".gif"
        try:
            iio.imwrite(output_file, images, duration=0.2)
        except Exception as e:
            print(f"ERROR! Couldn't create GIF-file: {e}")


def main():
    """
    Init application
    """
    parser = argparse.ArgumentParser(description="Creating GIF-animation from frames.")
    parser.add_argument("-i", "--images", type=str, help="Path to the folder with frames.")
    parser.add_argument("-o", "--output", type=str, help="Name of an output file.")
    args = parser.parse_args()
    create_gif(args.images, args.output)


if __name__ == "__main__":
    main()
