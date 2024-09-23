from src.gaussian_kernel import create_gaussian_kernel
from src.derivative_gaussian_kernel import generate_derivative_gaussian_kernel
from src.convolution import convolve_image_with_kernel
from src.utils.plot_results import display_matrix

golfer_image = "../data/images/golfer_grayscale.jpg"
bear_image = "../data/images/bear_grayscale.jpg"
lions_image = "../data/images/lions_grayscale.jpg"

# Create Gaussian kernel (3X3 with sigma of 1)
gaussian_kernel = create_gaussian_kernel(3, 1)

# Perform convolution with gaussian kernel
filtered_image = convolve_image_with_kernel(golfer_image, gaussian_kernel)

display_matrix(filtered_image)
