import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve1d

# Load the image in grayscale
image = cv2.imread('image2.png', cv2.IMREAD_GRAYSCALE)

# Define the 1D derivative kernel
kernel = np.array([-0.5, 0, 0.5])

# Apply convolution in X and Y directions
gradient_x = convolve1d(image.astype(float), kernel, axis=1)
gradient_y = convolve1d(image.astype(float), kernel, axis=0)

# Compute gradient magnitude
gradient_mag = np.sqrt(gradient_x**2 + gradient_y**2)

# Convert all to 8-bit for display
gradient_x_disp = cv2.convertScaleAbs(gradient_x)
gradient_y_disp = cv2.convertScaleAbs(gradient_y)
gradient_mag_disp = cv2.convertScaleAbs(gradient_mag)

# Display all results
titles = ['Original', 'Gradient X', 'Gradient Y', 'Gradient Magnitude']
images = [image, gradient_x_disp, gradient_y_disp, gradient_mag_disp]
plt.figure(figsize=(14, 6))
for i in range(4):
plt.subplot(1, 4, i + 1)
plt.imshow(images[i], cmap='gray')
plt.title(titles[i])
plt.axis('off')
plt.tight_layout()
plt.show()