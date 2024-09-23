import matplotlib.pyplot as plt


def display_matrix(matrix):
    # Display the grayscale matrix as an image
    plt.imshow(matrix, cmap="gray", vmin=0, vmax=255)
    plt.colorbar()
    plt.show()
