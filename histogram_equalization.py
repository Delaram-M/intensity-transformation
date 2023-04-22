import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image

print_image(img)
plt.show()
img_cp = np.copy(img)


def histogram_equalization_transformation(image):

    intensity_count = np.zeros(256)
    for x, y in np.ndindex(image.shape):
        intensity_count[image[x, y]] += 1
    pixels_count = image.shape[0] * image.shape[1]

    p = np.zeros(256)
    for intensity in range(255):
        p[intensity] = intensity_count[intensity] / pixels_count

    s = np.zeros(256)
    s[0] = p[0]
    for intensity in range(255):
        s[intensity] = s[intensity - 1] + p[intensity]

    g = np.zeros(256)
    for intensity in range(255):
        g[intensity] = round(255 * s[intensity])

    for x, y in np.ndindex(image.shape):
        image[x, y] = g[image[x, y]]

    return image


img_cp = histogram_equalization_transformation(img_cp)
print_image(img_cp)
plt.show()
