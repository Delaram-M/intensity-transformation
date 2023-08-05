import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image

print_image(img)
plt.show()
img_cp = np.copy(img)


def line_equation_finder(x1, y1, x2, y2):
    if x1 == x2:
        alpha = 0
    else:
        alpha = (y2 - y1) / (x2 - x1)
    beta = y2 - alpha * x2
    return alpha, beta


def piecewise_linear_transformation(image, a1, b1, a2, b2):
    alpha1, beta1 = line_equation_finder(0, 0, a1, b1)
    alpha2, beta2 = line_equation_finder(a1, b1, a2, b2)
    alpha3, beta3 = line_equation_finder(a2, b2, 255, 255)
    for x, y in np.ndindex(image.shape):
        init_z = image[x, y]
        if init_z < a1:
            z = alpha1 * image[x, y] + beta1
        elif init_z < a2:
            z = alpha2 * image[x, y] + beta2
        else:
            z = alpha3 * image[x, y] + beta3
        image[x, y] = z
    return image


print("\nenter parameters. There are 2 breaking points.")
print("The 1st breaking point (a1, b1):")
a1 = float(input("a1: "))
b1 = float(input("b1: "))
print("The 2nd breaking point (a2, b2):")
a2 = float(input("a2: "))
b2 = float(input("b2: "))


img_cp = piecewise_linear_transformation(img_cp, a1, b1, a2, b2)
print_image(img_cp)
plt.show()
