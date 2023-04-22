import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img_path = 'assets/images/cute-piglet.jpg'
img = np.asarray(Image.open(img_path).convert('L'), dtype='int64')


def print_image(image):
    print(image)
    img_plot = plt.imshow(image, cmap='gray')


if __name__ == '__main__':
    print_image(img)
