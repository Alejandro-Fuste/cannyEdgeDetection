from src.gaussian_function import gaussian_function

# Creates a Gaussian kernel with the gaussian function
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