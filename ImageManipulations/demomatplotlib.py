import numpy as np
from matplotlib import pyplot as plt
import cv2


img = cv2.imread("clouds.jpg")
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


