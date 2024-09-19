import math

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
          g_value = gaussian_function(i, sigma) * gaussian_function(j, sigma)
          row.append(g_value)
          kernel_sum += g_value
        kernel.append(row)

   
