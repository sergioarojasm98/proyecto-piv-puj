import os # built-in
import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install -U matplotlib
from math import log10, sqrt # built-in


INPUT_PATH = "/Users/sergiorojas/Pictures/pic_5px.png" 

def run():
    message = input("Ingrese el mensaje: ")

    def message_to_binary(message):
        if type(message) == str:

            # ord() function returns an integer representing the Unicode character
            # the Unicode Standard (version 15.0) classifies 1,481 characters as belonging to the Latin script
            # link: https://en.wikipedia.org/wiki/List_of_Unicode_characters

            return ''.join([format(ord(i), "08b") for i in message]) # string.join(iterable) -> list comprehension
        elif type(message) == bytes or type(message) == np.ndarray:
            return [format(i, "08b") for i in message]
        elif type(message) == int or type(message) == np.uint8:
            return format(message, "08b")
        else:
            raise TypeError("Input type not supported")

    def hide_message(image, secret_message):

        # the maximum bytes to encode: ( wight * height * 3 RGB arrays ) / 8 bits per character
        # however, I could use 7 bits per character since I'm only using english text
        # which means that the max. Unicode character would be the integer 126 that is 1111110

        n_bytes = image.shape[0] * image.shape[1] * 3 // 8
        # secret_message += "[END]" # you can use any string as the delimeter
        data_index = 0
        # it converts input data to binary format using message_to_binary()
        binary_secret_message = message_to_binary(secret_message)
        data_length = len(binary_secret_message) # to find the length of data that needs to be hidden
        
        for values in image:
            for pixel in values:
                # in the case of color images, the decoded images will have the channels stored in BGR order
                # link: https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html
                b, g, r = message_to_binary(pixel)
                # modify the least significant bit only if there is still data to store
                if data_index < data_length:
                    # hide the data into least significant bit of red pixel
                    pixel[0] = int(r[:-1] + binary_secret_message[data_index], 2)
                    data_index += 1
                if data_index < data_length:
                    # hide the data into least significant bit of green pixel
                    pixel[1] = int(g[:-1] + binary_secret_message[data_index], 2)
                    data_index += 1
                if data_index < data_length:
                    # hide the data into least significant bit of  blue pixel
                    pixel[2] = int(b[:-1] + binary_secret_message[data_index], 2)
                    data_index += 1
                # if data is encoded, just break out of the loop
                if data_index >= data_length:
                    break

        return image

    pic = cv2.imread(INPUT_PATH)
    os.chdir("/Users/sergiorojas/Pictures/Stego_LSB_Try001")
    cv2.imwrite("Image000001_Stego.png", hide_message(pic, message))

if __name__ == "__main__":
    run()