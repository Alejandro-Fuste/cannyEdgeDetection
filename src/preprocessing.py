from src.utils.read_grayscale_image import read_grayscale_image
from src.gaussian_kernel import create_gaussian_kernel
from src.derivative_gaussian_kernel import generate_derivative_gaussian_kernel
from src.convolution import convolve_image_with_kernel
from src.utils.plot_results import display_matrix

golfer_image = "../data/images/golfer_grayscale.jpg"
bear_image = "../data/images/bear_grayscale.jpg"
lions_image = "../data/images/lions_grayscale.jpg"

# Convert images to matrices
golfer_matrix = read_grayscale_image(golfer_image)
bear_matrix = read_grayscale_image(bear_image)
lions_matrix = read_grayscale_image(lions_image)

# Create Gaussian kernel (3X3 with sigma of 1)
gaussian_kernel = create_gaussian_kernel(3, 1)

# Perform convolution with gaussian kernel
filtered_image = convolve_image_with_kernel(golfer_matrix, gaussian_kernel)

display_matrix(filtered_image)
