import math
from src.gaussian_function import gaussian_function

# Define the 1D Gaussian function
def gaussian_function(x, sigma):
    exponent = - (x ** 2) / (2 * sigma ** 2)
    return math.exp(exponent)

# Create the 3x3 Gaussian kernel
def create_gaussian_kernel(size, sigma):
    kernel = []
    kernel_sum = 0 # For normalizing kernel
    offset = size//2 # To keep the kernel around 0

    for i in range(-offset, offset + 1):
        row = []
        for j in range(-offset, offset + 1):
          # Calculate the 2D Gaussian value (since this is a 2D kernel)
          value = gaussian_function(i, sigma) * gaussian_function(j, sigma)
          row.append(value)
          kernel_sum += value
        kernel.append(row)

   # normalize kernel
    for i in range(size):
        for j in range(size):
            kernel[i][j] /= kernel_sum

    return kernel

size = 3
sigma = 1
gaussian_kernel = create_gaussian_kernel(size, sigma)

# Print the kernel
for row in gaussian_kernel:
    print(row)
