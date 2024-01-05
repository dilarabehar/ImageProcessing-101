import cv2

def apply_gaussian_blur(image, sigma=1.0):
    blurred_image = cv2.GaussianBlur(image, (5, 5), sigma)
    return blurred_image

# Görüntüyü oku
image_path = "cat.jpeg"
image = cv2.imread(image_path)

# Gaussian filtre uygula
blurred_image = apply_gaussian_blur(image, sigma=1.0)

# Görüntüleri OpenCV imshow kullanarak gösterme
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
