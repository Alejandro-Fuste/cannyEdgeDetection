import numpy as np
import cv2


def compute_gradient_magnitude(x_image, y_image, sigma):
    # I_x & I_y are the images convoluted with gaussian derivatives in the x and y directions
    I_x = x_image
    I_y = y_image

    # Compute the magnitude of the gradient at each pixel
    magnitude = np.sqrt(I_x ** 2 + I_y ** 2)

    return magnitude
