import numpy as np


# Performs Non-Maximum Suppression on the gradient magnitude and direction.

def non_maximum_suppression(magnitude, direction):
    
    # Initialize the output array with zeros
    rows = magnitude.shape[0]
    cols = magnitude.shape[1]
    suppressed = np.zeros((rows, cols), dtype=np.float32)

    # Convert directions to range [0, 180)
    direction = direction % 180

    # Loop through every pixel in the gradient magnitude image
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            # Get the magnitude and direction at the current pixel
            current_mag = magnitude[i, j]
            current_dir = direction[i, j]

            # Determine the two neighboring pixels to compare based on the gradient direction
            if (0 <= current_dir < 22.5) or (157.5 <= current_dir < 180):
                # 0 degree (horizontal edge), compare with left and right pixels
                neighbor1 = magnitude[i, j - 1]
                neighbor2 = magnitude[i, j + 1]
            elif 22.5 <= current_dir < 67.5:
                # 45 degrees, compare with top-right and bottom-left pixels
                neighbor1 = magnitude[i - 1, j + 1]
                neighbor2 = magnitude[i + 1, j - 1]
            elif 67.5 <= current_dir < 112.5:
                # 90 degrees (vertical edge), compare with top and bottom pixels
                neighbor1 = magnitude[i - 1, j]
                neighbor2 = magnitude[i + 1, j]
            elif 112.5 <= current_dir < 157.5:
                # 135 degrees, compare with top-left and bottom-right pixels
                neighbor1 = magnitude[i - 1, j - 1]
                neighbor2 = magnitude[i + 1, j + 1]

                # Suppress the non-maximum pixels
            if current_mag >= neighbor1 and current_mag >= neighbor2:
                suppressed[i, j] = current_mag
            else:
                suppressed[i, j] = 0

    return suppressed
