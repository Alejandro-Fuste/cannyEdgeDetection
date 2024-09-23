from src.convolution import convolve_image_with_kernel
from src.preprocessing import gaussian_kernel
from src.preprocessing import x_derivative, y_derivative
from src.magnitude import compute_gradient_magnitude


def canny_edge_detector(image):
    # Perform convolution with gaussian kernel
    filtered_image = convolve_image_with_kernel(image, gaussian_kernel)

    # Perform convolution with gaussian derivatives
    x_derivative_image = convolve_image_with_kernel(filtered_image, x_derivative)
    y_derivative_image = convolve_image_with_kernel(filtered_image, y_derivative)

    # Compute magnitude
    magnitude = compute_gradient_magnitude(x_derivative_image, y_derivative_image, 1.5)
    