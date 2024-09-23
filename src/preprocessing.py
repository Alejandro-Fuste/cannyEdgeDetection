from src.derivative_gaussian_kernel import generate_derivative_gaussian_kernel

# Generate a 3 x 3 derivative of Gaussian kernel with sigma of 1
size = 3
sigma = 1
kernel_x, kernel_y = generate_derivative_gaussian_kernel(size, sigma)

# Print the x_kernel
print("Derivative of Gaussian Kernel (X-direction):")
for row in kernel_x:
    print(row)

# Print the y_kernel
print("Derivative of Gaussian Kernel (Y-direction):")
for row in kernel_y:
    print(row)

