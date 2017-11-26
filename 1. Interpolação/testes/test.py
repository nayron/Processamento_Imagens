import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.bmp', 0)
# cv2.IMREAD_GRAYSCALE
# IMREAD_COLOR
# IMREAD_UNCHANGED

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100], [80, 100], 'c', linewidth=5)
# plt.show()

cv2.imwrite('lena_cinza.bmp', img)
