from src.gaussian_function import gaussian_function

# This function computes the derivative of the Gaussian equation
def gaussian_derivative(x, sigma):
    return -x / (sigma**2) * gaussian_function(x, sigma)