import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image

print_image(img)
plt.show()
img_cp = np.copy(img)


def histogram_stretching(image):
    # delete 10% of pixels to find [a, b] range
    intensities = [image[x, y] for x, y in np.ndindex(image.shape)]
    intensities.sort()
    pixels_count = img.shape[0] * image.shape[1]
    removing_pixels_count = round(10 / 100 * pixels_count / 2)
    del intensities[:removing_pixels_count]
    del intensities[-removing_pixels_count:]
    a = min(intensities)
    b = max(intensities)

    # histogram stretching
    for x, y in np.ndindex(image.shape):
        init_z = image[x, y]
        if init_z < a:
            z = 0
        elif init_z > b:
            z = 255
        else:
            z = round(255 * (init_z - a) / (b - a))
        image[x, y] = z
    return image


img_cp = histogram_stretching(img_cp)
print_image(img_cp)
plt.show()
