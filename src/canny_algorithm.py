from src.convolution import convolve_image_with_kernel
from src.preprocessing import gaussian_kernel


def canny_edge_detector(image):
    # Perform convolution with gaussian kernel
    filtered_image = convolve_image_with_kernel(image, gaussian_kernel)
