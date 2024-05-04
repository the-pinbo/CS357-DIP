from skimage import filters
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./image/ClownOrig.jpg',0)
# plt.imshow(img,cmap='grey')
# plt.show()

F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)

plt.imshow(np.log1p(np.abs(Fshift)),cmap='hot')
# plt.axis('off')
plt.show()