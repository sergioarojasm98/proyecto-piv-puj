import os # built-in
import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import matplotlib.pyplot as plt # pip install -U matplotlib
from math import log10, sqrt # built-in

def run():

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

    def show_message(image):
        binary_data = ""
        for values in image:
            for pixel in values:
                b, g, r = message_to_binary(pixel) #convert the blue ,green and red values into binary format
                binary_data += b[-1] #extracting data from the least significant bit of blue pixel
                binary_data += g[-1] #extracting data from the least significant bit of green pixel
                binary_data += r[-1] #extracting data from the least significant bit of red pixel
        # split by 8-bits
        all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
        # convert from bits to characters
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "[END]": #check if we have reached the delimeter which is "#####"
                break
        #print(decoded_data)
        return decoded_data[:-5] #remove the delimeter to show the original hidden message
    
    def decode_text():
        # read the image that contains the hidden image
        image = cv2.imread("/Users/sergiorojas/Pictures/Stego_LSB_Try001/Image000001_Text64800.PNG") #read the image using cv2.imread()     
        text = show_message(image)
        return text

    print(decode_text())

if __name__ == "__main__":
    run()