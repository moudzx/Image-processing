import matplotlib.pyplot as plt
import numpy as np
from skimage import data

# Step 1: Load the built-in 'camera' image
I = data.camera() # This loads the 'camera' image as a NumPy array

# Step 2: Display the original image
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off') # Hide axes for better visualization
plt.show()

# Step 3: Apply thresholding
I[I > 127] = 255 # Set pixels greater than 127 to 255
I[I <= 127] = 0 # Set pixels less than or equal to 127 to 0

# Step 4: Display the processed image
plt.imshow(I, cmap='gray')
plt.title("Processed Image")
plt.axis('off') # Hide axes for better visualization
plt.show()