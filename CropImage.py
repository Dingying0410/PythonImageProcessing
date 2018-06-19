from PIL import Image
import os


def crop_image(directory, tile_size):
    """
    Crop the image, the size of each sub image is specifed in tile_size
    :param directory: the directory of the image
    :param tile_size: the size of each sub image, tile_size[0] is the width, tile_size[1] is the height
    :return: the cropped images are saved in a new directory
    """
    image = Image.open(directory + 'test.png')
    width, height = image.width, image.height

    # number of rows
    rows = height / tile_size[1]

    # number of columns
    cols = width / tile_size[0]

    if not os.path.exists(directory + 'Cropped'):
        os.makedirs(directory + 'Cropped')

    for i in range(cols):
        for j in range(rows):
            cropped_img = image.crop((120 * i, 220 * j, 120 * (i + 1), 220 * (j + 1)))
            cropped_img.save(directory + 'Cropped/test_' + str(j) + '_' + str(i) + '.png')


if __name__ == '__main__':
    crop_image('DataSet/', (120, 220))