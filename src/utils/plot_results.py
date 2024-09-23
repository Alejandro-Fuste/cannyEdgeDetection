from src.utils.read_grayscale_image import read_grayscale_image
import matplotlib.pyplot as plt

# path to golfer grayscale image
image_path = "../../data/images/golfer_grayscale.jpg"

# function call creates matrix
matrix = read_grayscale_image(image_path)

# Display the grayscale matrix as an image
plt.imshow(matrix, cmap="gray", vmin=0, vmax=255)
plt.colorbar()
plt.show()
