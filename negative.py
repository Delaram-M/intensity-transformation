import matplotlib.pyplot as plt
import numpy as np
from main import img, print_image
from linear import linear_transformation

print_image(img)
plt.show()
img_cp = np.copy(img)

img_cp = linear_transformation(img_cp, -1, 255)
print_image(img_cp)
plt.show()
