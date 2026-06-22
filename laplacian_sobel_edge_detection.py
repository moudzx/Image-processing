import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian operator
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Apply Sobel operator in X direction
sobel_x = cv2.Sobel(image, cv2.CV_64F, dx=1, dy=0, ksize=3)

# Apply Sobel operator in Y direction
sobel_y = cv2.Sobel(image, cv2.CV_64F, dx=0, dy=1, ksize=3)

# Convert float64 images to uint8 for display
laplacian = cv2.convertScaleAbs(laplacian)
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Display results using matplotlib
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y']
images = [image, laplacian, sobel_x, sobel_y]
plt.figure(figsize=(12, 6))
for i in range(4):
	plt.subplot(1, 4, i + 1)
	plt.imshow(images[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')