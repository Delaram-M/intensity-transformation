import math
import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image

print_image(img)
plt.show()
img_cp = np.copy(img)


def logarithmic_transformation(image):
    for x, y in np.ndindex(image.shape):
        z = math.floor(255 / math.log(256, 2) * math.log(image[x, y]+1, 2))
        if z < 0:
            z = 0
        if z > 255:
            z = 255
        image[x, y] = z
    return image


img_cp = logarithmic_transformation(img_cp)
print_image(img_cp)
plt.show()
