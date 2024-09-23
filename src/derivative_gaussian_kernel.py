from src.gaussian_derivative import gaussian_derivative
from src.gaussian_function import gaussian_function

def generate_derivative_gaussian_kernel(size, sigma):
    kernel_x = [[0 for _ in range(size)] for _ in range(size)]
    kernel_y = [[0 for _ in range(size)] for _ in range(size)]

    center = size // 2
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            kernel_x[i][j] = gaussian_derivative(x, sigma) * gaussian_function(y, sigma)
            kernel_y[i][j] = gaussian_function(x, sigma) * gaussian_derivative(y, sigma)
    
    return kernel_x, kernel_y
