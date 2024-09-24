from src.utils.image_to_numpy_array import convert_image_to_numpy_array
from src.gaussian_kernel import create_gaussian_kernel
from src.derivative_gaussian_kernel import generate_derivative_gaussian_kernel
from src.convolution import convolve_image_with_kernel
from src.magnitude import compute_gradient_magnitude
from src.gradient_orientation import compute_gradient_orientation, visualize_orientation
from src.utils.plot_results import display_matrix
import cv2
import numpy as np

golfer_image = "../data/images/golfer_grayscale.jpg"
bear_image = "../data/images/bear_grayscale.jpg"
lions_image = "../data/images/lions_grayscale.jpg"

# Convert images to numpy arrays
golfer_np_array = convert_image_to_numpy_array(golfer_image)
bear_np_array = convert_image_to_numpy_array(bear_image)
lions_np_array = convert_image_to_numpy_array(lions_image)

# Create Gaussian kernel (3X3 with sigma of 1)
gaussian_kernel = create_gaussian_kernel(3, 1.5)

# Perform convolution with gaussian kernel
filtered_image = convolve_image_with_kernel(golfer_np_array, gaussian_kernel)

# Generate Gaussian derivative
x_derivative, y_derivative = generate_derivative_gaussian_kernel(3, 1.5)

# Perform convolution with gaussian derivatives
x_derivative_image = convolve_image_with_kernel(filtered_image, x_derivative)
y_derivative_image = convolve_image_with_kernel(filtered_image, y_derivative)

# Compute magnitude
magnitude = compute_gradient_magnitude(x_derivative_image, y_derivative_image, 1.5)

# Compute gradient orientation
orientation = compute_gradient_orientation(x_derivative_image, y_derivative_image)



# display_matrix(filtered_image)
# display_matrix(x_derivative_image)
# display_matrix(y_derivative_image)
# display_matrix(magnitude)




