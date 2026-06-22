from skimage import data
import matplotlib.pyplot as plt

# Load built-in grayscale image
I = data.camera()

# Create a figure with two subplots: one for the image, one for the histogram
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Show the image
ax[0].imshow(I, cmap='gray')
ax[0].set_title('Grayscale Image')
ax[0].axis('off') # Hide axis ticks

# Show the histogram
ax[1].hist(I.ravel(), bins=256, range=[0, 256])
ax[1].set_title('Histogram')
ax[1].set_xlabel('Pixel Intensity')
ax[1].set_ylabel('Frequency')

# Display both plots
plt.tight_layout()
plt.show()