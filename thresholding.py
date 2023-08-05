import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image

print_image(img)
plt.show()
img_cp = np.copy(img)


def thresholding(image, threshold):
    for x, y in np.ndindex(image.shape):
        init_z = image[x, y]
        if init_z < threshold:
            z = 0
        else:
            z = 255
        image[x, y] = z
    return image


print("\nenter parameters.")
threshold = float(input("threshold: "))


img_cp = thresholding(img_cp, threshold)
print_image(img_cp)
plt.show()
