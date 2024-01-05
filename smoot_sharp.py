import cv2
import numpy as np
import matplotlib.pyplot as plt

def smoothing_f(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

def sharpening_f(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    sharpened_image = image - 0.5 * laplacian
    sharpened_image = sharpened_image.astype(np.uint8)
    return sharpened_image

image_path = "fruits.jpg"
original_image = cv2.imread(image_path)

# Yumuşatma işlemi
smoothed_image = smoothing_f(original_image, kernel_size=3)

# Keskinleştirme işlemi
sharpened_image = sharpening_f(original_image)

# Görüntüleri OpenCV imshow kullanarak gösterme
cv2.imshow('Original Image', original_image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
