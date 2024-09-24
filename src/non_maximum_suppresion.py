import numpy as np


# Performs Non-Maximum Suppression on the gradient magnitude and direction.

def non_maximum_suppression(magnitude, direction):
    # Initialize the output array with zeros
    rows, cols = magnitude.shape
    suppressed = np.zeros((rows, cols), dtype=np.float32)

    # Convert directions to range [0, 180)
    direction = direction % 180

    # Loop through every pixel in the gradient magnitude image
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Get the magnitude and direction at the current pixel
            current_mag = magnitude[i, j]
            current_dir = direction[i, j]