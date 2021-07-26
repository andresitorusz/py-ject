import numpy as np
from PIL import Image


class Canvas:
    """
    Object where all shapes are going to be drawn
    """

    def __init__(self, width, length, color):
        """
        Creates a 3D numpy array and assign user color input as its color
        """
        self.width = width
        self.length = length
        self.color = color

        self.data = np.zeros((self.width, self.length, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, output_path):
        """
        Converts the current array into an image file
        """
        image = Image.fromarray(self.data, 'RGB')
        image.save(output_path)
