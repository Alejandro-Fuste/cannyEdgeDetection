import numpy as np
from PIL import Image


def convert_image_to_numpy_array(image_path):
    # Load the image using Pillow
    img = Image.open(image_path)

    # Convert the grayscale image to a numpy array
    img_array = np.array(img)

    # Reshape the array to have a shape of (H, W, 1)
    img_array = img_array[:, :, np.newaxis]

    return img_array


# test with golfer image
# input_image_path = '../../data/images/golfer_grayscale.jpg'  # Replace with your JPEG file path
# grayscale_image = convert_image_to_numpy_array(input_image_path)
# print(grayscale_image.shape)  # Should print (H, W, 1)
# print(grayscale_image)
