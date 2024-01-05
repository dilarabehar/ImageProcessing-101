import cv2

# Görüntüyü yükle
image = 'image_low_contrast.jpg'
new_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

# Histogram eşitleme işlemi
equalized_image = cv2.equalizeHist(new_image)

# Orjinal ve eşitlenmiş görüntüleri gösteren subplot'lar oluştur
cv2.imshow('Original Image', new_image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
