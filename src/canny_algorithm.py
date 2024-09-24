from src.utils.image_to_numpy_array import convert_image_to_numpy_array
from src.gaussian_kernel import create_gaussian_kernel
from src.derivative_gaussian_kernel import generate_derivative_gaussian_kernel
from src.convolution import convolve_image_with_kernel
from src.magnitude import compute_gradient_magnitude
from src.gradient_orientation import compute_gradient_orientation
from src.non_maximum_suppresion import non_maximum_suppression
from src.hystersis_thresholding import hysteresis_thresholding
from src.utils.plot_results import display_matrix


def canny_edge_detector(image, kernel_size, sigma):
    # Convert images to numpy arrays
    image_np_array = convert_image_to_numpy_array(image)

    # Create Gaussian kernel (3X3 with sigma of 1)
    gaussian_kernel = create_gaussian_kernel(kernel_size, sigma)

    # Perform convolution with gaussian kernel
    filtered_image = convolve_image_with_kernel(image_np_array, gaussian_kernel)

    # Generate Gaussian derivative
    x_derivative, y_derivative = generate_derivative_gaussian_kernel(kernel_size, sigma)

    # Perform convolution with gaussian derivatives
    x_derivative_image = convolve_image_with_kernel(filtered_image, x_derivative)
    y_derivative_image = convolve_image_with_kernel(filtered_image, y_derivative)

    # Compute magnitude
    magnitude = compute_gradient_magnitude(x_derivative_image, y_derivative_image, sigma)

    # Compute gradient orientation
    orientation = compute_gradient_orientation(x_derivative_image, y_derivative_image)

    # Calculate the non-maximum suppression
    nms = non_maximum_suppression(magnitude, orientation)

    # Perform Hysteresis Threshold
    threshold = hysteresis_thresholding(magnitude)

    display_matrix(filtered_image)
    display_matrix(x_derivative_image)
    display_matrix(y_derivative_image)
    display_matrix(magnitude)
    display_matrix(nms)
    display_matrix(threshold)
