import math
import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image

print_image(img)
plt.show()
img_cp = np.copy(img)

print("\nenter parameters.")
g = float(input("gamma: "))
calculated_c = float(255 / math.pow(255, g))  # 255/255^gamma <= c < 256/255^gamma


def power_low_transformation(image, gamma, c):
    for x, y in np.ndindex(image.shape):
        z = math.floor(c * math.pow(image[x, y], gamma))
        if z < 0:
            z = 0
        if z > 255:
            z = 255
        image[x, y] = z
    return image


img_cp = power_low_transformation(img_cp, g, calculated_c)
print_image(img_cp)
plt.show()
