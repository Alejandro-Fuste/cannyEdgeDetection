import cv2
import matplotlib.pyplot as plt
import numpy as np

def read_grayscale_image(image_path):
    """
    
    This function takes an image, makes it a 2D matrix, and returns this matrix.  
    
    """

    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if I is None:
        raise ValueError("Image not found or unable to read.")

    return I

# code to make sure function works remove 

'''

# path to golfer grayscale image
image_path = "../../data/images/golfer_grayscale.jpg"

# function call creates matrix
matrix = read_grayscale_image(image_path)

# Display the grayscale matrix as an image
plt.imshow(matrix, cmap="gray", vmin=0, vmax=255)
plt.colorbar()
plt.show()

'''
