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
    strong_x, strong_y, strong_z = np.where(gradient_magnitude >= high_threshold)
    strong_x, strong_y, strong_z = np.where(gradient_magnitude >= high_threshold)


    # Mark the weak pixels
    weak_x, weak_y, weak_z = np.where((gradient_magnitude >= low_threshold) & (gradient_magnitude < high_threshold))
    result[weak_x, weak_y, weak_z] = weak_pixel

    # Remove weak pixels unless connected to strong pixels
    for i in range(1, gradient_magnitude.shape[0] - 1):
        for j in range(1, gradient_magnitude.shape[1] - 1):
            for k in range(1, gradient_magnitude.shape[2] - 1):
                if result[i, j, k] == weak_pixel:
                    # Check if the weak pixel is connected to a strong pixel in its 26-neighbor region
                    if (result[i - 1:i + 2, j - 1:j + 2, k - 1:k + 2] == strong_pixel).any():
                        result[i, j, k] = strong_pixel
                    else:
                        result[i, j, k] = 0  # Suppress weak pixel if not connected to strong pixel

    return result
