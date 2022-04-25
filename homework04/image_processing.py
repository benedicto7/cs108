"""CS 108 - Lab 8

This module implements image processing functions using the Python Imaging
Library (PIL) to load and display images, and NumPy to manipulate the image's
2D array of pixels. Each pixel is represented as a list of intensity values
for red, green and blue (RGB), each value between 0 (low intensity) and 255 (
high intensity). For example:
    [0, 0, 0] represents black
    [255, 255, 255] represents white
    [255, 0, 0] represents red

@author: Keith VanderLinden (kvlinden) and Ken Arnold (ka37)
@date: Spring, 2020 - ported from Java/Processing, Fall, 2010
"""


from PIL import Image
import numpy as np
from copy import deepcopy
from guizero import App, Picture


def load_image(filename):
    """ This function loads an image from the specified file. """

    # Convert pixel values to integer format in order to
    # allow arithmetic that may overflow np's default uint8.
    return np.array(Image.open(filename), dtype='int32')


def display_image(image_array):
    """ This function displays the given image in a separate GuiZero window. """

    # Clip pixel values back to 8-bit range for display.
    image = Image.fromarray(np.uint8(np.clip(image_array, 0, 255)))

    # Show the image in a guizero window.
    app = App(width=image_array.shape[1], height=image_array.shape[0])
    Picture(app, image=image)
    # Bring the guizero window to the front
    # https://stackoverflow.com/a/36191443/69707
    root = app.tk
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    app.display()

def flip_horizontal(image):
    """ This function mirrors the given image around a vertical line. """

    # Deepcopy is used to copy the original data value which will later make flipping easier. This is needed
    # because to flip the image, we need to use the original data value and perform a simple calculation so
    # that they can be flipped. Without deepcopy, the programmer need to implement a code that will reverse
    # the data values using other python codes/functions.
    
    image_copy = deepcopy(image)

    num_rows = len(image)
    num_columns = len(image[0])

    for row_index in range(num_rows):
        for column_index in range(num_columns):
            image[row_index][column_index] = image_copy[row_index][num_columns - column_index - 1]

    return image

def change_brightness(image, value):
    """ This function receives an integer from the user that will either produce a dim or brighten picture depending on the value. """
    num_rows = len(image)
    num_columns = len(image[0])

    # Increase each RGB pixel value.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [
                rgb[0] + value,
                rgb[1] + value,
                rgb[2] + value
            ]

    return image

def negative(image):
    """ This function will produce a negative image. """
    
    num_rows = len(image)
    num_columns = len(image[0])

    # Inverse each RGB pixel value.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [
                255 - rgb[0],
                255 - rgb[1],
                255 - rgb[2]
            ]

    return image

def flip_vertical(image):
    """ This function mirrors the given image around a horizontal line. """

    image_copy = deepcopy(image)

    num_rows = len(image)
    num_columns = len(image[0])

    for row_index in range(num_rows):
        for column_index in range(num_columns):
            image[row_index][column_index] = image_copy[num_rows - row_index - 1][column_index]

    return image

def gray_scale(image):
    """ This function will produce a gray image. """
    
    num_rows = len(image)
    num_columns = len(image[0])

    # each RGB pixel value.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            image[row_index][column_index] = [
                (rgb[0] + rgb[1] + rgb[2])/3]

    return image

def polarize(image):
    """ This function polarize the given image. """
    
    num_rows = len(image)
    num_columns = len(image[0])
    
    # Initialize the value as [red green blue]
    total = 0

    # Loops through the image pixel's to find the total value of red, green, and blue.
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            
            # Adds the total value for red, green, blue in [r g b] format
            total = total + rgb
            
    # Total pixel in the image.
    total_pixel = num_rows * num_columns
    
    # Average value of red, green, blue.
    avg_red = total[0] / total_pixel
    avg_green = total[1] / total_pixel
    avg_blue = total[2] / total_pixel
    
    # Loops through the image pixel's rgb to check if it is below or above average. 
    for row_index in range(num_rows):
        for column_index in range(num_columns):
            rgb = image[row_index][column_index]
            
            # Checks the rgb of red.
            if rgb[0] > avg_red:
                rgb[0] = 255
            elif rgb[0] < avg_red:
                rgb[0] = 0
                
            # Checks the rgb of green.
            if rgb[1] > avg_green:
                rgb[1] = 255
            elif rgb[1] < avg_green:
                rgb[1] = 0
            
            # Checks the rgb of blue.
            if rgb[2] > avg_blue:
                rgb[2] = 255
            elif rgb[2] < avg_blue:
                rgb[2] = 0
                
    return image
