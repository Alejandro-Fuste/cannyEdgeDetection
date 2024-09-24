import numpy as np


# Performs Non-Maximum Suppression on the gradient magnitude and direction.

def non_maximum_suppression(magnitude, direction):
    # Initialize the output array with zeros
    rows, cols = magnitude.shape
    suppressed = np.zeros((rows, cols), dtype=np.float32)

    # Convert directions to range [0, 180)
    direction = direction % 180
    