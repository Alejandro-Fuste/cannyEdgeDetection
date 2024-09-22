import math

# Define the 1D Gaussian function using the gaussian equation
def gaussian_function(x, sigma):
    exponent = - (x ** 2) / (2 * sigma ** 2)
    return math.exp(exponent)