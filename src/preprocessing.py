from src.gaussian_function import gaussian_function
from src.gaussian_kernel import create_gaussian_kernel

size = 3
sigma = 1
gaussian_kernel = create_gaussian_kernel(size, sigma)

# Print the kernel
for row in gaussian_kernel:
    print(row)
