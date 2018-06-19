import os
import numpy as np
from PIL import Image


# Merge the image, first merge horizontally so that every row contains n images
# Then merge the image vertically

def merge_image(directory, n):
    """
    :param directory: the directory of the image
    :param n: the number of images on each row
    :return: the merged image
    """

    imgs = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            imgs.append(Image.open(directory + filename))

    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

    size = len(imgs)

    rows = []
    row_range = size / n if size % n == 0 else size / n + 1
    print size, row_range
    for i in range(row_range):
        row = []
        for j in range(n):
            # If there are fewer than n images on each row, fill them with white background
            if n * i + j >= size:
                row.append(background_image(255, min_shape[1], min_shape[0]).resize(min_shape))
            else:
                row.append(imgs[n * i + j].resize(min_shape))
        rows.append(np.hstack(row))
    imgs_comb = np.vstack(np.asarray(rows))
    imgs_comb = Image.fromarray(imgs_comb)
    if not os.path.exists(directory + '/../combs/'):
        os.makedirs(directory + '/../combs/')
    imgs_comb.save(directory + '/../combs/comb.png')


def background_image (color, row, col):
    """
    :param color: color of the background
    :param row: width of the image
    :param col: height of the image
    :return: the background image
    """

    data = [[color for j in range(col)] for i in range(row)]
    img = Image.fromarray(np.uint8(data), 'L')
    return img


if __name__ == '__main__':
    merge_image('DataSet/Cropped/', 10)