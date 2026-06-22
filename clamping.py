import matplotlib.pyplot as plt
import numpy as np
from skimage import data

# Step 1: Load the built-in 'camera' image
I = data.camera()

# Step 2: Display the original image (equivalent to imshow)
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off') # Hide axes for better visualization
plt.show()

# Step 3: Clip the pixel values (equivalent to the for-loops in MATLAB)
I = np.clip(I, 0, 255)

# Step 4: Display the processed image (equivalent to second imshow)
plt.imshow(I, cmap='gray')
plt.title("Processed Image")
plt.axis('off') # Hide axes
plt.show()