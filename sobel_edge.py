import cv2
import numpy as np

def sobel_edge_detection(image):
    # Gri tonlamalı hale getir
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Sobel kenar bulma işlemi
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

    # Kenar gücü ve yönu bulma
    edge_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    return edge_magnitude


# Görüntüyü oku
image_path = "cat.jpeg"
image = cv2.imread(image_path)

# Sobel kenar bulma işlemi
edge_magnitude = sobel_edge_detection(image)

# Görüntüleri gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Edge Magnitude', edge_magnitude.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
