import cv2

def read_grayscale_image(image_path):
    """
    
    This function takes an image, makes it a 2D matrix, and returns this matrix.  
    
    """

    I = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if I is None:
        raise ValueError("Image not found or unable to read.")

    return I