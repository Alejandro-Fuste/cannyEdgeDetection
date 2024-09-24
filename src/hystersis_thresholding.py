import numpy as np

# Function will perform hystersis thresholding with the following threshold values
low_threshold = 50
high_threshold = 100

# Constants for strong and weak pixels
weak_pixel = 75
strong_pixel = 255


def hysteresis_thresholding(gradient_magnitude):
    # Create an empty array for the result
    result = np.zeros_like(gradient_magnitude, dtype=np.uint8)

    # Mark the strong pixels
    strong_row, strong_col = np.where(gradient_magnitude >= high_threshold)
    result[strong_row, strong_col] = strong_pixel

    # Mark the weak pixels
    weak_row, weak_col = np.where((gradient_magnitude >= low_threshold) & (gradient_magnitude < high_threshold))
    result[weak_row, weak_col] = weak_pixel

    # Remove weak pixels unless connected to strong pixels

    # return result
