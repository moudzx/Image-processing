import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure

# Step 1: Create the matrix I (equivalent to MATLAB matrix)
I = np.array([[1, 0.9, 0.8, 0.5, 0],
[1, 0.9, 0.8, 0.5, 0],
[1, 0.9, 0.8, 0.5, 0],
[1, 0.9, 0.8, 0.5, 0]])

# Step 2: Display the original matrix I
plt.imshow(I, cmap='gray')
plt.title("Original Matrix I")
plt.axis('off') # Hide the axes
plt.show()

# Step 3: Apply intensity adjustment (imadjust equivalent)
J = exposure.rescale_intensity(I, in_range=(0.5, 0.9), out_range=(0, 1))

# Step 4: Display the adjusted matrix J
plt.imshow(J, cmap='gray')
plt.title("Adjusted Matrix J")
plt.axis('off') # Hide the axes