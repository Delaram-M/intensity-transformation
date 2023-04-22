import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image

print_image(img)
plt.show()
img_cp = np.copy(img)

print("\nenter parameters.")
a = float(input("alpha: "))
b = float(input("beta: "))


def linear_transformation(image, alpha, beta):
    for x, y in np.ndindex(image.shape):
        z = alpha * image[x, y] + beta
        if z < 0:
            z = 0
        if z > 255:
            z = 255
        image[x, y] = z
    return image


img_cp = linear_transformation(img_cp, a, b)
print_image(img_cp)
plt.show()
