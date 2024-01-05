import cv2
import numpy as np
import matplotlib.pyplot as plt

from utils import rescale,stack

original_image = cv2.imread(filename="dolar.jpg", flags=0)
cv2.imshow("Original Image ", original_image)

def bit_plane(original_image , bit_plane):
    bit_plane_image = np.full(original_image ,pow(2,bit_plane))
    return np.bitwise_and(original_image , bit_plane_image)

bit_plane_arrays = []

for bit_space in range(8):
    bit_plane_image = bit_plane(original_image , bit_plane)
    bit_plane_image = rescale(original_image)
    bit_plane_arrays.append(bit_plane_image)

row1 = stack(original_image , bit_plane_arrays[0] , bit_plane_arrays[1])
row2 = stack(bit_plane_arrays[2] , bit_plane_arrays[3],bit_plane_arrays[4] )
row3 = stack(bit_plane_arrays[5] , bit_plane_arrays[6] ,bit_plane_arrays[7] )
grid=np.stack((row1 , row2 , row3))
plt.imshow(grid , cmap="gray")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()