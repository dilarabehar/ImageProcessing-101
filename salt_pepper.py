import cv2
import numpy as np
from PIL import Image

def salt_and_pepper(image, salt_prob, pepper_prob):
    noisy_image = image.copy()

    # Salt noise
    salt_threshold = salt_prob
    salt_pixels = (np.random.random(image.shape) < salt_threshold)
    noisy_image[salt_pixels] = 255

    # Pepper noise
    pepper_threshold = pepper_prob
    pepper_pixels = (np.random.random(image.shape) < pepper_threshold)
    noisy_image[pepper_pixels] = 0

    return noisy_image

# Dışarıdan bir renkli resim yükleyin
image_path = "cat.jpeg"
image = np.array(Image.open(image_path))

# Salt and pepper gürültüsü ekleyerek resmi değiştir
noisy_image = salt_and_pepper(image, salt_prob=0.2, pepper_prob=0.2)

# Oluşturulan resimleri OpenCV imshow kullanarak görselleştir
cv2.imshow('Original Image', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
cv2.imshow('Noisy Image', cv2.cvtColor(noisy_image, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
