import numpy as np
import matplotlib.pyplot as plt


def compute_gradient_orientation(Gx, Gy):
    # Calculates the gradient orientation using arctan function
    orientation = np.arctan2(Gy, Gx)

    # Change from radians to degrees
    orientation = np.mod(orientation + 360, 360)

    return orientation


def visualize_orientation(orientation):
    # Normalize orientation for visualization and scale to [0,1]
    normalize_orientation = orientation / 360.0

    # Create the color map (hue for angle visualization)
    plt.imshow(normalize_orientation, cmap='hsv')
    plt.colorbar(label='Orientation (degrees)')
    plt.title('Edge Orientation Visualization')
    plt.show()
