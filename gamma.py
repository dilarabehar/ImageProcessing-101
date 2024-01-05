import cv2
import numpy as np
def gamma_correction(image, gamma=1.0):
    normalized_image = image / 255.0
    # Gamma düzeltmesi uygula
    corrected_image = np.power(normalized_image, gamma)
    # [0, 255] aralığına geri getir
    corrected_image = (corrected_image * 255).astype(np.uint8)
    return corrected_image

image = cv2.imread('img.png')
# Gamma düzeltme parametresi
gamma_value = 1.5
# Gamma düzeltme işlemi
result = gamma_correction(image, gamma_value)
# Giriş ve çıkış görüntülerini göster
cv2.imshow('Input Image', image)
cv2.imshow('Gamma', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
