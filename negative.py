import numpy as np
import matplotlib.pyplot as plt
from skimage import data

# Load a sample grayscale image
I = data.camera()

# Image Negative
negative_image = 255 - I

# Display original and negative image
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(I, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(negative_image, cmap='gray')
plt.title('Negative Image')
plt.axis('off')
plt.show()