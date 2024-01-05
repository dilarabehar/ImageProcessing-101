import cv2
import numpy as np

def laplace_blur(image, kernel_size):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Laplace filtresi uygula
    laplace_filtered = cv2.Laplacian(gray_image, cv2.CV_64F, ksize=kernel_size)

    # Mutlak değer alarak negatif değerleri pozitife çevir
    laplace_filtered = np.abs(laplace_filtered)

    # Görüntüyü renkli hale getirme (BGR formatında)
    laplace_filtered_color = cv2.cvtColor(np.uint8(laplace_filtered), cv2.COLOR_GRAY2BGR)

    return laplace_filtered_color

image_path = "image.jpg"
image = cv2.imread(image_path)

# Laplace filtresi ile blurring işlemi uygula
blurred_image = laplace_blur(image, kernel_size=3)

# Display the original and blurred images using OpenCV imshow
cv2.imshow('Original Color Image', image)
cv2.imshow('Blurred Image with Laplace Filter', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
