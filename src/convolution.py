import numpy as np
from scipy.signal import convolve2d


# Function performs 2D convolution of a grayscale image and a kernel
# Image shape (H,W,1)
# Kernel shape (K_H, K_W)
# Returns Convolved image with (H,W,1)

def convolve_image_with_kernel(image, kernel):
    # Check if image has 3 dimensions (H,W,C) and C should be 1 for grayscale
    if len(image.shape) == 3 and image.shape[2] == 1:
        # Squeeze the third dimension to get a 2D image (H, W) for convolution.
        image_2d = np.squeeze(image, axis=2)
    else:
        raise ValueError("Input image must have shape (H, W, 1) for grayscale images.")

    # Perform 2D convolution using scipy's convolved2d
    convolved_image = convolve2d(image_2d, kernel, mode='same', boundary='fill', fillvalue=0)

    # Expand dimensions back to (H,W,1) after convolution
    convolved_image_3d = np.expand_dims(convolved_image, axis=2)

    return convolved_image_3d
