import numpy as np
import matplotlib.pyplot as plt
from skimage import data, img_as_ubyte
from scipy.signal import convolve2d

# Step 1: Load a built-in grayscale image
I = data.camera() # Already 2D grayscale, dtype: uint8

# Step 2: Define a 3x3 averaging filter
Window = np.ones((3, 3)) / 9

# Step 3: Apply 2D filtering (same as filter2 in MATLAB)
imfilt = convolve2d(I, Window)

# Step 4: Display the original image
plt.figure()
plt.imshow(I, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Step 5: Display the filtered image (cast to uint8 for display)
plt.figure()
plt.imshow(imfilt.astype(np.uint8), cmap='gray')
plt.title("Filtered Image (Averaging)")
plt.axis('off')
plt.show()