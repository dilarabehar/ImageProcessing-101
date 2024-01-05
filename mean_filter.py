import cv2
import numpy as np

def ortalama_filtre(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

image = "fruits.jpg"
image_read = cv2.imread(image)

filtered_image = ortalama_filtre(image_read, kernel_size=3)

# Görüntüleri OpenCV imshow kullanarak gösterme
cv2.imshow('Original Image', image_read)
cv2.imshow('Filtered Image', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
