from PIL import Image

img = Image.open('DataSet/test.png')
tileSize = (120, 220)
width, height = img.size

# number of rows
rows = height / tileSize[1]

# number of elements in each row
cols = width / tileSize[0]

for i in range(cols):
    for j in range(rows):
        cropped_img = img.crop((120 * i, 220 * j, 120 * (i + 1), 220 * (j + 1)))
        cropped_img.save('DataSet/test_' + str(j) + '_' + str(i) + '.png')