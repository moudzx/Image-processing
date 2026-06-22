import numpy as np
import matplotlib.pyplot as plt
from skimage import data, util
from scipy.ndimage import median_filter

# Step 1: Load grayscale image
I = data.camera()

# Step 2: Add salt & pepper noise (amount = 0.02)
J = util.random_noise(I, mode='s&p', amount=0.02)

# Step 3: Convert noisy image from float [0,1] to uint8 [0,255]
J_uint8 = (J * 255).astype(np.uint8)

# Step 4: Apply 3x3 median filter
M, N = 3, 3
K = median_filter(J_uint8, size=(M, N))

# Step 5: Display noisy and filtered images
plt.figure()
plt.imshow(J_uint8, cmap='gray')
plt.title("Noisy Image (Salt & Pepper)")
plt.axis('off')
plt.figure()
plt.imshow(K, cmap='gray')
plt.title("Filtered Image (Median Filter)")
plt.axis('off')